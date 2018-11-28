#include<stdio.h>
int main()
{
    int tc,i,j,k;
    double c,f,x,time,wc,wtc,rate;
    freopen("B-large.in","r",stdin);
    freopen("boutl.out","w",stdout);
    scanf("%d",&tc);
    for(i=1;i<=tc;i++)
    {
        scanf("%lf %lf %lf",&c,&f,&x);
        time=0;
        rate=2;
        while(1)
        {
            wtc=x/rate;
            wc=(c/rate)+(x/(rate+f));
            if(wc<wtc)
            {
                time+=(c/rate);
                rate=rate+f;
            }
            else
            {
                time+=wtc;
                break;
            }
        }
        printf("Case #%d: %.7lf\n",i,time);

    }
    return 0;
}
