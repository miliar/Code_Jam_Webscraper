#include<stdio.h>
#include<stdlib.h>

int main(){
    freopen("B-small-attempt2.in","r",stdin);
    freopen("2 - small.txt","w",stdout);
    int buy;
    int round;
    double farmcost;
    double speed;
    double win;
    double rate;
    double time;
    double time_temp1;
    double time_temp2;
    double time_temp3;
    scanf("%d",&round);
    if(round<1 || round>100)scanf("%d",&round);
    for(int i=0;i<round;i++){
        buy=1;
        time=0;
        rate = 2;
        scanf("%lf",&farmcost);
        if(farmcost < 1 || farmcost > 500)scanf("%f",&farmcost);
        scanf("%lf",&speed);
        if(speed<1 || speed > 4)scanf("%f",&speed);
        scanf("%lf",&win);
        if(win<1 || win>2000)scanf("%f",&win);
        while(1){
            time_temp1 = win/rate;
            time_temp2 = win/(rate+speed);
            time_temp3 = farmcost/rate;
            if(time_temp1 < time_temp2+time_temp3)buy = 0;
            if(buy){    
                time+=time_temp3;
                rate += speed;
            }
            else{
                 time+=time_temp1;
                 break;
            }
        }
        printf("Case #%d: %.7f\n",i+1,time);  
    }
    return 0;
}
