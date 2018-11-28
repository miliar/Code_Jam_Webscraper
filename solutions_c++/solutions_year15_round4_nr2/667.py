#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>
#define INF 111111111
#define eps 1e-9
using namespace std;
int main()
{
    int T, cas = 0, i, j, n, m, k;
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    cin>>T;
    while(T--)
    {
        double v, t;
        double r[10], c[10];
        scanf("%d", &n);
        scanf("%lf%lf", &v, &t);
        for(i = 0; i < n; i++)
            scanf("%lf%lf", &r[i], &c[i]);
        printf("Case #%d: ", ++cas);
        if (n == 1)
        {
            if (fabs(c[0] - t) > eps) puts("IMPOSSIBLE");
            else printf("%.10f\n", v / r[0]);
        }
        else
        {
            if (c[1] > c[0]) swap(c[0], c[1]), swap(r[0], r[1]);
            if (fabs(c[0] - t) < eps && fabs(c[1] - t) < eps) printf("%.10f\n",  v / (r[0] + r[1]));
            else if (fabs(c[0] - t) < eps) printf("%.10f\n",  v / (r[0]));
            else if (fabs(c[1] - t) < eps) printf("%.10f\n",  v / (r[1]));
            else
            {
                if (c[0] < t || c[1] > t)
                {
                    puts("IMPOSSIBLE");
                    continue;
                }
                double k = (t - c[1]) / (c[0] - t);
                k = fabs(k);
//            double L = 0, R = v;
//            while(R - L > eps){
//                double mid = (L + R) / 2.;
//                double tm = v - mid;
//                double h = (mid * c[0] + tm * c[1]) / v;
//                if (h > t){
//                    R = mid;
//                } else L = mid;
//            }
//            double s1 = L / r[0];
                double s2 = (v * (k / (1. + k))) / r[0];
                double s1 = (v * (1. / (1. + k))) / r[1];
                double ans = max(s1, s2);
//                ans = min(ans, v / (r[0] + r[1]));

                printf("%.10f\n", ans);
            }
        }
    }
    return 0;
}
