#include <iostream>
#include<stdio.h>
using namespace std;
double v,tmp;
double a[10000][5];
double dog(int p1,int p2)
{
    double k1,k2;
    if (a[p1][2]==a[p2][2])
    {
        if (a[p1][2]!=tmp) return -1;
        else
        {
            if (p1==p2) return v/(a[p1][1]+a[p2][1])*2;
            else
                return v/(a[p1][1]+a[p2][1]);
        }
    }
    k2=v*(tmp-a[p1][2])/(a[p2][2]-a[p1][2]);
    k1=v*(tmp-a[p2][2])/(a[p1][2]-a[p2][2]);
    if (k1<0||k2<0) return -1;
    if (k1/a[p1][1]>k2/a[p2][1]) return k1/a[p1][1];
    return k2/a[p2][1];
}
int main()
{
    double _min,pt;
    int tt,ii,n,i,j;
    freopen("111.txt","r",stdin);
    freopen("222.txt","w",stdout);
    scanf("%d",&tt);
    for(ii=1;ii<=tt;ii++)
    {
        scanf("%d%lf%lf",&n,&v,&tmp);
        for(i=1;i<=n;i++)
        {
            scanf("%lf%lf",&a[i][1],&a[i][2]);
        }
        _min=1000000000;
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=n;j++)
            {
                pt=dog(i,j);
                if (pt!=-1&&pt<_min)
                    _min=pt;
            }
        }
        if (_min==1000000000) printf("Case #%d: IMPOSSIBLE\n",ii);
        else
            printf("Case #%d: %.9lf\n",ii,_min);
    }
    return 0;
}
