#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
const int N = 110;
int n;
double v,t;
struct P
{
    double v,t;
}a[N];
int com1(P aa,P bb)
{
    if (aa.t == bb.t) return aa.v < bb.v;
    return aa.t < bb.t;
}
int com2(P aa,P bb)
{
    if (aa.t == bb.t) return aa.v > bb.v;
    return aa.t > bb.t;
}
bool ok(double x)
{
    sort(a+1,a+n+1,com1);

    double now = 0;
    double tnow = 0;
    for (int i = 1;i <= n;i++)
    {
        if (now >= v) break;

        if (x * a[i].v + now >= v)
        {
            tnow = (now * tnow + (v - now) * a[i].t) / v;
            now = v;
        }
        else
        {
            if(now) tnow = (now * tnow + x * a[i].t * a[i].v )/ (now + x * a[i].v);
            else
                tnow = a[i].t;
            now += x * a[i].v;
        }
    }

    if (tnow > t || now < v) return 0;

    now = 0;
    tnow = 0;
    sort(a+1,a+n+1,com2);
    for (int i = 1;i <= n;i++)
    {
        if (now >= v) break;

        if (x * a[i].v + now >= v)
        {
            tnow = (now * tnow + (v - now) * a[i].t) / v;
            now = v;
        }
        else
        {
            if(now)tnow = (now * tnow + x * a[i].v * a[i].t )/(now + x * a[i].v);
            else
                tnow = a[i].t;
            now += x * a[i].v;
        }
    }

    if (tnow < t || now < v) return 0;

    return 1;
}
int main()
{
    freopen ("in.txt","r",stdin);
    freopen ("out.txt","w",stdout);
    int _;
    scanf("%d",&_);
    while (_--)
    {
        static int ca = 0;
        printf("Case #%d: ",++ca);
        scanf("%d%lf%lf",&n,&v,&t);
        for (int i = 1;i <= n;i++) scanf("%lf %lf",&a[i].v,&a[i].t);
        double l = 0,r = 1e9;

        while (r - l >= 1e-8)
        {
            double m = (l + r) / 2;

            if (ok(m)) r = m;
            else
                l = m;
        }
        if (!ok(1e9))
            puts("IMPOSSIBLE");
        else
            printf("%lf\n",l);
    }
}
