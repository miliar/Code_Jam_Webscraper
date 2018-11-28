#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
using namespace std;
#define SZ(v) ((int)(v).size())
#define REP(i, n) for (int i = 0; i < (n); ++i)
#define REPF(i, a, b) for (int i = (a); i <= (b); ++i)
#define REPD(i, a, b) for (int i = (a); i >= (b); --i)
const int maxint = -1u>>1;
const int maxn = 100 + 2;

int n, m;
int v[maxn][maxn];

bool row(int r, int x) {
    for (int i = 0; i < m; ++i) {
        if (v[r][i] > x) return false;
    }
    return true;
}

bool col(int c, int x) {
    for (int i = 0; i < n; ++i) {
        if (v[i][c] > x) return false;
    }
    return true;
}

bool work() {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (!row(i, v[i][j]) && !col(j, v[i][j])) return false;
        }
    }
    return true;
}

int main() {
    freopen("b.out", "w", stdout);
    int t, ca = 0;
    scanf("%d", &t);
    while (t--) {
        printf("Case #%d: ", ++ca);
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                scanf("%d", &v[i][j]);
            }
        }
        bool ans = work();
        if (ans) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}

