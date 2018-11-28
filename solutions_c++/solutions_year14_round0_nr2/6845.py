#include <stdio.h>

int main()
{
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; ++i) {
        double C, F, X;
        scanf("%lf %lf %lf", &C, &F, &X);
        double seconds = 0.0;
        double rate = 2.0;
        while ((C / rate + X / (rate + F)) < (X / rate)) {
            seconds += C / rate;
            rate += F;
        }
        seconds += X / rate;
        printf("Case #%d: %.7f\n", i + 1, seconds);
    }
    return 0;
}
