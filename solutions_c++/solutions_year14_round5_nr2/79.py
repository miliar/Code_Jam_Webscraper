#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i = 0; i < (int)(n); i++)
typedef long long ll;
typedef pair <int, int> PII;
const int N = 105;
const int INF = 1e9;
int Tc, P, Q, n;
int h[N], g[N];
int win[N];
int f[N][20005];

void cm(int &x, int t) {
    if (t > x) x = t;
}

int main() {
    cin >> Tc;
    rep (ri, Tc) {
        printf("Case #%d: ", ri + 1);
        cin >> P >> Q >> n;
        rep (i, n) cin >> h[i] >> g[i];
        rep (i, n) {
            win[i] = -INF;
            for (int j = 0; j * Q < h[i]; j++) {
                int k = 0;
                while (j * Q + k * P < h[i]) k++;
                win[i] = max(win[i], j - k);
            }
            //cout << win[i] << endl;
        }
        memset(f, 0xff, sizeof(f));
        f[0][1] = 0;
        int ans = 0;
        rep (i, n + 1) {
            rep (j, 20001) {
                if (i < n && f[i][j] != -1) {
                    cm(f[i + 1][j + (h[i] + Q - 1) / Q], f[i][j]);
                    if (j + win[i] >= 0) {
                        cm(f[i + 1][j + win[i]], f[i][j] + g[i]);
                    }
                }
                ans = max(ans, f[i][j]);
            }
        }
        cout << ans << endl;
    }
}

