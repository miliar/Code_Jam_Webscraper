#include <iostream>
#include <stdio.h>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out","w",stdout);
    int o, cas=0;
    scanf("%d",&o);
    while (o--)
    {
        double c,f,x,ans;
        scanf("%lf%lf%lf",&c,&f,&x);
        double v=2.0;
        ans=x/v;
        double t=0;
        while (t<ans)
        {
            t+=c/v; v+=f;
            ans=min(ans,t+x/v);
        }
        printf("Case #%d: ",++cas);
        printf("%.7lf\n",ans);
    }
    return 0;
}