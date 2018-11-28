#include <string>
#include <fstream>
#include <iostream>
#include <cstdint>
#include <vector>
#include <array>
#include <stack>
#include <unordered_map>

using LettersMap = std::unordered_map<char, uint32_t>;

std::array<LettersMap, 10> digitsMap = []()
{
    std::string digits[10] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
    std::array<LettersMap, 10> digitsMap;

    for (size_t i = 0; i < 10; ++i)
    {
        auto& digitsMapi = digitsMap[i];
        for (const auto& c: digits[i])
        {
            auto letterIt = digitsMapi.find(c);
            if (letterIt != digitsMapi.end())
                letterIt->second += 1;
            else
                digitsMapi.emplace(c, 1);
        }
    }

    return digitsMap;
}();

uint32_t exists(const LettersMap& element, const LettersMap& set)
{
    uint32_t result = 0;

    for (const auto& letter: element)
    {
        auto setIt = set.find(letter.first);
        if (setIt == set.end() || setIt->second < letter.second)
            return 0;

        if (result == 0)
            result = setIt->second / letter.second;
        else
            result = std::min(result, setIt->second / letter.second);
    }

    return result;
}

void remove(LettersMap& set, const LettersMap& element, uint32_t times = 1)
{
    for (const auto& letter : element)
    {
        if (set[letter.first] < letter.second * times)
            throw std::logic_error("This shouldn't happen!");

        set[letter.first] -= letter.second * times;
    }
}

void add(LettersMap& set, const LettersMap& element, uint32_t times = 1)
{
    for (const auto& letter : element)
    {
        set[letter.first] += letter.second * times;
    }
}

std::array<uint32_t, 10> eval(LettersMap& letters)
{
    std::stack<uint32_t> states;
    auto phone_digits = std::array<uint32_t, 10>{0};

    while (std::any_of(letters.begin(), letters.end(), [](std::unordered_map<char, uint32_t>::const_reference b) { return b.second > 0; }))
    {
        uint32_t d = 0;
        if (!states.empty())
        {
            d = states.top();
            states.pop();

            add(letters, digitsMap[d]);
            phone_digits[d] -= 1;

            d++;
        }

        for (;d < 10; ++d)
        {
            auto t = exists(digitsMap[d], letters);
            if (t > 0)
            {
                remove(letters, digitsMap[d], t);
                phone_digits[d] += t;

                for (auto i = 0; i < t; ++i)
                    states.push(d);
            }
        }
    }

    return phone_digits;
}

int main(int argc, char* argv[])
{
    if (argc != 3)
    {
        std::cerr << "Usage: " << argv[0] << " <test_file> <output_file>" << std::endl;
        return 1;
    }

    auto inputFilename = argv[1];
    std::ifstream inputFile(inputFilename);
    if (!inputFile.is_open())
    {
        std::cerr << "File not found: '" << inputFilename << "'" << std::endl;
        return 2;
    }

    auto outputFilename = argv[2];
    std::ofstream outFile(outputFilename);
    if (!outFile.is_open())
    {
        std::cerr << "Could not open file '" << outputFilename << "' for writing." << std::endl;
        return 2;
    }

    uint16_t numTestCases;
    inputFile >> numTestCases;

    for (uint16_t i = 1; i <= numTestCases; ++i)
    {
        std::string S;
        inputFile >> S;

        LettersMap letters;
        for (const auto& c : S)
        {
            auto letterIt = letters.find(c);
            if (letterIt != letters.end())
                letterIt->second += 1;
            else
                letters[c] = 1;
        }

        auto phone_digits = eval(letters);

        outFile << "Case #" << i << ": ";
        for (size_t d = 0; d < phone_digits.size(); ++d)
            for (int t = 0; t < phone_digits[d]; ++t)
                outFile << d;
        outFile << std::endl;
    }
}