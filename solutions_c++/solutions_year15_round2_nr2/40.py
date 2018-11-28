#include <iostream>
#include <sstream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cstring>
#include <cmath>
#include <bitset>
#include <cstdlib>
#include <memory>
#include <ctime>

#define FILE

using namespace std;

int n, m, k;
int ans;
bool f[10002][10002];

inline void check(int x, int y) {
    if (k <= 0 || f[x][y] == true)
        return;
    f[x][y] = true;
    k--;
}

void solve() {
    cin >> n >> m >> k;
    int k2 = k;
    for (int i = 0; i < n + 1; i++)
        for (int j = 0; j < m + 1; j++)
            f[i][j] = false;
    for (int i = n - 1; i >= 0; i--) {
        for (int j = m - 1; j >= 0; j--) {
            if (i == n - 1 && j == m - 1)
                continue;
            if (f[i + 1][j] == false && f[i][j + 1] == false) {
                f[i][j] = true;
                k--;
            }
        }
    }
    ans = 0;
    check(0, m - 1);
    check(n - 1, m - 1);
    check(0, 0);
    check(n - 1, 0);

    for (int i = 0; i < n; i++) {
        check(i, 0);
        check(i, m - 1);
    }
    for (int i = 0; i < m; i++) {
        check(0, i);
        check(n - 1, i);
    }
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            check(i, j);

    for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++) {
            if (f[i][j] && f[i + 1][j])
                ans++;
            if (f[i][j] && f[i][j + 1])
                ans++;
    }

    k = k2;


    for (int i = 0; i < n + 1; i++)
        for (int j = 0; j < m + 1; j++)
            f[i][j] = false;
    for (int i = n - 1; i >= 0; i--) {
        for (int j = m - 1; j >= 0; j--) {
            if (f[i + 1][j] == false && f[i][j + 1] == false) {
                f[i][j] = true;
                k--;
            }
        }
    }
    int ans2 = ans;
    ans = 0;
    check(0, m - 1);
    check(n - 1, m - 1);
    check(0, 0);
    check(n - 1, 0);

    for (int i = 0; i < n; i++) {
        check(i, 0);
        check(i, m - 1);
    }
    for (int i = 0; i < m; i++) {
        check(0, i);
        check(n - 1, i);
    }
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            check(i, j);

    for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++) {
            if (f[i][j] && f[i + 1][j])
                ans++;
            if (f[i][j] && f[i][j + 1])
                ans++;
    }
    cout << min(ans, ans2) << endl;
}

int main() {
#ifdef FILE
    freopen("E:/1.in", "r", stdin);
    freopen("E:/1.out", "w", stdout);
#endif // FILE

    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
