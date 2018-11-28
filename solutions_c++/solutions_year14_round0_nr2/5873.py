#include<stdio.h>

int main(){
    int n;
    double c, f, x;
    int cas;

    scanf("%d", &n);
    for(cas = 1; cas <= n; cas++){
        scanf("%lf %lf %lf", &c, &f, &x);
        double ans = 0.0;
        double rate = 2.0;
        double t1, t2;
        while(true){
            t1 = ans + (c / rate) + x / (rate + f);
            t2 = ans + x / rate;
            if(t1 > t2){
                ans = t2;
                break;
            }
            else{
                ans = ans + c / rate;
                rate += f;
            }
        }

        printf("Case #%d: %.7lf\n", cas, ans);
    }
}
