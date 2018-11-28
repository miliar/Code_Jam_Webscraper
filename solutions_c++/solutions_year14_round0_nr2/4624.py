#include <cstdio>
#include <cstdlib>
#include <cstring>

double c,f,x,v,ans,t;

int main()
{
    freopen("B-small.in","r",stdin);
    freopen("b-out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        v=2;
        ans=x;
        t=0;
        while(ans>t+x/v+1e-7)
        {
            ans=t+x/v;
            t+=c/v;
            v+=f;
        }
        printf("Case #%d: %.7f\n",cas,ans);
    }
    return 0;
}
