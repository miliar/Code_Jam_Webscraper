#include "stdio.h"

int main() {
    int t;
    scanf("%i",&t);
    for (int ti=1; ti <= t; ti++) {
        double   cookiesPerSecond = 2.0, cookies=0.0, time=0.0,
                farmCost, bonusCPS, goal;
        scanf("%lf %lf %lf", &farmCost, &bonusCPS, &goal);
        if (farmCost >= goal)
            time = goal/cookiesPerSecond;
        else
            while (cookies < goal) {
                if (cookies < farmCost) {
                    time += (farmCost-cookies)/cookiesPerSecond;
                    cookies = farmCost;
                } else {
                    double   noBuyTime = (goal - cookies) / cookiesPerSecond,
                            buyTime = (goal - cookies + farmCost) / (cookiesPerSecond + bonusCPS);
                    if (buyTime <= noBuyTime) {
                        cookiesPerSecond += bonusCPS;
                        cookies -= farmCost;
                    } else {
                        time += noBuyTime;
                        cookies = goal;
                    }
                }
            }
        printf("Case #%i: %.7f\n", ti, time);
    }
    return 0;
}
