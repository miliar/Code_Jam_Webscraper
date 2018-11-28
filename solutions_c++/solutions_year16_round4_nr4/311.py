#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

int tests, n, acc, ans;
char g[30][30];
int order[4];
bool vis[30];

bool dfs(int d) {
    if (d == n) return true;
    int i = order[d], mark = false;;
    for (int j = 0; j < n; ++ j) {
        if (vis[j] || g[i][j] == '0') continue;
        vis[j] = true;
        mark = true;
        if (!dfs(d + 1)) return false;
        vis[j] = false;
    }
    return mark;
}

bool check() {
    for (int i = 0; i < n; ++ i)
        order[i] = i;
    bool mark = true;
    do {
        memset(vis, 0, sizeof(vis));
        if (!dfs(0)) {
            mark = false;
            break;
        }
    } while (next_permutation(order, order + n));
    return mark;
}

void dd(int i, int j) {
    if (j == n) {
        dd(i + 1, 0);
        return;
    }
    if (i == n) {
        if (check())
            ans = min(ans, acc);
        return;
    }
    if (g[i][j] == '1') dd(i, j + 1);
    else {
        dd(i, j + 1);
        g[i][j] = '1';
        ++ acc;
        if (acc < ans) dd(i, j + 1);
        -- acc;
        g[i][j] = '0';
    }
}

int main() {
    cin >> tests;
    for (int cases = 1; cases <= tests; ++ cases) {
        cin >> n;
        ans = n * n;
        for (int i = 0; i < n; ++ i)
            cin >> g[i];
        dd(0, 0);
//        cout << check() << endl;
        printf("Case #%d: %d\n", cases, ans);
    }
    return 0;
}
