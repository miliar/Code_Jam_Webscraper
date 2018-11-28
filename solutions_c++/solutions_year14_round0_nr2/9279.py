#include <cstdio>

#define eps 1e-5

#define nf (C / cps)
#define d (X / cps)

int main() {
    int T;
    scanf("%d", &T);
    for (int tz = 0; tz ++< T;) {
        int z;
        double C, F, X, t = 0;
        scanf("%lf%lf%lf", &C, &F, &X);
        double cps = 2;
        while (d > nf + X / (cps + F)) {
            t += nf;
            cps += F;
        }
        t += d;
        printf("Case #%d: %.7lf\n", tz, t);
    }
}
