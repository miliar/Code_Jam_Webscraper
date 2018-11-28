#include <cstdint>
#include <iostream>
#include <set>
#include <string>

using namespace std;

void PrintResult(uint64_t i, uint64_t n)
{
    std::cout << "Case #" + to_string(i) << ": ";
    if (n == 0)
        std::cout << "INSOMNIA";
    else
        std::cout << to_string(n);
    std::cout << std::endl;
}

void SolveTestCaseI(uint64_t i, uint64_t n)
{
    set<uint8_t> digits;
    for (uint8_t digit = 0; digit < 10; ++digit)
        digits.insert(digit);
    uint64_t currentN = n;
    while (true)
    {
        // remove digits for this n
        uint64_t computingReminder = currentN;
        while (computingReminder)
        {
            uint8_t reminder = computingReminder % 10;
            digits.erase(reminder);
            computingReminder /= 10;
        }
        // are we finished?
        if (digits.empty())
        {
            PrintResult(i, currentN);
            return;
        }
        // increase n
        uint64_t newN = currentN + n;
        if (newN <= currentN)
        {
            PrintResult(i, 0);
            return;
        }
        currentN = newN;
    }
}

int main()
{
    uint64_t t;
    cin >> t;
    for (uint64_t i = 1; i <= t; ++i)
    {
        uint64_t n;
        std::cin >> n;
        SolveTestCaseI(i, n);
    }
    return 0;
}
