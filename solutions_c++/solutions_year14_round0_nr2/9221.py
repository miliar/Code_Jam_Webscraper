#include <stdio.h>
#include <algorithm>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int T;
    scanf("%d", &T);
    rep (_q, T) {
        double C, F, X;
        scanf("%lf%lf%lf", &C, &F, &X);
        double ans = X / 2;
        double t = 0, r = 2;
        while (t < ans) {
            t += C / r;
            r += F;
            ans = min(ans, t + X / r);
        }
        printf("Case #%d: %.7f\n", _q+1, ans);
    }
    return 0;
}
