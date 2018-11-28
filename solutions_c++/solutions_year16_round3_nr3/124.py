#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

int A[10][10][10];
int g[10][10][10];
int J, P, S, K, N, maxAns;

int check() {
    int tmp(0);

    for (int i = 1; i <= J; ++i) {
        for (int j = 1; j <= P; ++j) {
            tmp = 0;
            for (int k = 1; k <= S; ++k) {
                tmp += g[i][j][k];
            }
            if (tmp > K) return -1;
        }
    }

    for (int i = 1; i <= J; ++i) {
        for (int k = 1; k <= S; ++k) {
            tmp = 0;
            for (int j = 1; j <= P; ++j) {
                tmp += g[i][j][k];
            }
            if (tmp > K) return -1;
        }
    }

    for (int j = 1; j <= P; ++j) {
        for (int k = 1; k <= S; ++k) {
            tmp = 0;
            for (int i = 1; i <= J; ++i) {
                tmp += g[i][j][k];
            }
            if (tmp > K) return -1;
        }
    }

    int res(0);
    for (int i = 1; i <= J; ++i)
        for (int j = 1; j <= P; ++j)
            for (int k = 1; k <= S; ++k) {
                if (g[i][j][k] == 1) {
                    ++res;
                }
            }

    return res;
}

void dfs(int who) {
    if (who >= N) {
        int ans = check();
        if (ans != -1) {
            if (ans > maxAns) {
                maxAns = ans;
                for (int i = 1; i <= J; ++i)
                    for (int j = 1; j <= P; ++j)
                        for (int k = 1; k <= S; ++k)
                            A[i][j][k] = g[i][j][k];
            }
        }
        return;
    }

    int i, j, k;
    i = (who / (P * S)) + 1;
    j = ((who % (P * S)) / S) + 1;
    k = (who % S) + 1;
    //cout << who << " " << i << " " << j << " " << k << endl;

    g[i][j][k] = 0;
    dfs(who + 1);
    g[i][j][k] = 1;
    dfs(who + 1);
}

int main()
{
    freopen("C.in", "r", stdin);
    //freopen("C.out", "w", stdout);

    int T;

    cin >> T;

    for (int i = 1; i <= T; ++i) {
        cin >> J >> P >> S >> K;

        N = J * P * S;

        maxAns = 0;

        cout << "Case #" << i << ": ";

        memset(g, 0, sizeof(g));

        dfs(0);

        cout << maxAns << endl;
        for (int i = 1; i <= J; ++i)
            for (int j = 1; j <= P; ++j)
                for (int k = 1; k <= S; ++k)
                    if (A[i][j][k]) {
                        cout << i << " " << j << " " << k << endl;
                    }
    }

    return 0;
}
