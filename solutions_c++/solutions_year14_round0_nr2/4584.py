#include <stdio.h>

int main()
{
    int t, i,k;
    double c, f, x, rate, time;
    scanf("%d", &t);
    k = 1;
    for (i = 0; i < t; i++) {

        scanf("%lf%lf%lf", &c, &f, &x);
        rate = 2.0;
        time = 0.0;
        while ((x/rate) > (c/rate) + (x/(rate+f))) {
            time = time + (c/rate);
            rate = rate + f;
        }
        time =  time + (x/rate);
        printf("Case #%d: %0.7lf\n",k, time);
        k++;
    }
    return 0;
}
