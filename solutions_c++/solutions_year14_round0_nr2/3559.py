#include <cstdio>
int T;
double ans,c,f,x,v;

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d", &T);
    for (int tt = 0; tt < T; tt++)
    {
        scanf("%lf%lf%lf", &c, &f, &x);
        ans = 0;
        v = 2;
        while (x/v > c/v + x/(v+f))
            ans += c/v, v += f;
        printf("Case #%d: %.8lf\n", tt + 1, ans + x / v);
    }
    return 0;
}
