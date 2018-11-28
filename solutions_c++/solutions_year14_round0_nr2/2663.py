#include <stdio.h>

int main(void)
{
    int tn, n;
    double c, f, x, total, rate, buytime, waittime;
    scanf("%d", &tn);
    for(n=1;n<=tn;n++){
        printf("Case #%d: ",n);
        scanf("%lf%lf%lf",&c, &f, &x);
        total=0;
        rate=2.0;
        buytime=(c/rate)+x/(rate+f);
        waittime=x/rate;
        while(buytime<waittime){
            total+=(c/rate);
            rate=rate+f;
            buytime=(c/rate)+x/(rate+f);
            waittime=x/rate;
        }
        printf("%.7lf\n", total+waittime);
    }

    return 0;
}
