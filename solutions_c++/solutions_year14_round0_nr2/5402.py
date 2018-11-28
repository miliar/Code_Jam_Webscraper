#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main()
{
    //freopen("B-small-attempt0.in", "r", stdin);
    //freopen("B-small-attempt0.out", "w", stdout);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    double C, F, X;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t)
    {
        scanf("%lf%lf%lf", &C, &F, &X);
        double ans = X * 0.5;
        double time = 0.0;
        double rate = 2.0;
        while (time < ans)
        {
            time += C / rate;
            rate += F;
            ans = min(ans, time + X / rate);
        }
        printf("Case #%d: %.7lf\n", t, ans);
    }
    return 0;
}
