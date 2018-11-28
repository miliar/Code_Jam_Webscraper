#include<stdio.h>
#define max 100009

double minimum(double a,double b)
{
    return (a<b?a:b);
}

int main()
{
    int i,t;
    double c,f,x,min,res,total,fram,nf,t1,t2;
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%lf %lf %lf",&c,&f,&x);
        min=max;
        total=0.0;
        fram=0.0;
        t1=x/2.0;
        min=minimum(min,t1);
        nf=2;
        while(1)
        {
            fram=c/nf;
            nf=nf+f;
            double cost=x/nf;
            total=total+fram+cost;
            t2=total;
            if(t1<t2)
                break;
            t1=t2;
            min=minimum(min,total);
            if(min)
            total=total-cost;
        }
        printf("Case #%d: %.7lf\n",i,min);
    }
    return 0;
}
