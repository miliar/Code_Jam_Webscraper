#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i = 0; i < (int)(n); i++)
typedef long long ll;
typedef pair <int, int> PII;
const int N = 1005;
const int INF = 1e9;
int n;
int a[N], idx[N];
int f[N][N];

bool cmp(int i, int j) {
    return a[i] < a[j];
}

int main() {
    //freopen("in", "r", stdin);
    int Tc;
    scanf("%d", &Tc);
    rep (ri, Tc) {
        printf("Case #%d: ", ri + 1);
        scanf("%d", &n);
        rep (i, n) scanf("%d", &a[i]);
        rep (i, n) idx[i] = i;
        rep (i, N) rep (j, N) f[i][j] = INF;
        sort(idx, idx + n, cmp);
        f[0][0] = 0;
        int ans = INF;
        rep (i, n + 1) {
            for (int j = 0; i + j <= n; j++) {
                if (i + j == 0) continue;
                int c = i + j - 1;
                int lc = 0, rc = 0;
                for (int k = idx[c]; k >= 0; k--) lc += a[k] > a[idx[c]];
                for (int k = idx[c]; k < n; k++) rc += a[k] > a[idx[c]];
                if (i) {
                    f[i][j] = min(f[i][j], f[i - 1][j] + lc);
                }
                if (j) {
                    f[i][j] = min(f[i][j], f[i][j - 1] + rc);
                }
                if (i + j == n) {
                    ans = min(ans, f[i][j]);
                }
                //printf("f[%d][%d] = %d\n", i, j, f[i][j]);
            }
        }
        printf("%d\n", ans);
    }
}

