#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

const int maxn = 1024;

int f[maxn][maxn];
int a[maxn];
int id[maxn];
int cnt[maxn][2];

bool cmp(int x, int y) {
    return a[x] < a[y];
}

void update(int &a, int b) {
    a = min(a, b);
}

void solve() {
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        id[i] = i;
    }
    sort(id, id + n, cmp);
    for (int i = 0; i < n; ++i) {
        cnt[i][0] = cnt[i][1] = 0;
        for (int j = i + 1; j < n; ++j) {
            if (id[j] < id[i]) {
                cnt[i][1]++;
            }
            if (id[j] > id[i]) {
                cnt[i][0]++;
            }
        }
    }
    for (int i = 0; i <= n; ++i) {
        for (int j = 0; i + j <= n; ++j) {
            f[i][j] = 1 << 30;
        }
    }
    f[0][0] = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; i + j < n; ++j) {
            if (f[i][j] == (1 << 30)) {
                continue;
            }
            update(f[i][j + 1], f[i][j] + cnt[i + j][0]);
            update(f[i + 1][j], f[i][j] + cnt[i + j][1]);
        }
    }
    int ans = 1 << 30;
    for (int i = 0; i <= n; ++i) {
        update(ans, f[i][n - i]);
    }
    printf("%d\n", ans);
}

int main() {
    int T;
    cin >> T;
    for (int caseId = 1; caseId <= T; ++caseId) {
        printf("Case #%d: ", caseId);
        solve();
    }
}
