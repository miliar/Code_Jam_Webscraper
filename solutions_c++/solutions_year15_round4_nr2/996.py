#include <cstdio>
#include <cstring>
#include <cmath>

#define esp 1e-12

const int N =  110;
double r[N], c[N];
int n;
double v, x;

inline double max(double a, double b)
{
    return  a > b ? a : b;
}
int main()
{

    freopen("in2.txt", "r", stdin);
    freopen("out2.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) 
    {
        scanf("%d%lf%lf", &n, &v, &x);
        for (int i = 0; i < n; ++i)
            scanf("%lf%lf", &r[i], &c[i]);
        printf("Case #%d: ", cas);
        if (n == 1)
        {
            if (fabs(c[0] - x) > esp)
                puts("IMPOSSIBLE");
            else
                printf("%.9f\n", v / r[0]);
            continue;
        }
        if (r[1] * fabs(c[0]-c[1]) < esp || r[0] * fabs(c[0] - c[1]) < esp)
        {
            if (fabs(c[0] - x) > esp)
                puts("IMPOSSIBLE");
            else
                printf("%.9f\n", v / (r[0]+r[1]));
            continue;

        }
        double t2 = v * (x - c[0]) / (r[1] * (c[1] - c[0]));
        double t1 = v * (x - c[1]) / (r[0] * (c[0] - c[1]));
        if (t1 < 0 || t2 < 0)
        {
            puts("IMPOSSIBLE");
            continue;
        }

        printf("%.9f\n", max(t1, t2) + esp);
            
    }
    return 0;
}
