#include <iostream>
#include <sstream>
#include <string>
#include <stdio.h>
#include <iomanip>
#include <cstring>
#define eps 1e-9
using namespace std;

int mi[8] = {-1, -1, -1, 0, 1, 1, 1, 0 };
int mj[8] = {-1,  0,  1, 1, 1, 0, -1, -1 };

void solve() {
    int N, M, R;
    cin >> N >> M >> R;
    int n = 0, m = 0, r = R;

    char T[50][50];
    for (int i = 0; i < N; i++) for (int j = 0; j < M; j++)
        T[i][j] = '.';

    while (R > 0) {
        if (N - n < M - m) {
            for (int i = n; i < N && R > 0; i++) {
                if (R == 1 && i == N - 2) {
                    if (M - m > 0 && N > 1) {
                        break;
                    }
                }
                T[i][m] = '*';
                R--;
            }
            m++;
        } else {
            for (int j = m; j < M && R > 0; j++) {
                if (R == 1 && j == M - 2) {
                    if (N - n > 0 && M > 1) {
                        break;
                    }
                }
                T[n][j] = '*';
                R--;
            }
            n++;
        }
    }

    int revealed = 1;
    T[N-1][M-1] = 'c';

    bool D[50][50];
    memset(D, 0, sizeof(D));
    D[N - 1][M - 1] = true;

    bool has_r = true;
    while (has_r) {
        has_r = false;
        for (int i = 0; i < N; i++) 
        for (int j = 0; j < M; j++) {
            if (D[i][j]) {
                bool hm = false;
                for (int qi = 0; qi < 8; qi++) {
                    int ni = mi[qi] + i;
                    int nj = mj[qi] + j;
                    if (ni >= 0 && ni < N && nj >= 0 && nj < M) {
                        if (T[ni][nj] == '*') hm = true;
                    }
                }
                if (!hm) { 
                    for (int qi = 0; qi < 8; qi++) {
                        int ni = mi[qi] + i;
                        int nj = mj[qi] + j;
                        if (ni >= 0 && ni < N && nj >= 0 && nj < M) {
                            if (!D[ni][nj]) {
                                has_r = true;
                                revealed++;
                                D[ni][nj] = true;
                            }
                        }
                    }
                }
            }
        }
    }
    
    if (revealed + r != N*M) {
        cout << "Impossible" << endl;
        return;
    }
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cout << T[i][j];
        }
        cout << endl;
    }
}

int main() {
    int t;
    cin >> t;
    for (int qq = 1; qq <= t; qq++) {
        cout << "Case #" << qq << ":" << endl;
        solve();
    }
}
