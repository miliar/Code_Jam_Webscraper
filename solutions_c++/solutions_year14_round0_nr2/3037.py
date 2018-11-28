#include<stdio.h>
main()
{
    int i,j,k,ti,te;
    double rate,goal,farm,add,sum,x,y;

    freopen("B-large.in","r",stdin);
    freopen("output.out","w",stdout);

    scanf("%d",&te);
    for(ti=1;ti<=te;ti++)
    {
        scanf("%lf %lf %lf",&farm,&add,&goal);
        sum=0;
        rate=2;
        while(1)
        {
            x=farm/rate+goal/(rate+add);
            y=goal/rate;
            //printf("%lf or %lf\n",x,y);
            if(x<=y)
            {
                sum+=farm/rate;
                rate+=add;
            }
            else
            {
                sum+=y;
                break;
            }
        }
        printf("Case #%d: %.7lf\n",ti,sum);
    }
}
