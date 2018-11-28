#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
using namespace std;

int isBuy(double money, double rate, double f, double target){
    if(target/(f + rate) - (target - money)/rate >= -1e-8){
        return 0;
    }
    return 1;
}
int main()
{
    freopen("B-small-attempt1.in", "r", stdin);
    //freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while(T--){
        double rate = 2.0, time = 0.0, money = 0.0;
        double F, C, X;
        scanf("%lf%lf%lf", &C, &F, &X);
        printf("Case #%d: ", ++cas);
        if(C >= X){
            printf("%.7f\n", X / rate);
            continue;
        }
        else{
            time += C / rate;
        }
        while(isBuy(C, rate, F, X) == 1){
            rate += F;
            time += C / rate;
            money = C;
        }
        time += (X - C)/rate;
        printf("%.7f\n", time);
    }
    return 0;
}
