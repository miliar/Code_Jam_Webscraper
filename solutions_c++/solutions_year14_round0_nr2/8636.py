#include<cstdio>
int main()
{
    int t,r=1;
    scanf("%d",&t);
    while(r<=t)
    {
    double C,F,X,rate=2.0,t1=0,t2=0;
    scanf("%lf",&C);
    scanf("%lf",&F);
    scanf("%lf",&X);
    while(1)
    {
        t2=t1+X/rate;
       t1=t1+X/(rate+F)+C/rate;
        if(t1<t2)
        {
            t2=t2-X/rate;
            rate=rate+F;
            t1=t1-X/rate;

        }
        else
        {
            break;
        }

    }
    printf("Case #%d: %.7f\n",r,t2);
    r++;

    }
    return 0;
}
