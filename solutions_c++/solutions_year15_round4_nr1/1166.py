#include <bits/stdc++.h>
using namespace std;
int dx[] = {-1, 0, 1, 0};
int dy[] = {0, -1, 0, 1};
const char dirs[] = "^<v>";

int r, c;
char b[110][110];

bool find(int i, int j, int ddx, int ddy) {
    if (ddx)
        for (int i1 = i + ddx; i1 >= 0 and i1 < r; i1 += ddx)
            if (b[i1][j] != '.')
                return true;
    if (ddy)
        for (int j1 = j + ddy; j1 >= 0 and j1 < c; j1 += ddy)
            if (b[i][j1] != '.')
                return true;
    return false;
}

int main() {
    int cases;
    scanf("%d", &cases);
    for (int cs = 1; cs <= cases; cs++) {
        scanf("%d%d", &r, &c);
        for (int i = 0; i < r; i++)
            scanf("%s", b[i]);
        bool possible = true;
        int ans = 0;
        for (int i = 0; possible and i < r; i++)
            for (int j = 0; possible and j < c; j++)
                if (b[i][j] != '.') {
                    bool inc = true, found = false;
                    for (int dir = 0; dir < 4; dir++)
                        if (find(i, j, dx[dir], dy[dir])) {
                            found = true;
                            if (dirs[dir] == b[i][j])
                                inc = false;
                        }
                    if (!found) {
                        possible = false;
                    } else if (inc)
                        ans++;
                }
        if (possible)
            printf("Case #%d: %d\n", cs, ans);
        else
            printf("Case #%d: IMPOSSIBLE\n", cs);
    }
}
