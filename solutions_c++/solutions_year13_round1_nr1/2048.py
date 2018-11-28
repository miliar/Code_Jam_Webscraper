#include <iostream>
#include <cstdint>

//#define _USE_MATH_DEFINES
//#include <math.h>

int main()
{
    int count;
    std::cin >> count;

    for (int i = 1; i <= count; ++i)
    {
        int r;
        uint64_t t;

        std::cin >> r >> t;

        int count = 0;
        for (int j = 0; ; ++j)
        {
            double ml = (j + 1) * (2 * r + 2 * j + 1);
            if (ml <= t)
                count++;
            else
                break;
        }

        std::cout << "Case #" << i << ": " << count << std::endl;
    }

    return 0;
}