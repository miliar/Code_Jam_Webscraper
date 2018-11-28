#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

int T;
int n;
long double v, m, r;
long double vi[128];
long double ri[128];
int id[128];

bool cmp(int x, int y) {
    return ri[x] < ri[y];
}

int main() {
    freopen("bl.in", "r", stdin);
    freopen("bl.out", "w", stdout);
    scanf("%d", &T);
    for (int test = 1; test <= T; test++) {
        printf("Case #%d: ", test);
        scanf("%d%Lf%Lf", &n, &v, &r);
        m = r * v;
        bool hl = false, hh = false;
        for (int i = 1; i <= n; i++) {
            scanf("%Lf%Lf", vi + i, ri + i);
            id[i] = i;
            if (ri[i] <= r)
                hl = true;
            if (ri[i] >= r)
                hh = true;
        }
        sort(id + 1, id + 1 + n, cmp);
        long double l = 0, r = 1e10, mid;
        for (int tn = 0; tn < 400; tn++) {
            mid = (l + r) / 2;
            long double vl = 0, ml = 0;
            for (int ii = 1; ii <= n; ii++) {
                int i = id[ii];
                long double t = min(mid * vi[i], v - vl);
                vl += t;
                ml += t * ri[i];
            }
            long double vh = 0, mh = 0;
            for (int ii = n; ii > 0; ii--) {
                int i = id[ii];
                long double t = min(mid * vi[i], v - vh);
                vh += t;
                mh += t * ri[i];
            }
            if (mh < m / (1 + 1e-12) || ml / (1 + 1e-12) > m)
                l = mid;
            else
                r = mid;
        }
        if (hl && hh)
            printf("%.12Lf\n", l);
        else
            printf("IMPOSSIBLE\n");
    }
    return 0;
}