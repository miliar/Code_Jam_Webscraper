#include <cstdint>
#include <iostream>
#include <string>

using namespace std;

void SolveTestCaseT(uint64_t t, std::string pancakeStack)
{
    bool tosIsHappy = pancakeStack[0] == '+';
    uint64_t numOfFlips = 0;
    for (size_t i = 0; i < pancakeStack.size() - 1; ++i)
    {
        if (pancakeStack[i] != pancakeStack[i + 1])
        {
            ++numOfFlips;
            tosIsHappy = !tosIsHappy;
        }
    }
    if (!tosIsHappy)
        numOfFlips += 1;
    std::cout << "Case #" << to_string(t) << ": " << numOfFlips << std::endl;
}

int main()
{
    uint64_t t;
    cin >> t;
    for (uint64_t i = 1; i <= t; ++i)
    {
        std::string pancakeStack;
        std::cin >> pancakeStack;
        SolveTestCaseT(i, pancakeStack);
    }
    return 0;
}
