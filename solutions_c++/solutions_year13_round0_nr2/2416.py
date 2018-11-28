#include <algorithm>
#include <cassert>
#include <cstdio>
#include <iostream>
using namespace std;
#define For(i,x) for (int i=0; i<(int)(x); i++)

const int N = 110;

class Outof {
    int rows, cols;
public:
    Outof(int rows, int cols) : rows(rows), cols(cols) {}
    bool operator()(int r, int c) {
        if (r < 0 || r >= rows) return true;
        if (c < 0 || c >= cols) return true;
        return false;
    }
};

void display(int rows, int cols, int bd[][N]) {
    For(i, rows) {
        For(j, cols) {
            printf("%d ", bd[i][j]);
        }
        printf("\n");
    }
}

bool cut_straight(int rows, int cols, int bd[][N], int finalbd[][N], int ox, int oy, int dx, int dy, bool overwrite) {
    Outof outof(rows, cols);
    int x = ox;
    int y = oy;
    while (!outof(x, y)) {
        if (finalbd[x][y] > finalbd[ox][oy]) {
            // cannot cut
            return false;
        }
        if (overwrite)
            bd[x][y] = min(bd[x][y], finalbd[ox][oy]);

        x += dx;
        y += dy;
    }

    x = ox;
    y = oy;
    while (!outof(x, y)) {
        if (finalbd[x][y] > finalbd[ox][oy]) {
            return false;
        }
        if (overwrite)
            bd[x][y] = min(bd[x][y], finalbd[ox][oy]);

        x += -dx;
        y += -dy;
    }
    return true;
}

bool cut(int rows, int cols, int bd[][N], int finalbd[][N]) {
    const int tab[][2] = {
        { 0, 1 },
        { 1, 0 },
//        { 1, 1 },
//        { -1, 1 },
    };
    const int tab_sz = sizeof(tab) / sizeof(tab[0]);

    For(i, rows) For(j, cols) {
        assert(bd[i][j] >= finalbd[i][j]);
        if (bd[i][j] == finalbd[i][j]) continue;

        bool cutted = false;
        For(k, tab_sz) {
            int dx = tab[k][0];
            int dy = tab[k][1];
            bool ok = cut_straight(rows, cols, bd, finalbd, i, j, dx, dy, false);

            if (ok) {
                cut_straight(rows, cols, bd, finalbd, i, j, dx, dy, true);
                cutted = true;
                break;
            }
        }

        if (!cutted) return false;

//         if (cutted) {
//             printf("cut %d %d\n", i, j);
//             display(rows, cols, bd);
//             puts("");
//         }
    }

    // check
    For(i, rows) For(j, cols) {
        assert(bd[i][j] == finalbd[i][j]);
    }

    return true;
}

bool calc(int rows, int cols, int finalbd[][N]) {
    int bd[N][N];
    For(i, rows) For(j, cols) bd[i][j] = 100;

    bool ret = cut(rows, cols, bd, finalbd);
    return ret;
}

int main() {
    int ncases;
    scanf("%d", &ncases);

    For(cc, ncases) {
        int rows, cols;
        scanf("%d %d", &rows, &cols);

        int bd[N][N];
        For(i, rows) For(j, cols) {
            scanf("%d", &bd[i][j]);
        }

        bool ok = calc(rows, cols, bd);
        printf("Case #%d: %s\n", cc+1, (ok ? "YES" : "NO"));
    }
}



