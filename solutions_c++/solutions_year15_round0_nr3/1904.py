#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>

using namespace std;
const int N = 10010;
char s[N];
int dp[N][N];
int d[5][5] = {0, 0, 0, 0, 0,
               0, 1, 2, 3, 4,
               0, 2, -1, 4, -3,
               0, 3, -4, -1, 2,
               0, 4, 3, -2, -1};

int tran(char ch) {
    if (ch == '1') return 1;
    if (ch == 'i') return 2;
    if (ch == 'j') return 3;
    return 4;
}

int cal(int x, int y) {
    int xx, yy, rr, r;
    if (x > 0) xx = 1; else xx = -1;
    if (y > 0) yy = 1; else yy = -1;
    r = d[abs(x)][abs(y)];
    if (r > 0) rr = 1; else rr = -1;
    r = abs(r);
    return rr * xx * yy * r;
    
}

bool solve(char *s, int n) {
    for (int i = 0; i < n; i++)
    {
        char now = 1;
        for (int j = i; j < n; j++)
        {
            now = cal(now, tran(s[j]));
            dp[i][j] = now;
        }
    }
    //cout<<dp[0][2]<<dp[3][5]<<dp[6][11]<<endl;
    for (int i = 0; i < n; i++)
        for (int j = i + 2; j < n; j++)
            if (dp[0][i] == 2 && dp[i+1][j-1] == 3 && dp[j][n-1] == 4)
                return true;
    return false;
}

int main() {
    int o, n, m, cas = 0;
    scanf("%d", &o);
    while (o--) {
        scanf("%d%d", &n, &m);
        scanf("%s", s);
        for (int i = 0; i < n * m; i++)
            s[i] = s[i % n];
        printf("Case #%d: ", ++cas);
        if (solve(s, n*m)) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}