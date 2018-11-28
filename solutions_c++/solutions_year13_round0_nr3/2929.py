#include <cstdlib>
#include <iostream>
#include <cmath>

bool isFair(int check)
{
    char buffer[6] = "\0\0\0\0\0";
    char * soln = itoa(check, buffer,10);
    int sz = 0;
    while(*(soln++)) sz++;
    if(sz == 1)
        return true;
    for(int i = 0; i < sz/2; i++)
        if(buffer[i] != buffer[sz - 1])
            return false;
    return true;
}

bool isSquare(int check)
{
    for(int i = 0; i <= check; i++)
        if( i * i == check && isFair(i))
            return true;
    return false;
}

int main()
{
    int trials;
    std::cin >> trials;
    for(int i = 0; i < trials; i++)
    {
        int count = 0;
        int min;
        int max;
        std::cin >> min;
        std::cin >> max;
        for(min; min <= max; min++)
        {
            if(isFair(min) && isSquare(min))
            {
                count++;
            }
        }
        std::cout << "Case #" << i + 1 << ": " << count << '\n';
    }


}