#include<stdio.h>
#include<limits>
#include<algorithm>
using namespace std;
 double comp(double a, double b)
{
return (a-b);
}
int main(){
 double C,F,X;
int T,Y;
scanf("%d",&T);
Y=T;
while(T--){
     double time,best_time,rate=0;
    //t_time=0;
    rate=2;
    scanf("%lf%lf%lf",&C,&F,&X);
    int count=0;
    best_time=X/rate;
    time=C/rate;
    rate=rate+F;
    
    while(comp(time,best_time)<0){
     best_time=min(best_time,time+(X/rate));
        time=time+(C/rate);
        rate=rate+F;
       
//        count++;

    
    }
    
    printf("Case #%d: %.7lf\n",Y-T,best_time);

}

}
