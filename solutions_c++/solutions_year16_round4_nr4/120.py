#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <stack>
#include <bitset>
#define INF 0x3f3f3f3f
#define eps 1e-8
#define FI first
#define SE second
using namespace std;
typedef long long ll;

char s[10][10];

int n;

int ok[10][10];

inline int bitcount(int s) {
    int c = 0;
    while(s) {
        s ^= s & -s;
        ++ c;
    }
    return c;
}

int who[10];

bool dp[5][1 << 4];

inline bool bad(int x, int c) {
    memset(dp, 0, sizeof(dp));
    dp[0][0] = true;
    for(int i = 1; i <= c; ++ i) {
        int w = who[i - 1];
        for(int j = 0; j < 1 << n; ++ j) {
            if(!dp[i - 1][j]) continue;
            for(int k = 0; k < n; ++ k) {
                if(k == x) continue;
                if(!ok[w][k]) continue;
                if(j >> k & 1) continue;
                dp[i][j | (1 << k)] = true;
            }
        }
    }
    for(int i = 0; i < 1 << n; ++ i) {
        if(i >> x & 1) continue;
        if(bitcount(i) == c && dp[c][i]) return true;
    }
    return false;
}

inline bool check(int st) {
    for(int i = 0; i < n; ++ i) {
        for(int j = 0; j < n; ++ j) {
            int p = i * n + j;
            if(s[i][j] == '1' && (st >> p & 1))
                return false;
            ok[i][j] = 0;
            ok[i][j] |= s[i][j] == '1';
            ok[i][j] |= st >> p & 1;
        }
    }
    for(int i = 0; i < n; ++ i) {
        int c = 0;
        for(int j = 0; j < n; ++ j) {
            if(ok[j][i])
                who[c ++] = j;
        }
        if(bad(i, c)) return false;
    }
    return true;
}

int main() {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("Ds.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++ cas) {
        scanf("%d", &n);
        for(int i = 0; i < n; ++ i) {
            scanf("%s", s[i]);
        }
        int tot = n * n;
        int ans = INF;
        for(int i = 0; i < 1 << tot; ++ i) {
            int c = bitcount(i);
            if(c >= ans) continue;
            if(check(i)) ans = c;
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
