#include <iostream>
#include <iomanip>


int main(void)
{
    int T = 0;
    std::cin >> T;

    for (int i = 0; i < T; ++i)
    {
        double C = 0.0;
        std::cin >> C;

        double F = 0.0;
        std::cin >> F;

        double X = 0.0;
        std::cin >> X;

        double timeElapsed = 0.0;
        double farmNumber = 0.0;

        while ((X - C) / (2 + farmNumber * F) > X / (2 + (farmNumber + 1) * F))
        {
            timeElapsed += C / (2 + farmNumber* F);
            ++farmNumber;
        }

        std::cout << "Case #" << i + 1 << ": " << std::fixed << std::setprecision(7)
                  << timeElapsed + (X / (2 + farmNumber * F)) << std::endl;
    }
}
