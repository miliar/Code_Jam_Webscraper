#include <cstdint>
#include <cmath>
#include <iostream>
#include <string>

using namespace std;

void SolveTestCaseT(uint8_t t, uint8_t k, uint8_t c, uint8_t s)
{
    cout << "Case #" << to_string(t) << ": ";
    uint64_t kToCMin1 = static_cast<uint64_t>(pow(static_cast<long double>(k), static_cast<long double>(c - 1)) + 0.5);
    for (uint8_t n = 0; n < k; ++n)
    {
        if (n != 0)
            cout << ' ';
        uint64_t indexToCheck = kToCMin1 * n;
        cout << indexToCheck + 1;
    }
    cout << std::endl;
}

int main()
{
    uint16_t t;
    cin >> t;
    for (uint8_t i = 1; i <= t; ++i)
    {
        uint16_t k, c, s;
        std::cin >> k >> c >> s;
        SolveTestCaseT(i, k, c, s);
    }
    return 0;
}
