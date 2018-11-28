/*
 * B.cpp
 * Copyright (C) 2016 mlckq <moon5ckq@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */
#include <iostream>
#include <algorithm>
using namespace std;

#define MAXN 205

double f[MAXN][MAXN];
int N, K;
double p[MAXN], q[MAXN];

int main() {
    int T;
    cin >> T;
    for(int c = 1; c <= T; ++c) {
        printf("Case #%d: ", c);
        cin >> N >> K;
        for (int i = 1; i <= N; ++i) {
            cin >> p[i];
            q[i] = p[i];
        }
        int X;

        sort(q + 1, q + N + 1);

        double best = 0;

        for (int x = 0; x <= K; ++x) {
            int k = 0;
            for (int i = 1; i <=x;++i)
                p[++k] = q[i];
            for (int i = x + 1; i <= K; ++i) {
                p[++k] = q[N - K + i];
            }
            if ( k == K) {
        memset(f, 0, sizeof(f));
        f[1][0] = 1 - p[1];
        f[1][1] = p[1];
        for (int i = 2; i <= K; ++i)
            for (int j = 0; j <= i; ++j)
                f[i][j] = f[i-1][j] * (1-p[i]) + f[i-1][j-1]*p[i];

//        printf("%.10f\n", f[K][K/2]);
        if (best < f[K][K/2]) {
            best = f[K][K/2];
            X = x;
        }
            }
        }

/*        for (int i = K/2 + 1; i <= K; ++i)
            p[i] = p[N-K + i];
        N = K;*/
/*        for (int i = 1; i<=N;++i)
        printf("%f, ", p[i]);
        puts("");
*/

        printf("%.10f\n", best);
        /*
        for (int i = 1; i <= N; ++i)
            printf("%f,",q[i]);
        puts("");
        for (int y = 0; y < N; ++y)
            if (X & (1 << y)) {
                printf("%f,", q[y + 1]);
            }
        puts("");*/
    }


    return 0;
}
