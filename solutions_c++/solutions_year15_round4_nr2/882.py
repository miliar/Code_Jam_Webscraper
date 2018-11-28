#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

int main()
{
    freopen("x.in", "r", stdin);
    freopen("x.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        int n;
        double V, C, r1, c1, r2, c2;
        scanf("%d%lf%lf", &n, &V, &C);
        scanf("%lf%lf", &r1, &c1);
        if (n == 1)
        {
            if (fabs(c1 - C) > 1e-6) printf("Case #%d: IMPOSSIBLE\n", cas);
            else printf("Case #%d: %.7f\n", cas, V / r1);
            continue;
        }
        scanf("%lf%lf", &r2, &c2);
        if ((c1 - C) * (c2 - C) > 0)
        {
            printf("Case #%d: IMPOSSIBLE\n", cas);
            continue;
        }
        if (fabs(c1 - c2) < 1e-6)
        {
            printf("Case #%d: %.7f\n", cas, V / (r1 + r2));
            continue;
        }
        double t1 = V * (C - c2) / (c1 - c2) / r1;
        double t2 = (V - t1 * r1) / r2;
//        cout<<t1<<" "<<t2<<endl;
//        if (fabs(t2) < 1e-6)
//        {
//            swap(t1, t2);
//        }
//        if (fabs(t1) < 1e-6) printf("Case #%d: %.7f\n", cas, t2);
//        else printf("Case #%d: %.7f\n", cas, max(t1, t2));
        printf("Case #%d: %.7f\n", cas, max(t1, t2));
    }
    return 0;
}
