#include<stdio.h>
int main()
{
    int t;
    int i,j,k;
    #ifndef ONLINE_JUDGE
        freopen("input.c","r",stdin);
        freopen("output.c","w",stdout);
    #endif // ONLINE_JUDGE
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        double c,f,x;
        scanf("%lf%lf%lf",&c,&f,&x);
        double val=x;
        double current_rate=2.0;
        double future_rate=2.0+f;
        double time1=0.0;
        double time2=0.0;
        double ttime=0.0;
        while(1)
        {
            time1=c/current_rate;
            time2=x/future_rate;
            if((time1+time2)>x/current_rate)
            {
                ttime+=x/current_rate;
                break;
            }
            else
            {
                ttime+=c/current_rate;
                current_rate+=f;
                future_rate+=f;
            }
        }
        printf("Case #%d: %.7f\n",i,ttime);
    }
    return 0;
}
