#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

const int maxn = 200;

const int dx[4] = {0, 0, 1, -1}, dy[4] = {1, -1, 0, 0};

int A[maxn][maxn];
int n, m;

bool isGood(int x, int y) {
    if (x >= n || y >= m || x < 0 || y < 0) return 0;
    if (A[x][y] == 5) return 1;
    int d = A[x][y];
    x += dx[d];
    y += dy[d];
    while (!(x >= n || y >= m || x < 0 || y < 0) && A[x][y] == 5) {
        x += dx[d];
        y += dy[d];
    }
    if (x >= n || y >= m || x < 0 || y < 0) return 0;
    return 1;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int test = 1; test <= T; ++test) {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                char c;
                cin >> c;
                if (c == '.') A[i][j] = 5;
                else if (c == '^') A[i][j] = 3;
                else if (c == 'v') A[i][j] = 2;
                else if (c == '>') A[i][j] = 0;
                else A[i][j] = 1;
            }
        }
        int Cnt = 0;
        int fl = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (!isGood(i, j)) {
                    ++Cnt;
                    int vb = 0;
                    for (int k = 0; k < 4; ++k) {
                        A[i][j] = k;
                        if (!isGood(i, j))++vb;
                    }
                    if (vb == 4) fl = 1;
                }
            }
        }
        if (fl) printf("Case #%d: IMPOSSIBLE\n", test);
        else printf("Case #%d: %d\n", test, Cnt);
    }
}