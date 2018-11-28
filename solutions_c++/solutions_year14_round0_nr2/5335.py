#include <stdio.h>

int main () {
    int tt;
    double C,F,X;
    scanf("%d",&tt);
    double rate;
    double time;
    for (int t = 1; t <= tt; t++) {
        scanf("%lf%lf%lf",&C,&F,&X);
        rate = 2;
        time = 0;
        while (true) {
            if (X / rate >= X / (rate + F) + C / rate) {
                time += C / rate;
                rate += F;
            } else {
                time += X / rate;
                break;
            }
        }
        printf("Case #%d: %.7lf\n",t,time);
    }
    return 0;
}
