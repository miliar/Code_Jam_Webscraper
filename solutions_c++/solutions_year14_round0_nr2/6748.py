#include <iostream>
#include <stdint.h>
#include <limits>

typedef std::numeric_limits<double> dbl;

void round(int32_t r)
{
    double c = 0, f = 0, x = 0;
    std::cin >> c >> f >> x;

    double rate = 2.0;
    double spent = 0;

    while(true)
    {
        double secs_to_go = x / rate;
        double secs_with_next_to_go = (c / rate) + x / (rate + f);

        //std::cout << "c=" << c << " rate=" << rate << " x=" << x << " f=" << f << std::endl;

        if(secs_to_go > secs_with_next_to_go)
        {
            spent += c / rate;
            rate += f;
        }
        else
        {
            spent += x / rate;
            break;
        }
    }
    std::cout << "Case #" << r << ": " << spent << std::endl;
}

int main()
{
    int32_t rn = 0;
    std::cin >> rn;

    std::cout.precision(dbl::digits10);

    for(int32_t r = 1; r <= rn; r++)
    {
        round(r);
    }

    return 0;
}
