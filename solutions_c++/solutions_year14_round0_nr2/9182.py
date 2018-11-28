#include<cstdio>
#include<cstdlib>

using namespace std;
#define REP(i,a,b) \
    for(int(i)=int(a);i<=int(b);i++)

int main(){
    int T,casectr;
    double C,F,X,rate,farm_time,just_total_time,total_time,eps = 0.000001L;
    scanf("%d",&T);
    casectr = T;
    while(T--){
        scanf("%lf",&C);
        scanf("%lf",&F);
        scanf("%lf",&X);
        rate = 2.0L;
//        printf("C is now: %lf\n",C);
//        printf("F is now : %lf\n",F);
//        printf("X is now: %lf\n",X);
        just_total_time = X/rate;
        farm_time = C/rate;
        rate += F;
        total_time = farm_time + X/rate;
        while(just_total_time > total_time){
            just_total_time = total_time;
            total_time = total_time - X/rate;
            farm_time = C/rate;
            rate += F;
            total_time = total_time + farm_time + X/rate;
        }
        printf("Case #%d: %.7lf\n",casectr-T,just_total_time);
    }
    return 0;
}
