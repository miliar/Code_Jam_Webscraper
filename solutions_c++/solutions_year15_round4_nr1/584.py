#include <iostream>
#include <cstdio>
using namespace std;

int R, C;
char a[105][105];

int neibor(int y, int x, char dir) {
    int nei = 0;
    for (int j = 0; j < R; ++j) {
        if (j == y)  continue;
        if (j < y && dir == '^' && a[j][x] != '.')  ++nei;
        if (j > y && dir == 'v' && a[j][x] != '.')  ++nei;
    }

    for (int i = 0; i < C; ++i) {
        if (i == x)  continue;
        if (i < x && dir == '<' && a[y][i] != '.')  ++nei;
        if (i > x && dir == '>' && a[y][i] != '.')  ++nei;
    }

    return nei;
}

int allnei(int y, int x) {
    return neibor(y, x, '^') + neibor(y, x, 'v') + neibor(y, x, '<') + neibor(y, x, '>');
}

int main () {
    int T;
    cin >> T;
    for (int tt = 1; tt <= T; ++tt) {
        cin >> R >> C;
        for (int j = 0; j < R; ++j) {
            for (int i = 0; i < C; ++i) {
                cin >> a[j][i];
            }
        }

        bool isok = true;
        int tochange = 0;

        for (int j = 0; j < R && isok; ++j) {
            for (int i = 0; i < C; ++i) {
                if (a[j][i] == '.')  continue;
                int t = allnei(j, i);
                if (t == 0) {
                    isok = false;
                    break;
                } else {
                    if (neibor(j, i, a[j][i]) == 0) ++tochange;
                }
            }
        }

        if (!isok) {
            printf("Case #%d: IMPOSSIBLE\n", tt);
        } else {
            printf("Case #%d: %d\n", tt, tochange);
        }

    }

    return 0;
}

