#include <cstdio>
#include <algorithm>
using namespace std;

#define MAX 105

#define mp make_pair
#define fi first
#define se second

typedef pair<double, double> pdd;

int n;
double vol, temp;
pdd src[MAX];

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d %lf %lf", &n, &vol, &temp);
        for (int i = 0; i < n; i++)
            scanf("%lf %lf", &src[i].se, &src[i].fi);
        printf("Case #%d: ", t);
        sort(src, src+n);
        if (src[n-1].fi < temp) {
            puts("IMPOSSIBLE");
            continue;
        }
        if (src[0].fi > temp) {
            puts("IMPOSSIBLE");
            continue;
        }
        if (src[0].fi == src[1].fi) {
            src[0].se += src[1].se;
            n--;
        }
        int done = 0;
        for (int i = n-1; i >= 0; i--) {
            if (src[i].fi == temp) {
                printf("%.6lf\n", vol / src[i].se);
                done = 1;
                break;
            }
        }
        if (done) continue;
        if (n == 1) {
            puts("IMPOSSIBLE");
            continue;
        }
        double v1 = vol * (temp - src[0].fi) / (src[1].fi - src[0].fi);
        double v0 = vol - v1;
        double ans = max(v0 / src[0].se, v1 / src[1].se);
        printf("%.6lf\n", ans);
    }
}
