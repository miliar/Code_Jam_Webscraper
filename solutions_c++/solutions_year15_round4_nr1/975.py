#include <cstdio>
#include <algorithm>
#define MAXR 101

int solve() {
    char g[MAXR][MAXR];
    int R, C;

    scanf("%d %d ", &R, &C);
    for (int i = 0; i < R; ++i) {
        scanf("%s ", g[i]);
    }

    int how_many = 0;
    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            bool fall_off = true;
            if (g[i][j] == '^') {
                for (int k = i-1; k >= 0 && fall_off; --k)
                    fall_off = fall_off && g[k][j] == '.';
            }
            if (g[i][j] == '>') {
                for (int k = j+1; k < C && fall_off; ++k)
                    fall_off = fall_off && g[i][k] == '.';
            }
            if (g[i][j] == 'v') {
                for (int k = i+1; k < R && fall_off; ++k)
                    fall_off = fall_off && g[k][j] == '.';
            }
            if (g[i][j] == '<') {
                for (int k = j-1; k >= 0 && fall_off; --k)
                    fall_off = fall_off && g[i][k] == '.';
            }
            if (g[i][j] == '.') {
                fall_off = false;
            }
            if (fall_off) {
                ++how_many;
                bool can_be_saved = false;
                for (int k = 0; k < R; ++k) {
                    if (k != i && g[k][j] != '.')
                        can_be_saved = true;
                }
                for (int k = 0; k < C; ++k) {
                    if (k != j && g[i][k] != '.')
                        can_be_saved = true;
                }
                if (!can_be_saved)
                    return -1;
            }
        }
    }

    return how_many;
}

int main() {
    int T;

    scanf("%d ", &T);
    for(int i = 1; i <= T; ++i) {
        int s = solve();
        if (s == -1) {
            printf("Case #%d: IMPOSSIBLE\n", i);
        } else {
            printf("Case #%d: %d\n", i, s);
        }
    }

    return 0;
}
