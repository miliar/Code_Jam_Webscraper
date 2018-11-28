#include<cstdio>
#include<cstdlib>
#include<algorithm>
using namespace std;

int T;
double C, F, X;

int main() {
    scanf("%d", &T);
    for (int t=1; t<=T; t++) {
        scanf("%lf%lf%lf", &C,&F,&X);
        double rate = 2.0;
        double accum = 0;
        while (1) {
            // at current rate
            double best = X/rate;

            // get a farm
            double local = C/rate;
            double localrate = rate + F;
            double localbest = local + X/localrate;
            // printf("local = %lf, localrate = %lf, localbest = %lf\n", local, localrate, localbest);
            if (localbest - best < 1e-8) {
                rate = localrate;
                accum += local;
            } else {
                accum += best;
                break;
            }
        }
        printf("Case #%d: %.7lf\n", t, accum);
    }
    return 0;
}
