#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;

double v, x;
int n;
double r[100], c[100];

bool b_small(double &ans)
{
    if ((n == 1) || (fabs(c[0] - c[1]) < 1e-10))
    {
        if (n == 2) { r[0] += r[1]; }
        if (fabs(c[0] - x) < 1e-10)
        {

            ans = v / r[0];
            return true;
        } else { return false; }
    }

    double t2 = (x * v - c[0] * v) / (c[1] * r[1] - c[0] * r[1]), t1 = (v - r[1] * t2) / r[0];
    ans = max(t2, t1);
    return (min(t2, t1) > -1e-10);
}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int test;
    scanf("%d", &test);
    for (int t = 1; t <= test; t++)
    {
        printf("Case #%d: ", t);
        scanf("%d%lf%lf", &n, &v, &x);
        for (int i = 0; i < n; i++) { scanf("%lf%lf", &r[i], &c[i]); }
        double ans = 0;
        if (b_small(ans)) { printf("%.6f\n", ans); }
        else { printf("IMPOSSIBLE\n", ans); }
    }
    return 0;
}
