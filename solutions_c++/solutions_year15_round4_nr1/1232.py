#include <cstdio>
#include <cassert>

const int MXN = 120;

char map[MXN][MXN];
bool edg[MXN][MXN][4];

int conv(char c) {
    switch (c) {
        case '^':
            return 0;
        case 'v':
            return 1;
        case '<':
            return 2;
        case '>':
            return 3;
        default:
            assert(false);
    }
}

int main() {

    int t;
    scanf("%d", &t);

    for (int T = 1; T <= t; T++) {

        int r, c;
        scanf("%d %d", &r, &c);

        for (int i = 0; i < r; i++)
            scanf("%s", map[i]);

        for (int i = 0; i < r; i++)
            for (int j = 0; j < c; j++)
                for (int d = 0; d < 4; d++)
                    edg[i][j][d] = false;

        for (int i = 1; i < r; i++)
            for (int j = 0; j < c; j++)
                edg[i][j][0] = edg[i - 1][j][0] || (map[i - 1][j] != '.');
        for (int i = r - 2; i >= 0; i--)
            for (int j = 0; j < c; j++)
                edg[i][j][1] = edg[i + 1][j][1] || (map[i + 1][j] != '.');
        for (int j = 1; j < c; j++)
            for (int i = 0; i < r; i++)
                edg[i][j][2] = edg[i][j - 1][2] || (map[i][j - 1] != '.');
        for (int j = c - 2; j >= 0; j--)
            for (int i = 0; i < r; i++)
                edg[i][j][3] = edg[i][j + 1][3] || (map[i][j + 1] != '.');

        int need = 0;
        bool win = true;
        for (int i = 0; i < r; i++)
            for (int j = 0; j < c; j++) if (map[i][j] != '.') {
                bool good = false;
                for (int d = 0; d < 4; d++)
                    good |= edg[i][j][d];
                if (good) {
                    need += !edg[i][j][conv(map[i][j])];
                } else {
                    win = false;
                }
            }

        printf("Case #%d: ", T);
        if (win)
            printf("%d\n", need);
        else
            puts("IMPOSSIBLE");

    }

}
