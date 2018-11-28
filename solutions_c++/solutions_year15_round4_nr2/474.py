#include <cstdio>

void solve(int tp)
{
    printf("Case #%d: ",tp);
    int n;
    double v,x;
    scanf("%d %lf%lf",&n,&v,&x);
    double a,b,c,d;
    scanf("%lf%lf",&a,&b);
    if (n == 1)
    {
        if (v == 0)
            printf("0\n");
        else if (b != x || a == 0)
            printf("IMPOSSIBLE\n");
        else
            printf("%lf\n",v/a);
        return;
    }
    scanf("%lf%lf",&c,&d);
    if (v==0)
    {
         printf("0\n");
         return;
    }
    if (d==b && b == x)
    {
        printf("%lf\n",v/(a+c));
        return;
    }
    if ((b > x && d > x) || (b < x && d < x) || (a == 0 && d != x) || (c == 0 && b != x) || (c==0 && a== 0))
    {
        printf("IMPOSSIBLE\n");
        return;
    }

    double t2 = 100000000000;
    double t1 = t2;

    if (c)t2 = v*(x-b)/ (c*(d-b));
    if (a)t1 = v*(x-d)/ (a*(b-d));

    if (t2 > t1) t1 = t2;
    printf("%lf\n",t1);
}

int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i= 1; i <= t; i++)
        solve(i);
    return 0;
}
