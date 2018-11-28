#include <bits/stdc++.h>

const int MAXR = 101;

bool gg(char arr[MAXR+2][MAXR+2], int x, int y) {
    int dx[] = {0, 1, 0, -1};
    int dy[] = {1, 0, -1, 0};

    int d = -1;
    if (arr[x][y] == '>') d = 0;
    if (arr[x][y] == 'v') d = 1;
    if (arr[x][y] == '<') d = 2;
    if (arr[x][y] == '^') d = 3;

    do {
        x += dx[d], y += dy[d];
        if (arr[x][y] == '\0') return true;
    } while (arr[x][y] == '.');

    return false;
}

int solve() {
    int r, c;
    scanf("%d%d", &r, &c);

    char arr[MAXR+2][MAXR+2] = {{}};

    int cntr[MAXR+2] = {};
    int cntc[MAXR+2] = {};

    for (int i = 1; i <= r; ++i) {
        scanf("%102s", arr[i] + 1);
        for (int j = 1; j <= c; ++j) {
            if (arr[i][j] != '.')
                cntr[i] += 1, cntc[j] += 1;
        }
    }

    int acc = 0;
    for (int i = 1; i <= r; ++i) {
        for (int j = 1; j <= c; ++j) {
            if (arr[i][j] == '.') continue;

            if (cntr[i] == 1 and cntc[j] == 1)
                return -1;

            if (gg(arr, i, j))
                acc += 1;
        }
    }

    return acc;
}

int main() {
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        printf("Case #%d: ", t);
        int ans = solve();
        if (ans == -1)
            puts("IMPOSSIBLE");
        else
            printf("%d\n", ans);
    }
    return 0;
}
