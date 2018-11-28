#include <iostream>
#include <fstream>
#include <set>
#include <vector>

using namespace std;

const uint64_t MaxT = 100;

std::vector<uint64_t> ReadTasks(std::istream& is)
{
    size_t taskCount;
    is >> taskCount;
    std::vector<uint64_t> tasks;
    while (taskCount-- > 0)
    {
        uint64_t N;
        is >> N;
        tasks.push_back(N);
    }
    return std::move(tasks);
}

void RemoveDigitsSeen(uint64_t number, bool* digitsSeen, size_t& numberOfDigitsSeen)
{
    while (number > 0)
    {
        short digit = static_cast<short>(number % 10);
        if (!digitsSeen[digit])
        {
            digitsSeen[digit] = true;
            if (++numberOfDigitsSeen == 10)
            {
                return;
            }
        }
        number /= 10;
    }
}

uint64_t FindLastNumber(uint64_t N)
{
    size_t numberOfDigitsSeen = 0;
    bool digitsSeen[10] = { false };
    
    uint64_t number = N;
    for (uint64_t t = 1; t <= MaxT; ++t)
    {
        RemoveDigitsSeen(number, digitsSeen, numberOfDigitsSeen);
        if (numberOfDigitsSeen == 10)
        {
            return number;
        }
        number += N;
    }
    throw std::runtime_error("Failed to find a digit");
}

int main(int args, char** argv)
{
    //std::istream& input = std::cin;
    std::ifstream input("input.txt");
    std::vector<uint64_t> tasks = ReadTasks(input);

    std::ofstream out("output.txt");
    for (size_t i = 0; i < tasks.size(); ++i)
    {
        out << "Case #" << i + 1 << ": ";
        try
        {
            uint64_t lastNumber = FindLastNumber(tasks[i]);
            out << lastNumber << std::endl;
        }
        catch (const std::exception&)
        {
            out << "INSOMNIA" << std::endl;
        }
    }
}