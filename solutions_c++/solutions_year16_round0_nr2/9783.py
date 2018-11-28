#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 110;
int dp[N][N][2][2];
char s[N];
int n;
int sgn(char c) {
    if (c == '+') return 1;
    return 0;
}

void upd(int &x, int y) {
    if (x == -1) x = y;
    else x = min(x, y);
}

int dfs(int x, int y, int a, int b) {
    if (x == y) {
        return dp[x][y][a][b] = b != sgn(s[x]);
    }
    if (dp[x][y][a][b] != -1) return dp[x][y][a][b];
    int &ret = dp[x][y][a][b];
    if (a == 0) {
        if (sgn(s[y]) == b) upd(ret, dfs(x, y - 1, a, b));
        else upd(ret, dfs(x, y - 1, a, 1 - b) + 1);

        if (sgn(s[x]) != b) upd(ret, dfs(x + 1, y, 1 - a,1 - b) + 1);
        else upd(ret, dfs(x + 1, y, 1 - a, b) + 2);
    }
    else {
        if (sgn(s[x]) == b) upd(ret, dfs(x + 1, y, a, b));
        else upd(ret, dfs(x + 1, y, a, 1 - b) + 1);
        
        if (sgn(s[y]) != b) upd(ret, dfs(x, y - 1, 1 - a, 1 - b) + 1);
        else upd(ret, dfs(x, y - 1, 1 - a, b) + 2);
    }
    return dp[x][y][a][b];
}

void solve(int cas) {
    memset(dp, -1, sizeof(dp));
    scanf("%s", s + 1);
    n = strlen(s + 1);
    printf("Case #%d: %d\n", cas, dfs(1, n, 0, 1));
}

int main()
{
    int t;
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) solve(i);
    return 0;
}
