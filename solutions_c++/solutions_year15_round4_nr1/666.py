#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <queue>

#define LL long long
#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define PII pair<int, int>
#define PID pair<int, double>

using namespace std;

int T, n, m;
char map[110][110];

bool walk(int x, int y, int dx, int dy) {
    x += dx; y += dy;
    while (x > 0 && x <= n && y > 0 && y <= m) {
        if (map[x][y] != '.') return true;
        x += dx; y += dy;
    }
    return false;
}

int main(){
    scanf("%d", &T);
    for (int Tno = 1; Tno <= T; ++Tno) {
        scanf("%d%d", &n, &m);
        for (int i = 1; i <= n; ++i)
            scanf("%s", map[i] + 1);

        int ans = 0;
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                if (map[i][j] == '.') continue;
                bool up = walk(i, j, -1, 0),
                     down = walk(i, j, 1, 0),
                     left = walk(i, j, 0, -1),
                     right = walk(i, j, 0, 1);
                char c = map[i][j];
                if (c == '^' && up) continue;
                if (c == 'v' && down) continue;
                if (c == '<' && left) continue;
                if (c == '>' && right) continue;
                if (up || down || left || right) ++ans;
                else ans = -1e9;
            }
        }

        printf("Case #%d: ", Tno);
        if (ans < 0) printf("IMPOSSIBLE\n");
        else printf("%d\n", ans);
    }
}
