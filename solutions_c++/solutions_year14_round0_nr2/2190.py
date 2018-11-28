#include <iostream>

double resolve(double C, double F, double X)
{
    double producing = 2;
    double totalTime = 0;
    while (1)
    {
        double time1= C / producing + X / (producing + F);
        double time2 = X / producing;
        if (time1 < time2)
        {
            totalTime += C / producing;
            producing += F;
        }
        else
        {
            totalTime += time2;
            break;
        }
    }

    return totalTime;
}

int main(int argc, const char *argv[])
{
    int cases = 0;
    std::cin >> cases;

    for (int i = 1; i <= cases; ++i)
    {
        double C = 0;
        double F = 0;
        double X = 0;

        std::cin >> C >> F >> X;

        std::cout.precision(7);
        std::cout << "Case #" << i << ": ";
        std::cout << std::fixed << resolve(C, F, X) << std::endl;
    }

    return 0;
}
