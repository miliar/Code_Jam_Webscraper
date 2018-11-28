#include <cstdio>
#include <iostream>
using namespace std;
int T;
double C, F, X, c[50505], f[50505];
int main()
{
    freopen("B-small-attempt2.in", "r", stdin);
//    freopen("B-small-attempt2.out", "w", stdout);
    scanf("%d", &T);
    for ( int I(1); I <= T; I++)
    {
        scanf("%lf%lf%lf", &C, &F, &X);
        printf("Case #%d: ", I);
        c[0] = 0;
        f[0] = X / 2;
        double ans = f[0];
        for ( int i(1); i * 2 <= X; i++)
        {
            c[i] = c[i - 1] + C / (2 + (i - 1) * F);
            f[i] = c[i] + X / (2 + i * F);
            ans = min(ans, f[i]);
            // if ( f[i] > f[i-1] ){
            // 	ans = f[i-1];
            // 	break;
            // }
            printf("%d %lf\n",i,ans);
        }
        printf("%.7lf\n", ans);
    }
    return 0;
}
