#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <iomanip>

int main(int argc, char *argv[])
{
    int cases = 0;
    std::cin >> cases;

    std::cin.clear();
    std::cin.ignore();

    for(int i = 0; i < cases; i++)
    {
        double C;
        double F;
        double X;

        std::cin >> C;
        std::cin >> F;
        std::cin >> X;

        double rate = 2;
        double runtime = 0;

        while((runtime + X/rate) > (runtime + C/rate + X/(rate+F)))
        {
            runtime += C/rate;
            rate += F;
        }

        runtime += X/rate;

        std::cout << "Case #" << i+1 << ": ";
        std::cout << std::fixed << std::setprecision(7) << runtime;
        std::cout << std::endl;
    }
}


