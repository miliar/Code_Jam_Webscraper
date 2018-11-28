#include <stdio.h>


using namespace std;

int main()
{
    const double init_rate =2.0;
    int cases;
    char garbage[81];
    scanf("%d", &cases);
    fgets(garbage,80,stdin);
    for(int k=0;k<cases;k++)
    {
        double cost;
        double farm_rate;
        double win;
        scanf("%lf %lf %lf",&cost,&farm_rate,&win);
        fgets(garbage,80,stdin);
        double min = win/init_rate;
        if(cost >= win)
        {
            printf("Case #%d: %.7f\n",k+1,min);
            continue;
        }

        double cur_rate = init_rate;
        double spent = 0;
        while(1)
        {
            double tmp;
            double buy_time = cost/cur_rate;
            spent+=buy_time;
            cur_rate += farm_rate;
            tmp = (win/cur_rate) + spent;
            if(tmp >= min)
                break;
            
            min = tmp;

        }

        // output answer
        printf("Case #%d: %.7f\n",k+1,min);
    }
    return 0;
}
