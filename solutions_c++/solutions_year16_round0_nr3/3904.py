#include <string>
#include <fstream>
#include <iostream>
#include <cstdint>
#include <bitset>
#include <cmath>
#include <sstream>
#include <algorithm>

uint64_t getDivisor(uint64_t n)
{
    if (n % 2 == 0) 
        return 2;

    auto max = static_cast<uint64_t>(ceil(sqrt(n)));
    for (uint64_t i = 3; i < max; i += 2)
    {
        if (n % i == 0)
            return i;
    }

    return 0;
}

uint64_t getNumber(const std::bitset<32>& number, uint16_t base)
{
    uint64_t result = 0;
    for (auto i = 0; i < 32; ++i)
    {
        if (number[i])
            result += pow(base, i);
    }
    return result;
}

void printBits(std::ostream& os, const std::bitset<32>& number, uint16_t numbits)
{
    for (auto i = numbits - 1; i >= 0; --i)
    {
        os << (number[i] ? 1 : 0);
    }
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
    inputFile.ignore(100, '\n');

    for (uint16_t t = 1; t <= numTestCases; ++t)
    {
        uint32_t n, j;
        inputFile >> n >> j;

        outFile << "Case #" << t << ":" << std::endl;

        std::bitset<32> number(0);

        uint64_t numresults = 0;
        for (uint64_t baseNumber = 0; numresults < j; baseNumber++)
        {
            number = baseNumber << 1;
            number[0] = 1;
            number[n - 1] = 1;

            std::ostringstream oss;
            printBits(oss, number, n);
            int base;
            for (base = 2; base <= 10; ++base)
            {
                auto num = getNumber(number, base);

                auto div = getDivisor(num);
                if (div != 0) 
                {
                    oss << ' ' << div;
                }
                else
                {
                    break;
                }
            }

            if (base > 10) 
            {
                outFile << oss.str() << std::endl;
                numresults++;
            }
        }
    }  
}
