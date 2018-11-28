#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

using namespace std;

int W, H, B, ans;
int g[501][501], f[501][501];
bool valid(int x, int y) { return 0 <= x && x < H && 0 <= y && y < W; }
int kGo[8][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};

void search(int x, int y, int cost) {
    if (g[x][y] != -1)
        cost += 1;

    if (cost >= ans || cost >= f[x][y])
        return;
    f[x][y] = cost;
    if (y == W - 1) {
        ans = min(ans, cost);
        return;
    }

    for (int d = 0; d < 8; ++d) {
        int dx = x + kGo[d][0], dy = y + kGo[d][1];
        if (!valid(dx, dy))
            continue;
        search(dx, dy, cost);
    }
}

void solve() {
    scanf("%d %d %d", &W, &H, &B);
    for (int i = 0; i < H; ++i)
        for (int j = 0; j < W; ++j) {
            g[i][j] = 0;
            f[i][j] = H * W;
        }
    for (int i = 0; i < B; ++i) {
        int X0, X1, Y0, Y1;
        scanf("%d %d %d %d", &X0, &Y0, &X1, &Y1);
        for (int x = X0; x <= X1; ++x)
            for (int y = Y0; y <= Y1; ++y)
                g[y][x] = -1;
    }
    ans = W;
    for (int i = 0; i < H; ++i)
        search(i, 0, 0);
    /*
    for (int i = 0; i < W; ++i) {
        for (int j = 0; j < H; ++j) {
            if (i == 0) {
                if (g[j][i] == -1)
                    f[j][i] = 0;
                else
                    f[j][i] = 1;
            } else {
                int cur = g[j][i] == -1 ? 0 : 1;
                int minAdj = f[j][i - 1];
                if (j > 0)
                    minAdj = min(minAdj, f[j - 1][i - 1]);
                if (j + 1 < H)
                    minAdj = min(minAdj, f[j + 1][i - 1]);
                f[j][i] = minAdj + cur;
            }
        }
    }
    for (int i = 0; i < H; ++i)
        ans = min(ans, f[i][W - 1]);*/
    printf("%d\n", ans);
}

int main() {
    int numCases;
    scanf("%d", &numCases);
    for (int caseNo = 1; caseNo <= numCases; ++caseNo) {
        printf("Case #%d: ", caseNo);
        solve();
    }
    return 0;
}

