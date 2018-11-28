#include <iostream>
using namespace std;

const int maxn = 100;
const int maxm = 100;

int main() {
    int t, tt, n, m, i, j, k;
    bool can1, can2, can;
    int mat[maxn][maxm];

    cin >> t;
    for (tt = 1; tt <= t; tt++) {
        cin >> n >> m;
        for (i = 0; i < n; i++) {
            for (j = 0; j < m; j++) {
                cin >> mat[i][j];
            }
        }

        can = true;
        for (i = 0; i < n && can; i++) {
            for (j = 0; j < m && can; j++) {
                can1 = true;
                can2 = true;

                for (k = 0; k < n; k++) {
                    if (mat[k][j] > mat[i][j]) {
                        can1 = false;
                        break;
                    }
                }

                for (k = 0; k < m; k++) {
                    if (mat[i][k] > mat[i][j]) {
                        can2 = false;
                        break;
                    }
                }

                can &= (can1 | can2);
            }
        }

        cout << "Case #" << tt << ": " << (can ? "YES": "NO") << endl;
    }

    return 0;
}

