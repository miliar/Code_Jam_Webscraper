#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
using namespace std;
string s[15];
int pre[15][15];
int a[15];
int len[15];
int n, m;
int ans = 0, ansed;

inline int check() {
    int ans = n;
    for (int i = 0; i < m; ++i) {
        int tmp = 0;
        for (int j = 0; j < i; ++j) {
            if (a[j] != a[i]) continue;
            tmp = max(tmp, pre[i][j]);
        }
        ans += len[i] - tmp;
    }
    return ans;
}

int cnt;
int ok[5];
void dfs(int k) {
    if (k == m) {
        memset(ok, 0 ,sizeof(ok));
        for (int i = 0; i < m; ++i) ok[a[i]] = 1;
        for (int i = 0; i < n; ++i) if (!ok[i]) return;
        int tmp = check();
        if (!ansed)
            ans = max(ans, tmp);
        else {
            if (tmp == ans) cnt++;
        }
        return;
    }
    for (int i = 0; i < n; ++i) {
        a[k] = i;
        dfs(k + 1);
    }
}


int main() {
    freopen("DS.in", "r", stdin);
    freopen("DS.out", "w", stdout);
    int T, ca = 0;
    cin >> T;
    while (T--) {
       // scanf("%d %d\n", &m, &n);
       cin >> m >> n;
        for (int i = 0; i < m; ++i) cin >> s[i];
        for (int i = 0; i < m; ++i) len[i] = s[i].length();
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < m; ++j) {
                int tmp = 0;
                for (int k = 0; k < min(len[i], len[j]); ++k) {
                    if (s[i][k] == s[j][k]) tmp++; else break;
                }
                pre[i][j] = tmp;
            }
        }
        cnt = 0;
        ans = 0;
        ansed = 0;
        dfs(0);
        ansed = 1;
        dfs(0);
        printf("Case #%d: ", ++ca);
        cout << ans << ' ' << cnt << endl;
    }
    return 0;
}
