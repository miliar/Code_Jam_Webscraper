#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <cmath>
using namespace std;
#define eps 1e-6

double r[111],c[111];

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int t,n;
    double v,x;
    scanf("%d",&t);
    for (int cas=1;cas<=t;++cas)
    {
        scanf("%d%lf%lf",&n,&v,&x);
        for (int i=1;i<=n;++i) scanf("%lf%lf",r+i,c+i);
        printf("Case #%d: ",cas);
        if (n==1)
        {
            if (c[1]!=x) puts("IMPOSSIBLE");
            else printf("%.12f\n",v/r[1]);
        }
        else if (n==2)
        {
            if (c[1]==c[2])
            {
                if (c[1]!=x) puts("IMPOSSIBLE");
                else printf("%.12f\n",v/(r[1]+r[2]));
                continue;
            }
            if ((x>c[1]&&x>c[2])||(x<c[1]&&x<c[2]))
            {
                puts("IMPOSSIBLE");
                continue;
            }
            double V1,V2;
            V1=v*(x-c[2])/(c[1]-c[2]);
            V2=v-V1;
            printf("%.12f\n",max(V1/r[1],V2/r[2]));
        }
    }
    return 0;
}
