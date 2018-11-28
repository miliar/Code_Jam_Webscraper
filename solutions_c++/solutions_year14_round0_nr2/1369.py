#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;


int main()
{
    int T;
    scanf("%d", &T);

    for(int tt = 1; tt <= T; tt++)
    {
        printf("Case #%d: ", tt);
 
        double C, F, X;
        scanf("%lf%lf%lf", &C, &F, &X);

        double ans = X / 2;
        double tmp = 0;
        for(int i = 0; i < 20000000; i++)
        {
            ans = min(ans, tmp + X / (2 + i * F));
            tmp += C / (2 + i * F);
        }
        printf("%.9f\n", ans);
    }

    return 0;
}
