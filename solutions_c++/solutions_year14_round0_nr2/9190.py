// vim:set sw=4 et smarttab:
// Qualification Round 2014

#include <cstdio>
#include <cassert>

double c, f, x;

double solve()
{
    double t_farm = 0;
    double rate = 2.0;
    double min = x / rate;
    while (true)
    {
        t_farm += c / rate;
        if (t_farm >= min)
            break;
        rate += f;
        if (t_farm + x / rate < min)
            min = t_farm + x / rate;
    }
    return min;
}

int main()
{
    int ntc;
    scanf("%d", &ntc);
    for (int tc = 1; tc <= ntc; ++tc)
    {
        scanf("%lf%lf%lf", &c, &f, &x);
        double answer = solve();
        printf("Case #%d: %.7lf\n", tc, answer);
    }
}
