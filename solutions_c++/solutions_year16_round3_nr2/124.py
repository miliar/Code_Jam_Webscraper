#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

long long M;
int T, N, K, g[101][101];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);


    int T;
    cin >> T;

    for (int i = 1; i <= T; ++i) {
        cin >> N >> M;

        cout << "Case #" << i << ": ";

        if (M > (1ll << (N - 2))) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }

        cout << "POSSIBLE" << endl;

        memset(g, 0, sizeof(g));

        g[1][N] = 1;
        -- M;

        for (int i = 2; i <= N - 1; ++i)
            for (int j = i + 1; j <= N - 1; ++j)
                g[i][j] = 1;

        for (int i = 2; i <= N - 1; ++i)
            g[i][N] = 1;

        K = 0;
        while (1) {
            if (!M) {
                    break;
            }

            if (M % 2 == 1) {
                g[1][N - 1 - K] = 1;
            }
            M /= 2;

            ++K;
        }

        for (int i = 1; i <= N; ++i) {
                for (int j = 1; j <= N; ++j) {
                        cout << g[i][j];
                }
                cout << endl;
        }
    }



    return 0;
}
