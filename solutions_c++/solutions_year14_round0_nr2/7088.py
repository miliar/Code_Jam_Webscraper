#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
        int test;
        double rate = 2.0;
        double C,F,X, time = 0.0;
        freopen ("input.txt", "r", stdin);
        freopen ("output.txt", "w", stdout);
        scanf( "%d\n", &test );
        for(int i = 1; i <= test; i++){
            scanf("%lf", &C);
            scanf("%lf", &F);
            scanf("%lf", &X);
            if(C > X){
                time = X/rate;
            }
            else{
                int flag = 0;
                double break_rate = 0.0;
                while(X/rate > ((C/rate)+(X/(rate+F)))){
                    break_rate = X/(rate+F);
                    time += C/rate;
                    rate += F;
                    flag = 1;
                }
                if(!flag){
                    time = X/rate;
                }
                else{
                    time += break_rate;
                }
            }
            printf("Case #%d: %.7f\n",i, time);
            time = 0.0;
            rate = 2.0;
        }
        return 0;
    }
