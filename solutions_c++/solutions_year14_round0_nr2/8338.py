#include <cstdlib>
#include <cstdio>

double minTime(double c, double f, double x, double rate, double quote)
{
    if (quote <= c)
        return x / rate;
    double farmTime = c / rate;
    double rest = minTime(c, f, x, rate + f, quote - c);
    double directTime = x / rate;

    return farmTime + rest < directTime ? farmTime + rest : directTime;
}

int main()
{
    int t;
    scanf("%d", &t);
    for (int idx = 0; idx < t; ++idx)
    {
        double rate = 2.0;
        double c, f, x;
        scanf("%lf %lf %lf", &c, &f, &x);

        double quote = x;
        double result = x / rate;
        double farmTime = 0.0;
        double restTime;
        while (quote > c)
        {
            farmTime += c / rate;
            rate += f;
            restTime = x / rate;
            if (result >= farmTime + restTime)
            {
                result = farmTime + restTime;
            }
            quote -=c;
        }

        printf("Case #%d: %.7f\n", idx + 1, result);
    }
    return 0;
}
