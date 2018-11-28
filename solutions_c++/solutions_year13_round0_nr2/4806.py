/*
    TASK:
    DATE: 2012-12-09
    STATE: AC
    Solution:
*/
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <string>
#include <map>
#include <set>
#define maxn 1000
#define maxm 100000
#define INF 0x3f3f3f3f
using namespace std;

int T, n, m;
int a[121][121];
bool flag;

bool solve() {
    for (int i=1; i<=n; i++)
        for (int j=1; j<=m; j++) {
            bool f1 = true, f2 = true;
            int x = a[i][j];
            for (int k=1; k<=m; k++) f1 &= a[i][k] <= x;
            for (int k=1; k<=n; k++) f2 &= a[k][j] <= x;
            if (!(f1 || f2)) return false;
        }
    return true;
}

int main() {
//    freopen(//"a.in", "r", stdin);
//    freopen("a.out", "w", stdout);
    scanf("%d", &T);
    for(int t=1; t<=T; t++) {
        scanf("%d%d", &n, &m);
        for (int i=1; i<=n; i++)
            for (int j=1; j<=m; j++) scanf("%d", &a[i][j]);
        flag = solve();
        printf("Case #%d: %s\n", t, (flag) ? "YES" : "NO");
    }
    return 0;
//    fclose(stdout);
}
