#include <cstdio>
#include <algorithm>

using namespace std;
int t, o, i, m, p, u, pf, pa, kk, a[1005];
double x, n[1005], k[1005];
int ok(int x)
{
    int i;
    for(i=1;i<=x;i++)
        if(n[m-x+i]<k[i]) return 0;
    return 1;
}
int main()
{
    freopen("4.in", "r", stdin);
    freopen("4.out", "w", stdout);
    scanf("%d", &t);
    for(o=1;o<=t;o++)
    {
        scanf("%d", &m);
        for(i=1;i<=m;i++)
            scanf("%lf", &n[i]);
        for(i=1;i<=m;i++)
            scanf("%lf", &k[i]);
        pf=0;
        pa=0;
        sort(n+1, n+m+1);
        sort(k+1, k+m+1);
        //for(i=1;i<=m;i++)
        //    if(n[i]>k[m-i+1]) pf++;
        //for(i=1;i<=m;i++)
        //    if(n[i]>k[i]) pa++;
        //if(pa>pf) pf=pa;
        p=0;
        u=m;
        while(p<=u)
        {
            kk=(p+u)/2;
            if(ok(kk))
            {
                x=kk;
                p=kk+1;
            }
            else u=kk-1;
        }
        pf=x;
        kk=1;
        pa=0;
        for(i=1;i<=m;i++)
        {
            if(n[i]<k[1])
                k[i]=-1;
            else if(n[i]>k[m])
            {
                k[i]=-1;
                pa++;
                sort(k+1,k+m+1);
            }
            else
            {
                p=i;
                u=m;
                while(p<=u)
                {
                    kk=(p+u)/2;
                    if(k[kk]>n[i]&&k[kk-1]<n[i])
                    {
                        k[kk]=-1;
                        break;
                    }
                    else if(k[kk]<n[i]) p=kk+1;
                    else u=kk-1;
                }
                sort(k+1,k+m+1);
            }
        }
        printf("Case #%d: %d %d\n", o, pf, pa);
    }
    return 0;
}
