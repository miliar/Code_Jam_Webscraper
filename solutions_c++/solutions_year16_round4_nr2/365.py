#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define REP(i, n) for (int i = 0; i < (int)(n); ++i)
typedef long long LL;
typedef pair<int, int> PII;

int tt;
int n, k;
double p[255];
double d[255];

void apply(int i) {
    for (int j = k; j > 0; --j) {
        d[j] += d[j - 1] * p[i];
        d[j - 1] *= 1 - p[i];
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &tt);
    for (int test = 1; test <= tt; ++test) {
        printf("Case #%d: ", test);
        scanf("%d%d", &n, &k);
        REP(i, n) scanf("%lf", p + i);
        sort(p, p + n);
        double mx = 0;
        REP(le, k + 1) {
            memset(d, 0, sizeof d);
            d[0] = 1;
            for (int i = 0; i < le; ++i) {
                apply(i);
            }
            for (int i = 0; i < k - le; ++i) {
                apply(n - 1 - i);
            }
            mx = max(mx, d[k / 2]);
        }
        printf("%.12f\n", mx);
    }
    return 0;
}
