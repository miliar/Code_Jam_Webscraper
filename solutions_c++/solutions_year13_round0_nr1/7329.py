#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <math.h>
#include <queue>

using namespace std;

char s[5][5];

bool win(char x) {
    bool ok = 0;
    for (int i = 0; i < 4; ++i) {
        bool has = 1;
        for (int j = 0; j < 4; ++j)
            has &= s[i][j] == x || s[i][j] == 'T';
        ok |= has;
    }

    for (int i = 0; i < 4; ++i) {
        bool has = 1;
        for (int j = 0; j < 4; ++j)
            has &= s[j][i] == x || s[j][i] == 'T';
        ok |= has;
    }

    bool d1 = 1, d2 = 1;
    for (int i = 0; i < 4; ++i) {
        d1 &= s[i][i] == x || s[i][i] == 'T';
        d2 &= s[i][3-i] == x || s[i][3-i] == 'T';
    }

    return ok || d1 || d2;
}

int main() {
    freopen("A-large.IN", "r", stdin);
    freopen("sol.txt", "w", stdout);

    int T;
    scanf("%d", &T);

    for (int t = 1; t <= T; ++t) {
        bool fin = 1;
        for (int i = 0; i < 4; ++i) {
            scanf("%s", s[i]);
            for (int j = 0; j < 4; ++j) {
                if (s[i][j] == '.') fin = 0;
            }
        }

        bool winX = win('X');
        bool winO = win('O');

        printf("Case #%d: ", t);

        if (winX) {
            printf("X won\n");
        } else if (winO) {
            printf("O won\n");
        } else if (fin) {
            printf("Draw\n");
        } else {
            printf("Game has not completed\n");
        }
    }

    return 0;
}
