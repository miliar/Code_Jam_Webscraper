#include <stdio.h>
#include <algorithm>
using namespace std;

#define EPS 1e-6

int main()
{
    int T;
    scanf("%d", &T);

    for (int cas = 1; cas <= T; ++cas)
    {
        double C;
        double F;
        double X;
        scanf("%lf%lf%lf", &C, &F, &X);

        int maxn = X / C + 1;
        double ret = X / 2;
        double sum = 0;
        for (int i = 1; i <= maxn; ++i)
        {
            sum += C / (2 + (i - 1) * F);
            double tmp = sum + X / (2 + i * F);
            ret = min(ret, tmp);
        }
        printf("Case #%d: %.7lf\n", cas, ret);
    }

    return 0;
}
