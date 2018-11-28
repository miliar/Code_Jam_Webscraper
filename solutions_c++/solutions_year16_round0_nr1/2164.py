#include <cstdio>
#include <cstdint>
#include <array>
#include <algorithm>

using namespace std;

bool FindLastNumber(unsigned n, uint64_t* lastNumber)
{
    if (n == 0)
    {
        return false;
    }

    array<bool, 10> seenDigit{};

    uint64_t counter = 0;

    do
    {
        ++counter;

        uint64_t currentNum = counter * n;

        while (currentNum)
        {
            seenDigit[currentNum % 10] = true;
            currentNum /= 10;
        }

    } while (!std::all_of(seenDigit.cbegin(), seenDigit.cend(), [](bool seen) {return seen; }));

    *lastNumber = counter * n;
    return true;
}

int main ()
{
    unsigned numTestCases;

    scanf_s("%u", &numTestCases);

    for (unsigned testCase = 1; testCase <= numTestCases; ++testCase)
    {
        unsigned n;
        scanf_s("%u", &n);

        uint64_t lastNumber;
        bool found = FindLastNumber(n, &lastNumber);

        printf_s("Case #%u: ", testCase);

        if (found)
        {
            printf_s("%I64u", lastNumber);
        }
        else
        {
            printf_s("INSOMNIA");
        }

        printf_s("\n");
    }

    return 0;
}
