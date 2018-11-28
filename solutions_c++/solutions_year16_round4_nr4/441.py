#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
#define get GET
char get[200][200];
int ans;
int n;
int p1[200], p2[200];
void nex(int x, int y, int& x2, int& y2) {
    if (y == n)
        x2 = x + 1, y2 = 1;
    else
        x2 = x, y2 = y + 1;
}
int sel[200], mark[200], use[200];
bool check(int u) {
    sel[++sel[0]] = u;
    use[u] = 1;
    int cnt = 0;
    for (int i = 1; i <= n; i++)
        if (get[u][i] == '1' && !mark[i]) {
            mark[i] = 1;
            for (int k = 1; k <= n; k++)
                if (!use[k] && !check(k)) return false;
            cnt++;
            mark[i] = 0;
        }
    use[u] = 0;
    sel[0]--;
    if (cnt == 0) return false;
    return true;
}
bool check() {
    memset(use, 0, sizeof use);
    sel[0] = 0;
    memset(mark, 0, sizeof mark);
    for (int i = 1; i <= n; i++)
        if (!check(i)) return false;
    return true;
}
void solve(int n, int i = 1, int j = 1, int tot = 0) {
    if (i == n + 1) {
        if (check()) ans = min(ans, tot);
        return;
    }
    int ni, nj;
    nex(i, j, ni, nj);
    if (get[i][j] == '0') {
        get[i][j] = '1';
        solve(n, ni, nj, tot + 1);
        get[i][j] = '0';
    }
    solve(n, ni, nj, tot);
}
int main() {
    int cas;
    scanf("%d", &cas);
    for (int _ = 1; _ <= cas; _++) {
        scanf("%d", &n);
        for (int i = 1; i <= n; i++) scanf("%s", get[i] + 1);
        ans = n * n;
        for (int i = 0; i < n; i++) p1[i] = i + 1, p2[i] = p1[i];

        solve(n);
        for (int i = 1; i <= n; i++)
            cerr << get[i] + 1 << endl;  // scanf("%s", get[i] + 1);
        printf("Case #%d: %d\n", _, ans);
    }
}
