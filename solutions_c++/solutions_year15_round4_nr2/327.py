#include <cstdio>
#include <cstring>
#include <cmath>
#include <iomanip>
using namespace std;

namespace {
#define eps 1e-8

int cmp(double a, double b) {
    double dt = a - b;
    if(fabs(dt) < eps)
        return 0;
    if(a < b)
        return -1;
    return 1;
}

int n;
double v, x;
double r[100], c[100];

void init() {
    scanf("%d%lf%lf", &n, &v, &x);

    for(int i = 0;i < n;i ++)
        scanf("%lf %lf", r + i, c + i);
}

void work(int iCase) {
    if(n == 1) {
        if(cmp(c[0], x)) {
            printf("Case #%d: IMPOSSIBLE\n", iCase + 1);
        } else {
            printf("Case #%d: %.10lf\n", iCase + 1, v / r[0]);
        }
    } else if(n == 2) {
        if(cmp(c[0], x) == 0 && cmp(c[1], x)) {
            printf("Case #%d: %.10lf\n", iCase + 1, v / r[0]);
        } else if(cmp(c[1], x) == 0 && cmp(c[0], x)) {
            printf("Case #%d: %.10lf\n", iCase + 1, v / r[1]);
        } else if(cmp(c[1], x) == 0 && cmp(c[0], x) == 0) {
            printf("Case #%d: %.10lf\n", iCase + 1, v / (r[0] + r[1]));
        } else if(cmp(c[0], x) != cmp(c[1], x)) {
            double t0 = v * (c[1] - x) / (r[0] * (c[1] - c[0]));
            double t1 = v * (c[0] - x) / (r[1] * (c[0] - c[1]));

            printf("Case #%d: %.10lf\n", iCase + 1, max(t0, t1));
        } else {
            printf("Case #%d: IMPOSSIBLE\n", iCase + 1);
        }
    } else {
        printf("Case #%d: IMPOSSIBLE\n", iCase + 1);
    }
}

void _main() {
    int T;
    scanf("%d", &T);
    for(int iCase = 0;iCase < T;iCase ++) {
        init();
        work(iCase);
    }

    return ;
}

} // namespace

// main
int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    ::_main();
    return 0;
}
