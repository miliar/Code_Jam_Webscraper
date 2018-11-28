#include <cstdio>
#include <algorithm>
using namespace std;

double r[100];
double c[100];

double solve(int n, double v, double x) {
    if(n == 1) {
        if(c[0] != x)
            return -1;
        return v / r[0];
    } else if(n == 2) {
        if(c[0] == c[1]) {
            if(x == c[0]) {
                return v / (r[0] + r[1]);
            } else {
                return -1;
            }
        } else if((c[0] < x && c[1] < x) || (c[0] > x && c[1] > x)) {
            return -1;
        } else {
            double y = x * v;
            double r1 = r[0], r2 = r[1];
            double c1 = r[0] * c[0], c2 = r[1] * c[1];

            double t1 = (v * c2 - r2 * y) / (r1 * c2 - r2 * c1);
            double t2 = (r1 * y - v * c1) / (r1 * c2 - r2 * c1);

            return max(t1, t2);
        }
    }
    return -1;
}

int main() {
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++) {
        int n;
        double v, x;
        scanf("%d %lf %lf", &n, &v, &x);
        for(int j = 0; j < n; j++)
            scanf("%lf %lf", r + j, c + j);
        double ans = solve(n, v, x);
        if(ans >= 0)
            printf("Case #%d: %.10f\n", i, ans);
        else
            printf("Case #%d: IMPOSSIBLE\n", i);
    }
}
