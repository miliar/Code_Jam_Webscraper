#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <sstream>

#define REP(i,n) for(int i=0;i<(n);i++)
#define REPD(i,n) for(int i=n-1;i>=0;i--)
#define FOR(i,n) for(int i=1;i<=(n);i++)
#define FORD(i,n) for(int i=(n);i>=1;i--)

#define SZ(x) ((int)x.size())
#define CC(a,x) memset(a,x,sizeof(a))
#define TWO(x) ((LL)1<<(x))

using namespace std;

int T;
int n;
double v, x;
struct src {
    double r, c;
}s[111];

void solve() {
    scanf("%d", &n);
    scanf("%lf%lf", &v, &x);
    REP(i, n) {
        scanf("%lf%lf", &s[i].r, &s[i].c);
        REP(j, i) {
            if (abs(s[j].c - s[i].c) < 1e-9) {
                s[j].r += s[i].r;
                i--;
                n--;
                break;
            }
        }
    }
    double ans = -1;
    if (n > 1) {
        REP(o, n) {
            double r0 = 0, x0 = 0, r1 = 0, x1 = 0;
            REP(i, n) {
                if (i == o) r0 = s[i].r, x0 = s[i].c;
                else {
                    x1 = (x1*r1 + s[i].r*s[i].c) / (r1 + s[i].r);
                    r1 += s[i].r;
                }
            }
            if ((x1 > x && x0 > x) || (x1 < x && x0 < x)) {
                continue;
            }
            double t0 = abs(x1 - x) / (abs(x1 - x) + abs(x0 - x)) * v / r0;
            double t1 = abs(x0 - x) / (abs(x1 - x) + abs(x0 - x)) * v / r1;
            if (ans < 0) ans = max(t0, t1);
            else ans = min(ans, max(t0, t1));
        }
        if (ans < 0) printf("IMPOSSIBLE");
        else printf("%.9lf", ans);
    } else {
        if (abs(s[0].c - x) < 1e-9) printf("%.9lf", v / s[0].r);
        else printf("IMPOSSIBLE");
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    scanf("%d", &T);
    for (int i=1; i<=T; i++) {
        printf("Case #%d: ", i);
        solve();
        printf("\n");
    }
    return 0;
}
