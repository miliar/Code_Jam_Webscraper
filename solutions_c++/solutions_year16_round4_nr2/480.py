#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

int N, K;
double thisAns, maxAns;
double P[505], Q[505], f[505][505];

double calc() {
    memset(f, 0, sizeof(f));

    f[0][0] = 1.0f;
    for (int i = 1; i <= K; ++i) {
        for (int j = 0; j < i; ++j) {
            f[j + 1][i - 1 - j] += f[j][i - 1 - j] * Q[i];
            f[j][i - 1 - j + 1] += f[j][i - 1 - j] * (1 - Q[i]);
        }
    }
    return f[K / 2][K / 2];
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int T;
    cin >> T;
    for (int Cas = 1; Cas <= T; ++Cas) {
        cin >> N >> K;
        for (int i = 1; i <= N; ++i) {
            cin >> P[i];
        }

        sort(P + 1, P + N + 1);

        maxAns = 0.0;
        for (int i = 0; i <= K; ++i) {
            int t = 0;
            for (int j = 1; j <= i; ++j) {
                Q[++t] = P[j];
            }
            for (int j = 1; j <= K - i + 1; ++j) {
                Q[++t] = P[N - (K - i) + j];
            }
            thisAns = calc();
            if (thisAns > maxAns) {
                maxAns = thisAns;
            }
        }

        printf("Case #%d: ", Cas);
        printf("%.8f\n", maxAns);
    }
    return 0;
}
