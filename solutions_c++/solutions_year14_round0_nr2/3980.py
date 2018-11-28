#include <cstdio>
#define EPS 0.000000001
using namespace std;

float min(float a, float b);

int main() {
    int t = 0;
    double C = 2.0, F = 0.0, X = 0.0, cps = 0.0;
    double time = 0.0, min_time = 0.0;
    scanf("%d", &t);
    for (int ggg = 1; ggg <= t; ggg++) {
        cps = 2.0;
        time = 0.0;
        scanf("%lf %lf %lf", &C, &F, &X);
        min_time = (X) / cps;
        while (true) {
            time += (C) / (cps);
            cps += F;
            if (time + (X) / (cps) < min_time) {
                min_time = time + (X) / (cps);
            }
            else {
                break;
            }
        }
        printf("Case #%d: %.7lf\n", ggg, min_time);
    }
    return 0;
}
