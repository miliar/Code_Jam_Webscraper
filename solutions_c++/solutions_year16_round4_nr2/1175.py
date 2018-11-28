#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int vec[1111];
double p[1111];
int n, k;

void work() {
    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; i++) scanf("%lf", &p[i]);
    double ans = 0;
    for (int i = 0; i < 1<<n; i++) {
        int c = 0;
        for (int j = 0; j < n; j++) {
            if (i >> j & 1) {
                vec[c++] = j;
            }
        }
        if (c != k) 
            continue;
        double sum = 0;
        for (int j = 0; j < 1<<k; j++) {
            int cnt = 0;
            int tot = 0;
            for (int a = 0; a < k; a++) {
                if (j >> a & 1) {
                    ++ tot;
                }
            }
            if (tot * 2 != k)
                continue;
            double P = 1.0;
            for (int a = 0; a < k; a++) {
                if (j >> a & 1) {
                    P *= p[vec[a]];
                } else {
                    P *= (1.0 - p[vec[a]]);
                }
            }
            sum += P;
        }
        ans = max(sum, ans);
    }
    printf("%.10f\n", ans);
    return ;
}

int main() {
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt1.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        printf("Case #%d: ", cas);
        work();
    }
    return 0;
}
