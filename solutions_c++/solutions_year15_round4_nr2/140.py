#include <stdio.h>
#include <algorithm>
using namespace std;
int n;
struct abc{
    double r, c;
    bool operator < (const abc &a) const {
        return c > a.c;
    }
}c[110];
double v, x;
bool pd(double t) {
    int i;
    double tott = 0, totv = 0, vv;
    for (i = 0; i < n; i++) {
        vv = min(v - totv, c[i].r * t);
        totv += vv;
        tott += vv * c[i].c;
    }
    tott /= totv;
    if (totv < v - 1e-12 || tott < x - 1e-12) return false;
    tott = 0, totv = 0;
    for (i = n - 1; i >= 0; i--) {
        vv = min(v - totv, c[i].r * t);
        totv += vv;
        tott += vv * c[i].c;
    }
    tott /= totv;
    if (totv < v - 1e-12 || tott > x + 1e-12) return false;
    return true;
}
int main() {
    int T, ri = 1, i;
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--) {
        scanf("%d%lf%lf", &n, &v, &x);
        v *= 100000;
        for (i = 0; i < n; i++) {
            scanf("%lf%lf", &c[i].r, &c[i].c);
            c[i].r *= 100000;
        }
        sort(c, c + n);
        double l = 0, r = 1e9, z;
        for (i = 0; i < 500; i++) {
            z = (l + r) * 0.5;
            if (pd(z)) r = z;
            else l = z;
        }
        pd(r);
        printf("Case #%d: ", ri++);
        if (r > 1e8) printf("IMPOSSIBLE\n");
        else printf("%.10f\n", r);
    }
    return 0;
}
