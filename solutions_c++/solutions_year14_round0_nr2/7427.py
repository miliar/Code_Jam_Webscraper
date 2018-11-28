#include <stdio.h>
int main()
{int totalcase;
    scanf("%d",&totalcase);
    for(int o=1;o<=totalcase;o++)
    {
        double cost,extra,target;
        double rate=2.0;
        scanf("%lf %lf %lf",&cost,&extra,&target);
        double totaltime=0.0;
        while((target-cost)/rate > target/(rate+extra))
        {
            totaltime+=cost/rate;
            rate+=extra;
        }
        totaltime+=target/rate;
        printf("Case #%d: ",o);
        printf("%.7lf\n",totaltime);
    }
    return 0;
}
