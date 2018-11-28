#include <iostream>
#include <limits>

void Case()
{
    double C,F,X;
    double farmCount = 0;
    double P = 2;
    std::cin >> C >> F >> X;
    double time = X/P;
    double timeForFarm = 0;

    std::cout.setf(std::ios::fixed);
    std::cout.precision(7);
    do
    {
        timeForFarm += C/P;
        P += F;
        double newtime = timeForFarm + X/P;
        if (newtime < time)
            time = newtime;
        else break;
    } while(true);
    std::cout << time;
}

int main()
{
    int caseCount;
    std::cin >> caseCount;
    for (int i = 1; i <= caseCount; ++i)
    {
        std::cout << "Case #" << i << ": ";
        Case();
        std::cout << std::endl;
    }
    return 0;
}
