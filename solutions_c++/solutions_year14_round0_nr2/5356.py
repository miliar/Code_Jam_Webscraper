#include <stdio.h>
int main()
{
//    freopen("B.in", "r", stdin);
//    freopen("B.out", "w", stdout);
    int t, kase=0;
    double c, f, x, s;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%lf%lf%lf", &c, &f, &x);
        s = 2.0;
        int k = (int)((f*x-2*c)/c/f);
        double ans = 0;
        for(int i=0; i<k; i++)
        {
            ans += c / s;
            s += f;
        }
        ans += x / s;
        printf("Case #%d: %.7f\n", ++kase, ans);
    }
    return 0;
}
