#include <cstdio>
#include <cmath>
#include <utility>
#include <algorithm>
using namespace std;
typedef long double ld;
ld a[110],b[110];
int n,p[110];
bool cmp(int x,int y)
{
    return(b[x]<b[y]);
}
int main()
{
    int T;
    scanf("%d",&T);
    while (T--)
    {
        int n;
        ld V,X;
        double xx,yy;
        scanf("%d%lf%lf",&n,&xx,&yy);
        V=xx,X=yy;
        ld sum=0,tot=0;
        for (int i=1;i<=n;i++)
        {
            double x,y;
            scanf("%lf%lf",&x,&y);
            a[i]=x,b[i]=y;
            b[i]-=X;
            p[i]=i;
            sum+=a[i];
            tot+=a[i]*b[i];
        }
        sort(p+1,p+n+1,cmp);
        static int id=0;
        printf("Case #%d: ",++id);
        if (b[p[1]]>0 || b[p[n]]<0)
            printf("IMPOSSIBLE\n");
        else
        {
            if (tot>0)
                for (int i=n;i;i--)
                {
                    int x=p[i];
                    if (fabs(tot)<1e-10)
                        break;
                    if (tot<=a[x]*b[x])
                    {
                        sum-=tot/b[x];
                        break;
                    }
                    else
                    {
                        tot-=a[x]*b[x];
                        sum-=a[x];
                    }
                }
            else if (tot<0)
                for (int i=1;i<=n;i++)
                {
                    int x=p[i];
                    if (fabs(tot)<1e-10)
                        break;
                    if (tot>=a[x]*b[x])
                    {
                        sum-=tot/b[x];
                        break;
                    }
                    else
                    {
                        tot-=a[x]*b[x];
                        sum-=a[x];
                    }
                }
            printf("%.10f\n",double(V/sum));
        }
    }
    return(0);
}

