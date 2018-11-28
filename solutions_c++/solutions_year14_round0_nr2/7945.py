#include<stdio.h>
int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("B_big.out","w",stdout);
    int t,cas=1;
    double c,f,x,sum,p,a,b;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        sum=0;
        p=2;
        a=x/p;
        b=c/p+x/(p+f);
        while(1)
        {
            if(a<b)
            {
                sum+=a;
                break;
            }
            sum+=c/p;
            p+=f;
            a=x/p;
            b=c/p+x/(p+f);
        }
        printf("Case #%d: %.7f\n",cas++,sum);
    }
    return 0;
}
