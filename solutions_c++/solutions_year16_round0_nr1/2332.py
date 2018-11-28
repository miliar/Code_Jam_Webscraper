#include <iostream>
#include <fstream>

int isGood(int x)
{
    if(x == 0)
        return 0;

    bool digits[10];
    for(int j(0); j < 10; j++)
    {
        digits[j] = false;
    }

    for(int j(1); j <= 2000; j++)
    {
        int test(j*x);

        while(test != 0)
        {
            int tmp = test%10;
            digits[tmp] = true;

            test -= tmp;
            test /= 10;
        }

        for(int i(0); i < 10; i++)
        {
            if(!digits[i])
            {
                break;
            }
            else if(i == 9)
            {
                return j*x;
            }
        }
    }
    return 0;
}

int main()
{
    std::ifstream f("in");
    std::ofstream o("out");

    int nb(0);
    f >> nb;

    for(int i(0); i < nb; i++)
    {
        int test(0);
        f >> test;

        int tmp(isGood(test));

        if(test == 0)
        {
            o << "Case #" << i+1 << ": INSOMNIA" << std::endl;
        }
        else
        {
            o << "Case #" << i+1 << ": " << tmp << std::endl;
        }
    }

    return 0;
}
