
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    for (int no = 0; no < T; no ++) {
        printf("Case #%d: ", no + 1);
        double C, F, X;
        scanf("%lf%lf%lf", &C, &F, &X);
        double ans = 1e100;
        double r = 2;
        double t = 0;
        while (true) {
            double tt = C / r;
            ans = min(ans, t + X / r);
            t += tt;
            r += F;
            if (t > ans) break;
        }
        printf("%.10lf\n", ans);
    }
    return 0;
}