#include <cstdio>

int main() {
    int t;
    double c, f, x;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
    {
        scanf("%lf %lf %lf", &c, &f, &x);
        double best = x/2.0;
        double time = 0;
        for (int j = 0; j < 15000000; ++j) {
            if (time + x/(2.0 + j*f) < best) best = time + x/(2.0 + j*f);
            time += c/(2.0 + j*f);
        }
        printf("Case #%d: %.7f\n", i+1, best);
    }
}