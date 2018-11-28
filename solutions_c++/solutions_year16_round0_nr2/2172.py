#include <bits/stdc++.h>

using namespace std;

char s[105];
int dp[105][105][2];
int Min(int a, int b) {if(a < 0) return b; else return a < b ? a : b;}
int go1(int a, int b, int k) {
    if(dp[a][b][k] != -1) return dp[a][b][k];
    if(a == b) {
        if(k == 1 && s[a] == '+' || k == 0 && s[a] == '-') dp[a][b][k] = 0;
        else dp[a][b][k] = 1;
        return dp[a][b][k];
    }
    for(int i = a; i < b; i ++) {
        int x0 = go1(a, i, 0), x1 = go1(a, i, 1);
        int y0 = go1(i+1, b, 0), y1 = go1(i+1, b, 1);
        int val = -1;
        if(k == 1) {
            val = x0 + y0 + y0%2 + 1;
            val = Min(val, x0 + y1 + 1 - y1%2);
            val = Min(val, x1 + y0 + 2 - y0%2);
            val = Min(val, x1 + y1 + y1%2);
            dp[a][b][k] = Min(dp[a][b][k], val);
        } else {
            val = x0 + y0 + y0%2;
            val = Min(val, x0 + y1 + 2 - y1%2);
            val = Min(val, x1 + y0 + 1 - y0%2);
            val = Min(val, x1 + y1 + 1 + y1%2);
            dp[a][b][k] = Min(dp[a][b][k], val);
        }
    }
    return dp[a][b][k];
}

int main() {
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int i = 1; i <= T; i ++) {
        scanf("%s", s);
        int n = strlen(s);
        memset(dp, -1, sizeof(dp));
        printf("Case #%d: %d\n", i, go1(0, n-1, 1));
    }
    return 0;
}
