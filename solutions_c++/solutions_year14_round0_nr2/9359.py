#include <iostream>
#include <cstdio>

double solve(double c, double f, double x, double per)
{
    double a = x / per;
    double b = (c/per) + (x/(per+f));

    if (a < b)
        return a;

    // std::cout << (c/per) << " " <<  c << " " << f << " " << x << " " << per+f << std::endl;
    return (c/per) + solve(c, f, x, per+f);
}

int main()
{
    int cases = 0;
    scanf("%d\n", &cases);

    for (int n = 0; n < cases; n++) {
        double c, f, x;
        scanf("%lf %lf %lf\n", &c, &f, &x);

        double rtn = solve(c, f, x, 2);

        printf("Case #%d: %.07f", n+1, rtn);

        if (n < cases-1) std::cout << std::endl;
    }
    return 0;
}
