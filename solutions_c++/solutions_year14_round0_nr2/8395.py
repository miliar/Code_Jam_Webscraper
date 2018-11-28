#include <algorithm>
#include <stdio.h>
#include <limits>

const int maxn = 10000000;

double check(double c, double f, double x, int n)
{
    double tm = 0.0, y = 2.0;
    for (int i = 0; i < n; ++i) {
        tm += c / y;
        y += f;
    }
    tm += x / y;
    return tm;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        double c, f, x;
        scanf("%lf%lf%lf", &c, &f, &x);
        int l = 0, r = maxn;
        while (r - l > 3) {
            int m1 = (2 * l + r) / 3;
            int m2 = (l + 2 * r) / 3;
            if (check(c, f, x, m1) < check(c, f, x, m2))
                r = m2;
            else
                l = m1;
        }
        if (r == maxn)
            fprintf(stderr, "oops %d\n", i + 1);
        double res = std::numeric_limits<double>::infinity();
        for (int j = l; j < r; ++j)
            res =  std::min(res, check(c, f, x, j));
        printf("Case #%d: %.7f\n", i + 1, res);
    }
}                               