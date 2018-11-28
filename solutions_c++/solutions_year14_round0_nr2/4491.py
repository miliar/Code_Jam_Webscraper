#include <cstdio>
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("1.txt","w",stdout);
    int t,cc;
    double c,f,x,ans,now;
    scanf("%d",&t);
    for (cc=1;cc<=t;cc++)
    {
        now=2;
        ans=0.0;
        scanf("%lf%lf%lf",&c,&f,&x);
        if (c>=x)
        {
            printf("Case #%d: %.7f\n",cc,x/2);
            continue;
        }
        ans+=c/2;
        while ((x-c)/now>x/(now+f))
        {
            now+=f;
            ans+=c/now;
        }
        ans+=(x-c)/now;
        printf("Case #%d: %.7f\n",cc,ans);
    }
    return 0;
}
