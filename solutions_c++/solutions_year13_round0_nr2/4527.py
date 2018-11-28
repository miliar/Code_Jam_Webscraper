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
const int maxint = -1u>>1;
const int maxn = 100 + 4;
const int dx[] = {0, 1};
const int dy[] = {1, 0};

int n, m;
int a[maxn][maxn];

bool ok(int k, int dir, int limit) {
    int x = k, y = 0;
    if (dir) swap(x, y);
    while (x < n && y < m) {
        if (a[x][y] > limit) return false;
        x += dx[dir];
        y += dy[dir];
    }
    return true;
}

bool check() {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (!ok(i, 0, a[i][j]) && !ok(j, 1, a[i][j])) return false;
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
                scanf("%d", &a[i][j]);
            }
        }
        bool ok = check();
        if (ok) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}

