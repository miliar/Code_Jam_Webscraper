#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

int t, n, m;
int a[128][128];

bool solve() {
    for (int i = 1; i <= n; ++i) {
        a[i][0] = -1;
    }
    for (int i = 1; i <= m; ++i) {
        a[0][i] = -1;
    }
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (a[i][0] < a[i][j]) {
                a[i][0] = a[i][j];
            }
            if (a[0][j] < a[i][j]) {
                a[0][j] = a[i][j];
            }
        }
    }
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (!(a[i][j] == a[i][0] || a[i][j] == a[0][j])) {
                return false;
            }
        }
    }
    return true;
}

int main() {
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i) {
        scanf("%d %d", &n, &m);
        for (int x = 1; x <= n; ++x) {
            for (int y = 1; y <= m; ++y) {
                scanf("%d", &a[x][y]);
            }
        }
        printf("Case #%d: %s\n", i, solve() ? "YES" : "NO");
    }
    return 0;
}
