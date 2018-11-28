#include <algorithm>
#include <cstdio>
#include <cstdlib>
using namespace std;

int main(int argc, char *argv[]) {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        double C, F, X;
        scanf("%lf%lf%lf", &C, &F, &X);
        double cps=2., best=X/2., tim=C/2.;
        while (tim < best) {
            cps += F;
            best = min(best, tim + X/cps);
            tim += C/cps;
        }
        printf("Case #%d: %.16lf\n", t, best);
        //fprintf(stderr, "Case #%d: %.16lf\n", t, best);
    }
    return EXIT_SUCCESS;
}
