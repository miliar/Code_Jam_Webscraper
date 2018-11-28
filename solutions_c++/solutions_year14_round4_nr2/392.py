#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

const int maxn = 1000 + 5;
int a[maxn], b[maxn];
int dyn[maxn][maxn];

void solve(int testNum)
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        scanf("%d", &a[i]);
        b[i] = a[i];
    }
    sort(b, b + n);
    for (int i = 0; i <= n; ++i) {
        for (int j = 0; j <= n; ++j) {
            dyn[i][j] = 1 << 30;
        }
    }
    dyn[0][0] = 0;
    for (int cnt = 0; cnt < n; ++cnt) {
        int curEl = b[cnt];
        int lcnt = 0;
        for (int i = 0; i < n; ++i) {
            if (a[i] > curEl) {
                ++lcnt;
            }
            else if (a[i] == curEl) {
                break;
            }
        }
        int rcnt = n - 1 - cnt - lcnt;
        for (int l = 0; l <= cnt; ++l) {
            int r = cnt - l;
            dyn[l + 1][r] = min(dyn[l + 1][r], dyn[l][r] + lcnt);
            dyn[l][r + 1] = min(dyn[l][r + 1], dyn[l][r] + rcnt);
        }
    }
    int res = 1 << 30;
    for (int l = 0; l <= n; ++l) {
        res = min(res, dyn[l][n - l]); 
    }

    printf("Case #%d: %d\n", testNum, res);
}

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        solve(i + 1);
    }
    return 0;
}
