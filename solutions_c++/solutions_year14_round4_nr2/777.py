#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <bitset>
#include <queue>
using namespace std;

#define rep(i, s, t) for (int i = (s); i <= (t); ++i)
#define REP(i, n) rep(i, 1, n)

int f[1111];
int g[1111];
int n, a[1111], b[1111], c[1111], vis[1111];
int s[1111], ans;
int sl[1111], sr[1111];
int Altria;

int dfs(int x){
    if (g[x] == Altria) return f[x];
    if (x > n) return 0;
    f[x] = 1e9;
    g[x] = Altria;
    f[x] = min(dfs(x + 1) + sl[x], f[x]);
    f[x] = min(dfs(x + 1) + sr[x], f[x]);
    return f[x];
}

void Fate(int ca){
    scanf("%d", &n);
    ans = 1e9;
    REP(i, n) scanf("%d", &a[i]);
    REP(i, n) b[i] = a[i];
    sort(b + 1, b + 1 + n);
    reverse(b + 1, b + 1 + n);
    REP(i, n) REP(j, n) if (a[j] == b[i]) s[i] = j;
    memset(sl, 0, sizeof sl);
    memset(sr, 0, sizeof sr);
    REP(i, n) REP(j, i - 1){
        sl[i] += s[i] < s[j];
        sr[i] += s[i] > s[j];
    }
    ++Altria;
    ans = min(ans, dfs(2));
    printf("Case #%d: ", ca);
    printf("%d\n", ans);
}

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int Ti;
    scanf("%d", &Ti);
    REP(x, Ti){
        Fate(x);
    }
}
