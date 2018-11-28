#include <cstdio>
#include <cmath>

#define EPS 1e-7

int TC;
double C, F, X, total_time, rate;

int main() {
    scanf("%d", &TC);
    for (int tc = 1; tc <= TC; tc++) {
        scanf("%lf %lf %lf", &C, &F, &X);
        total_time = 0.0;
        rate = 2.0;
        if (C <= X - EPS) {
            int k = (int)ceil((F * (X - C) - 2.0 * C) / (F * C));
            for (int i = 0; i < k; i++) {
                total_time += C / rate;
                rate += F;
            }
        }
        total_time += X / rate;
        printf("Case #%d: %lf\n", tc, total_time);
    }
}