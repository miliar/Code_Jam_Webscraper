#include <cstdio>
#include <cstdlib>

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        double C,F,X;
        scanf("%lf %lf %lf", &C, &F, &X);
        double time = 0;
        double cps = 2;
        while(X/cps > X/(cps+F) + C/cps) {
            time += C/cps;
            cps += F;
        }
        printf("Case #%d: %.7lf\n", i+1, time + X/cps);
    }
    return 0;
}
