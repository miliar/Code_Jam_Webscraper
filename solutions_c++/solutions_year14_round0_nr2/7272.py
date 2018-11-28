#include <iostream>
#include <iomanip>


int main(void)
{
    int T = 0;
    std::cin >> T;
    for (int i = 0; i < T; ++i)
    {
        double C = 0.0, F = 0.0, X = 0.0, t = 0.0, f = 0.0;
        std::cin >> C >> F >> X;
        for (; (X - C) / (2 + f * F) > X / (2 + (f + 1) * F); ++f)
            t += C / (2 + f * F);
        std::cout << "Case #" << i + 1 << ": " << std::fixed << std::setprecision(7) << t + (X / (2 + f * F)) << std::defaultfloat << std::endl;
    }
}
