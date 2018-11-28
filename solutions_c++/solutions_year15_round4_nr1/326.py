#include <cstdio>
const int LEFT = 1, RIGHT = 2, UP = 4, DOWN = 8;
int main() {
    int T;
    scanf("%d", &T);
    for (int t=1; t<=T; t++) {
        int r, c;
        scanf("%d%d", &r,&c);
        char a[r][c+2];
        for (int i=0; i<r; i++) scanf("%s", a[i]);
        char blocked[r][c], state[r][c];
        for (int i=0; i<r; i++)
            for (int j=0; j<c; j++) {
                blocked[i][j] = 0;
                char x = a[i][j];
                state[i][j] = (x == '.' ? 0 : x == '^' ? UP : x == 'v' ? DOWN : x == '>' ? RIGHT : LEFT);
            }
        for (int i=0; i<r; i++) {
            int y = 0;
            while (y < c && a[i][y] == '.') y++;
            if (y < c) blocked[i][y] |= LEFT;
        }
        for (int i=0; i<r; i++) {
            int y = c-1;
            while (y >= 0 && a[i][y] == '.') y--;
            if (y >= 0) blocked[i][y] |= RIGHT;
        }
        for (int i=0; i<c; i++) {
            int x = 0;
            while (x < r && a[x][i] == '.') x++;
            if (x < r) blocked[x][i] |= UP;
        }
        for (int i=0; i<c; i++) {
            int x = r-1;
            while (x >= 0 && a[x][i] == '.') x--;
            if (x >= 0) blocked[x][i] |= DOWN;
        }
        int res = 0;
        for (int i=0; i<r && res>=0; i++)
            for (int j=0; j<c && res>=0; j++) {
                if (blocked[i][j] == 15 && state[i][j] != 0) res = -1;
                else if (blocked[i][j] & state[i][j]) res++;
            }
        printf("Case #%d: ", t);
        if (res == -1) printf("IMPOSSIBLE\n"); else printf("%d\n", res);
    }
    return 0;
}
