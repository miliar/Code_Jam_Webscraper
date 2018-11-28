#include<stdio.h>
#include<string.h>

double a,b,c,rt;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int amm;
    scanf("%d",&amm);
    for (int cnt=1;cnt<=amm;cnt++)
    {
        double ans=0;
        rt=2;
        scanf("%lf%lf%lf",&a,&b,&c);
        while ( c/rt > a/rt+c/(rt+b) )
        {
            ans+=a/rt;
            rt+=b;
        }
        ans+=c/rt;
        printf("Case #%d: %.10lf\n",cnt,ans);
    }
    return 0;
}

