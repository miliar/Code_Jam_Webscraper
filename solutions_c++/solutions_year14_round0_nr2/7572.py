#include<iostream>
#include<map>
#include<vector>
#include<cstdio>
using namespace std;

int main(){
    int t, count = 1;
    double C,F,X;
    scanf("%d", &t);
    while(t--){
        scanf("%lf%lf%lf", &C, &F, &X);
        double rate=2;
        double timeFarm, timeWithout, total = 0;
        int flag = 1;
        while( flag ){
            timeFarm = (C/rate)+(X/(rate+F));
            timeWithout = X/rate;
            if( timeFarm < timeWithout){
                total += C/rate;
                rate += F;
            }else{
                total += X/rate;
                flag = 0;
            }
        }
        printf("Case #%d: %.7lf\n",count++, total);
    }
    return 0;
}