#include <cstdio>
double C, F, X;
double rate;
double sumTime;
int main()
{
    freopen("B-large.in", "rt", stdin);
    freopen("Bout.txt", "wt", stdout);

    int T, Case = 1;
    scanf("%d", &T);
    while (T--) {
        scanf("%lf %lf %lf", &C, &F, &X);
        rate = 2;
        sumTime = 0;

        while (X/rate > (C/rate + (X/(rate+F)))) {
            sumTime += C/rate;
            rate += F;
        }
        sumTime += X/rate;
        printf("Case #%d: %.7f\n", Case++, sumTime);
    }
}
