#include <stdio.h>
#include <stdlib.h>
int main(void){
    int T, t;
    scanf("%d", &t);
    for(T = 1; T <= t; T++){
        double C, F, X, time = 0, m = 2, sum = 0;
        scanf("%lf %lf %lf", &C, &F, &X);
        //printf("%lf %lf %lf\n", C, F, X);
        while(1){
            double t1, t2, t;
            t1 = C / m;
            t2 = X / m;
            t = C / F;
            if(t1 + t < t2){
                time += t1;
                m += F;
            }
            else{
                time += t2;
                break;
            }
        }
        printf("Case #%d: %.7lf\n", T, time);
    }
    return 0;
}
