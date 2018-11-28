#include <cstdio>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;

const int MAXN = 7;

bool can[MAXN * MAXN + 1][MAXN * MAXN + 1][1 << MAXN];
int dp[MAXN * MAXN + 1][MAXN * MAXN + 1][1 << MAXN];
int from[MAXN * MAXN + 1][MAXN * MAXN + 1][1 << MAXN];

int intersect[1 << MAXN][1 << MAXN];
int weight[1 << MAXN];

void precalc() {
    for (int mask = 0; mask < (1 << MAXN); mask++) {
        for (int i = 0; i < MAXN; i++) {
            if (mask & (1 << i)) {
                weight[mask]++;
            }
        }
        for (int newmask = 0; newmask < (1 << MAXN); newmask++) {
            for (int i = 0; i < MAXN; i++) {
                if ((newmask & (1 << i)) && (newmask & (1 << (i + 1)))) {
                    intersect[mask][newmask]++;
                }
                if ((mask & (1 << i)) && (newmask & (1 << i))) {
                    intersect[mask][newmask]++;
                }
            }
        }
    }
}

int a[100][10000];
int b[100][10000];

int neighbours(int i, int j, int r, int c) {
    int cnt = 0;
    for (int dx = -1; dx <= 1; dx++) {
        for (int dy = -1; dy <= 1; dy++) {
            if (abs(dx) + abs(dy) != 1) {
                continue;
            }
            int ni = i + dx, nj = j + dy;
            if (ni < 0 || ni >= r || nj < 0 || nj >= c) {
                continue;
            }
            if (a[ni][nj] == 1) {
                cnt++;
            }
        }
    }
    return cnt;
}

void put(int i, int j, int r, int c, int &n, int &ans) {
    if (n > 0 && a[i][j] == 0) {
        a[i][j] = 1;
        ans += neighbours(i, j, r, c);
        n--;
    }
}

void put(int r, int c, int n, int &ans) {
    put(0, 0, r, c, n, ans);
    put(0, c - 1, r, c, n, ans);
    put(r - 1, 0, r, c, n, ans);
    put(r - 1, c - 1, r, c, n, ans);
    for (int i = 0; i < r; i++) {
        put(i, 0, r, c, n, ans);
        put(i, c - 1, r, c, n, ans);
    }
    for (int j = 0; j < c; j++) {
        put(0, j, r, c, n, ans);
        put(r - 1, j, r, c, n, ans);
    }
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            put(i, j, r, c, n, ans);
        }
    }
}

int greedy(int r, int c, int n) {
    
    if (r > c) {
        swap(r, c);
    }
    int ans = 0;
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            a[i][j] = 0;
        }
    }
    for (int i = 0; i < r; i++) {
        for (int j = i & 1; j < c; j += 2) {
            put(i, j, r, c, n, ans);
        }
    }
    put(r, c, n, ans);
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            b[i][j] = a[i][j];
        }
    }
    return ans;
}

int greedy2(int r, int c, int n) {
    
    if (r > c) {
        swap(r, c);
    }
    int ans = 0;
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            a[i][j] = 0;
        }
    }
    for (int i = 0; i < r; i++) {
        for (int j = (i & 1) ^ 1; j < c; j += 2) {
            put(i, j, r, c, n, ans);
        }
    }
    put(r, c, n, ans);
    return ans;
}

int solve(int r, int c, int n, int &maskans) {
    
    if (r > c) {
        swap(r, c);
    }
    
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= c; j++) {
            for (int mask = 0; mask < (1 << r); mask++) {
                can[j][i][mask] = 0;
                dp[j][i][mask] = 4 * n;
            }
        }
    }
    
    can[0][0][0] = 1;
    dp[0][0][0] = 0;
    
    for (int j = 0; j < c; j++) {
        for (int i = 0; i <= n; i++) {
            for (int mask = 0; mask < (1 << r); mask++) {
                if (!can[j][i][mask]) {
                    continue;
                }
                for (int newmask = 0; newmask < (1 << r); newmask++) {
                    int m = weight[newmask];
                    if (m + i > n) {
                        continue;
                    }
                    can[j + 1][i + m][newmask] = 1;
                    if (dp[j + 1][i + m][newmask] > dp[j][i][mask] + intersect[mask][newmask]) {
                        dp[j + 1][i + m][newmask] = dp[j][i][mask] + intersect[mask][newmask];
                        from[j + 1][i + m][newmask] = mask;
                    }
                }
            }
        }
    }
    
    int mindp = 4 * n;
    
    for (int mask = 0; mask < (1 << r); mask++) {
        if (!can[c][n][mask]) {
            continue;
        }
        if (dp[c][n][mask] < mindp) {
            maskans = mask;
            mindp = min(mindp, dp[c][n][mask]);
        }
        maskans = mask;
    }

    return mindp;
}

void check() {
    for (int r = 1; r <= MAXN * MAXN; r++) {
        for (int c = r; r * c <= MAXN * MAXN; c++) {
            for (int n = 1; n <= r * c; n++) {
                int dp1 = greedy(r, c, n);
                int dp3 = greedy2(r, c, n);
                int mask;
                int dp2 = solve(r, c, n, mask);
                if (dp1 != dp2 && dp3 != dp2) {
                    cout << r << " " << c << " " << n << " " << dp2 << " " << dp1 << " " << dp3 << endl;
                    int m = n;
                    for (int k = c; k >= 1; k--) {
                        for (int j = 0; j < r; j++) {
                            if (mask & (1 << j)) {
                                cout << "*";
                            }
                            else {
                                cout << ".";
                            }
                        }
                        int newmask = from[k][m][mask];
                        m -= weight[mask];
                        mask = newmask;
                        cout << endl;
                    }
                    cout << endl;
                    for (int k = 0; k < r; k++) {
                        for (int j = 0; j < c; j++) {
                            if (a[k][j]) {
                                cout << "*";
                            }
                            else {
                                cout << ".";
                            }
                        }
                        cout << endl;
                    }
                    cout << endl;
                    for (int k = 0; k < r; k++) {
                        for (int j = 0; j < c; j++) {
                            if (b[k][j]) {
                                cout << "*";
                            }
                            else {
                                cout << ".";
                            }
                        }
                        cout << endl;
                    }
                    cout << endl;
                }
            }
        }
    }
}

void solve() {
    int r, c;
    int n;
    cin >> r >> c >> n;

    
    cout << min(greedy(r, c, n), greedy2(r, c, n));
    
}

int main(){
#ifndef ONLINE_JUDGE
    freopen("B-large.in-2.txt", "rt", stdin);
//        freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif
    
//    precalc();
    
//    check();
    
    int t;
    cin >> t;
    
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }
    
}
