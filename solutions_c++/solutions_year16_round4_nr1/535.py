/*
 * A.cpp
 * Copyright (C) 2016 mlckq <moon5ckq@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */
#include <cstdio>
#include <string>

using namespace std;

string f[14][3];
int g[14][3][3];

// 0p, 1r, 2s

#define n(x) ((x) + 1)%3
#define m(x) ((x) + 2)%3

int main() {

    f[1][0] = 'P';
    f[1][1] = 'R';
    f[1][2] = 'S';
    g[1][0][0] = 1;
    g[1][1][1] = 1;
    g[1][2][2] = 1;

    for (int i = 2; i <= 13; ++i) {
        for (int j = 0; j < 3; ++j) {
            f[i][j] = f[i-1][n(j)] + f[i-1][m(j)];
            string tmp = f[i-1][m(j)] + f[i-1][n(j)];
            if (f[i][j] > tmp) f[i][j] = tmp;
            for (int k = 0; k < 3; ++k)
                g[i][j][k] += g[i-1][n(j)][k] + g[i-1][m(j)][k];
        }
    }

//    printf("%s\n", f[3][2].c_str());
//    printf("%s\n", f[12][1].c_str());

    int T;
    scanf("%d", &T);
    for (int c = 1; c <= T; ++c) {
        printf("Case #%d: ", c);
        int N, R, P, S;
        scanf("%d%d%d%d", &N, &R, &P, &S);
        string best = "";
        for (int j = 0; j < 3; ++j) {
            if (g[N + 1][j][0] == P &&
                g[N + 1][j][1] == R &&
                g[N + 1][j][2] == S) {
                if (best.size() == 0 || best > f[N+1][j])
                    best = f[N+1][j];
            }
        }
        if (best.size() == 0) printf("IMPOSSIBLE\n");
        else printf("%s\n", best.c_str());
    }

    return 0;
}
