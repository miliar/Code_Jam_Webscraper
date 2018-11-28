#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>

using namespace std;

__uint128_t InterpretBase10BinAsBaseN(uint64_t val, uint64_t base)
{
    __uint128_t result = 0;
    __uint128_t conversion = 1;
    while (val)
    {
        result += (val % 2) * conversion;
        val /= 2;
        conversion *= base;
    }
    return result;
}

/**
 * @return Some sane divider or 0 if not possible to find... (sane means < 50000)
 */
__uint128_t FindDivider(__uint128_t val)
{
    __uint128_t maxDivider = min(val / 2, static_cast<__uint128_t>(50000));
    for (__uint128_t divider = 2; divider < maxDivider; ++divider)
    {
        if (val % divider == 0)
            return divider;
    }
    return 0;
}

std::string Print128bitInt(__uint128_t val)
{
    std::string result;
    while (val)
    {
        uint8_t digit = val % 10;
        result.insert(result.begin(), '0' + digit);
        val /= 10;
    }
    return result;
}

void FindJamcoints(uint64_t t, uint64_t n, uint64_t j)
{
    cout << "Case #" + to_string(t) + ":" << endl;
    uint64_t lowestVal = (static_cast<uint64_t>(1) << (n - 1)) + 1;
    uint64_t highestVal = (static_cast<uint64_t>(1) << n) - 1;
    for (uint64_t val = lowestVal; val <= highestVal; ++val)
    {
        // check that this value is a jamcoin
        // last digit has to be 1 (first is by the lowest/highestVal)
        if (val % 2 == 0)
            continue;
        // check the bases
        __uint128_t dividers[9];
        bool allDividersFound = true;
        for (uint64_t base = 2; base <= 10; ++base)
        {
            uint64_t index = base - 2;
            dividers[index] = FindDivider(InterpretBase10BinAsBaseN(val, base));
            if (!dividers[index])
            {
                allDividersFound = false;
                break;
            }
        }
        if (!allDividersFound)
            continue;
        // checks ok, here comes the jamcoin
        cout << Print128bitInt(InterpretBase10BinAsBaseN(val, 10)) << ' ';
        for (uint64_t base = 2; base <= 10; ++base)
        {
            if (base != 2)
                cout << ' ';
            cout << Print128bitInt(dividers[base - 2]);
        }
        cout << endl;
        // do we have enough?
        if (!--j)
            break;
    }
}

int main()
{
    uint64_t t;
    cin >> t;
    for (uint64_t i = 1; i <= t; ++i)
    {
        uint64_t n, j;
        cin >> n >> j;
        FindJamcoints(i, n, j);
    }
    return 0;
}
