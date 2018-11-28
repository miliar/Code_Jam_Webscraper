#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;


int main(){
    freopen("input.txt", "r", stdin) ;
    freopen("output.txt", "w", stdout) ;
    int T, cas = 1 ;
    scanf("%d", &T) ;
    while (T--){
        double C, F, X ;
        scanf("%lf %lf %lf", &C, &F, &X) ;
        //dp[2] = 0 ;
        double pre = 0 ;
        double res = X / 2.0 ;
        double cur = 2 + F ;
        for (int i = 0; i < 200000; i++){
            pre += C / (cur - F) ;
            res = min(res, pre + X / cur) ;
            cur += F ;
        }
        printf("Case #%d: %.7lf\n", cas++, res) ;
    }
    return 0;
}
