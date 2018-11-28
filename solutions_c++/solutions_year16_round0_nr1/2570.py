#include <iostream>
#include <stdint.h> // uint_fast64_t
#include <string>
#include <cassert>
#include <limits>

using namespace std;

constexpr uint_fast8_t count (const bool (&ten_digits)[10])
{
    int c = 0;
    for (auto d: ten_digits)
        c += d ? 1 : 0;
    return c;
}

void sheep (uint_fast64_t n)
{
    bool ten_digits[10] = {0};
    auto last_count = count(ten_digits);


    for (uint_fast64_t m=1; ; ++m)
    {
        if (m > 10000000000000000000ULL) //numeric_limits<decltype(n)>::max() / n)
        {
            std::cout << "INSOMNIA";
            return;
        }

        for (uint_fast64_t xxxx = m * n; xxxx > 0; xxxx /= 10)
        {
            uint_fast8_t digit = xxxx % 10;

            if (ten_digits[digit] == false)
            {
                auto c = count(ten_digits);
                if (c == 9)
                {
                    std::cout << (m * n);
                    return;
                }

                ten_digits[digit] = true;
            }
        }

        if ((m % 100) == 0)
        {
            auto c = count(ten_digits);
            if ( c == last_count )
            {
                std::cout << "INSOMNIA";
                return;
            }
            last_count = c;
        }
    }
}

int main()
{
    int t;
    std::cin >> t;
    assert(1 <= t);
    assert(     t <= 100);

    for (int i=1; i<=t; ++i)
    {
        std::cout <<"Case #"<< i <<": ";

        uint_fast64_t n;
        std::cin >> n;
        assert(0 <= n);
        assert(     n <= 1'000'000);

        sheep (n);

        std::cout << std::endl;
    }
}

