#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define REP(i, n) for (int i = 0; i < (int)(n); ++i)
typedef long long LL;
typedef pair<int, int> PII;

int tt, test, mask;
int n;
char s[33][33];
int a[33][33], b[33][33];
int pc[1 << 16];

bool used[33] = {};
int ord[33];
bool can[1 << 4], ncan[1 << 4];

bool go(int pos) {
    if (pos == n) {
        memset(can, 0, sizeof can);
        can[0] = true;
        bool ok = true;
        REP(ii, n) {
            int i = ord[ii];
            memset(ncan, 0, sizeof ncan);
            REP(mask, 1 << n) if (can[mask]) {
                bool tr = false;
                REP(j, n) if (b[i][j] && !(mask & (1 << j))) {
                    tr = true;
                    ncan[mask | (1 << j)] = true;
                }
                if (!tr) {
                    ok = false;
                    break;
                }
            }
            if (!ok) break;
            memcpy(can, ncan, sizeof can);
        }
        return ok;
    }
    REP(i, n) if (!used[i]) {
        ord[pos] = i;
        used[i] = true;
        if (!go(pos + 1)) return false;
        used[i] = false;
    }
    return true;
}

int main() {
    REP(i, 1 << 16) pc[i] = __builtin_popcount(i);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &tt);
    for (test = 1; test <= tt; ++test) {
        printf("Case #%d: ", test);
        scanf("%d", &n);
        REP(i, n) scanf("%s", s[i]);
        REP(i, n) REP(j, n) a[i][j] = s[i][j] - '0';
        int nn = n * n;
        int ans = 1234;
        for (mask = 0; mask < (1 << nn); ++mask) {
            if (pc[mask] >= ans) continue;
            bool ok = true;
            REP(i, n) REP(j, n) {
                b[i][j] = a[i][j] + ((mask & (1 << (i * n + j))) != 0);
                if (b[i][j] == 2) ok = false;
            }
            if (!ok) continue;
            memset(used, 0, sizeof used);
            if (go(0)) {
                ans = min(ans, pc[mask]);
            }
        }
        printf("%d\n", ans);
    }
    return 0;
}
