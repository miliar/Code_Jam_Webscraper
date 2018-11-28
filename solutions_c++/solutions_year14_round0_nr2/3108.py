#include <stdio.h>

int main()
{
    int T = 0;
    double C = 0;  // Cost
    double F = 0;  // Add Rate
    double X = 0;  // Gole
    double rate = 2, result = 0;
    double not_build_time = 0, build_time;
    scanf("%d", &T);
    for (int cases = 1; cases <= T; ++cases)
    {
        rate = 2;
        result = 0;
        scanf("%lf%lf%lf", &C, &F, &X);
        while (true)
        {
            not_build_time = X / rate;
            build_time = C / rate + X / (rate + F);
            if (not_build_time <= build_time)
            {
                result += X / rate;
                break;
            }
            // build
            result += C / rate;
            rate += F;
        }
        printf("Case #%d: %.7f\n", cases, result);
    }
    return 0;
}
