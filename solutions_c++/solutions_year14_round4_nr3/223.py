#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cstdio>

using namespace std;

int D[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

int W, H, B;
bool map[100][500];
int ans;

bool can_move(int x, int y, int d, int *next_x, int *next_y) {
    if (d < 0)
        d += 4;
    *next_x = x + D[d][0];
    *next_y = y + D[d][1];
    if (*next_x < 0 || *next_x >= W) return false;
    if (*next_y < 0 || *next_y >= H) return false;
    return !map[*next_x][*next_y];
}

int flow(int x, int y, int direction) {
    map[x][y] = true;
    if (y == H - 1)
        return 1;

    for (int next_d = direction - 1; next_d <= direction + 1; next_d++) {
        int next_x, next_y;
        if (can_move(x, y, next_d, &next_x, &next_y)) {
            int r = flow(next_x, next_y, next_d);
            if (r == 1)
                return r;
        }
    }
    return 0;
}

void solve() {
    cin >> W >> H >> B;
    memset(map, false, sizeof(map));
    for (int i = 0; i < B; i++) {
        int x0, y0, x1, y1;
        cin >> x0 >> y0 >> x1 >> y1;
        for (int x = x0; x <= x1; x++)
            for (int y = y0; y <= y1; y++)
                map[x][y] = true;
    }

    ans = 0;
    for (int i = 0; i < W; i++) {
        if (!map[i][0]) {
            ans += flow(i, 0, 0);
        }
    }

    cout << ans << endl;
}

int main() {
    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; testcase++) {
        cout << "Case #" << testcase << ": ";
        solve();
    }

    return 0;
}
