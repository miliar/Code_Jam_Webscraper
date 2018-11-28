#include <cstdio>

int main(int argc, char const *argv[])
{
    int T;
    double C, F, X;
    scanf("%d", &T);
    for(int cases = 1; cases <= T; cases++) {
        scanf("%lf %lf %lf", &C, &F, &X);
        double rate = 2;
        double seconds = 0;
        int strikes = 0;
        while(seconds+(C/rate)+(X/(rate+F)) < seconds+(X/rate)) {
            seconds += (C/rate);
            rate += F;
        }
        seconds += X/rate;
        printf("Case #%d: %.7f\n", cases, seconds);
    }
    return 0;
}