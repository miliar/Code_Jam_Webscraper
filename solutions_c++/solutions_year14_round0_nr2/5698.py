#include <cstdio>

int main()
{
    int T, kase = 1;
    scanf("%d", &T);

    while (T--) {
        double c, f, x, rate = 2, t = 0;
        scanf("%lf%lf%lf", &c, &f, &x);
        while (true) {
            double t1 = x / rate;
            double t2 = c / rate;
            if (t1 <= t2) {
                t += t1;
                break;
            }
            double t3 = x / (rate + f);
            if (t1 <= (t2+t3)) {
                t += t1;
                break;
            } else {
                t += t2;
                rate += f;
            }
        }
        printf("Case #%d: %.7f\n", kase++, t);
    }
}

