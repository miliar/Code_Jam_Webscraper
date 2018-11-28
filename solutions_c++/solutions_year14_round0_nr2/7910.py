#include <cstdio>
#include <cstdlib>

int main(int argc, char *argv[])
{
    int T;
    scanf("%d", &T);
    for (int ct = 1; ct <= T; ct++) {
        printf("Case #%d: ", ct);
        double fact = 0.0;
        double currentTime = 0.0, nextTime = 0.0, time = 0.0;
        double rate = 2.0;
        double C, F, X;
        scanf("%lf%lf%lf", &C, &F, &X);
        while(true) {
            double currentRate = (rate + fact*F);
            double nextRate = (rate + (fact+1)*F);
            currentTime = X/currentRate;
            nextTime = C/currentRate + X/nextRate;
            if (currentTime <= nextTime) {
                time = currentTime + time;
                break;
            } else {
                time = C/currentRate + time;
                fact++;
            }
        }
        printf("%.7lf\n", time);
    }
    return 0;
}
