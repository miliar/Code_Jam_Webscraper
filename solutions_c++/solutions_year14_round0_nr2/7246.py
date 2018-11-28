#include<stdio.h>
int main()
{
    int testcases;
    double C,F,X,rate,time;
    double eps=1e-9;
    scanf("%d",&testcases);
    for(int t=0;t<testcases;t++)
    {
        scanf("%lf%lf%lf",&C,&F,&X);
        rate=2.0;
        time=0.0;
        for(;;)
        {
            double donothingtime=time+(X/rate);
            double buyfarmtime=time+(C/rate)+(X/(rate+F));
            if(buyfarmtime+eps<donothingtime)
            {
                time=time+(C/rate);
                rate=rate+F;
            }
            else
            {
                time=time+(X/rate);
                break;
            }
        }
        printf("Case #%d: %.7lf\n",t+1,time);
    }
    return 0;
}
