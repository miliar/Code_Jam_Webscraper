#include <cstdio>

using namespace std;

int t, n;
double v, x, r[104], c[104];

double max(double a, double b) {
    if (a>b) return a;
    else return b;
}

int main() {
    freopen("B-small-B.in","r",stdin);
    freopen("B-out.out","w",stdout);
    scanf("%d",&t);
    for (int tp=1; tp<=t; tp++) {
        scanf("%d",&n);
        scanf("%lf%lf", &v, &x);
        for (int i=1; i<=n; i++) scanf("%lf%lf",&r[i], &c[i]);
        printf("Case #%d: ", tp);
        if (n == 1) {
            if (x != c[1]) printf("IMPOSSIBLE\n");
            else printf("%.8lf\n", v / r[1]);
        }
        else  {
            if (c[1] == c[2]) {
                if (c[1] != x) printf("IMPOSSIBLE\n");
                else printf("%.8lf\n", v / (r[1] + r[2]));
            }
            else {
                double v1 = v * (x - c[2]) / (c[1] - c[2]);
                double v2 = v - v1;
                if (v1 <-0.000001 || v2 <-0.000001) printf("IMPOSSIBLE\n");
                else printf("%.8lf\n", max(v1 / r[1], v2 / r[2]));
            }
        }
    }

    return 0;
}
