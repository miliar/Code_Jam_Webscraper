#include <iostream>
#include <queue>
#include <vector>
#include <functional>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    int T;
    cin >> T;
    for (int t=1; t<=T; t++) {
        long long n;
        long long m;
        cin >> n >> m;
        cout << "Case " << "#" << t << ": ";
        long long max_num = (1ll << (n - 2));
        if (m > max_num) {
            cout << "IMPOSSIBLE\n";
            continue;
        }
        cout << "POSSIBLE\n";
        int matr[100][100];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (j > i) {
                    matr[i][j] = 1;
                } else {
                    matr[i][j] = 0;
                }
            }
        }


        if (m == max_num) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    cout << (char)('0' + matr[i][j]);
                }
                cout << "\n";
            }
            continue;
        }

        matr[1][n] = 0;
        int v=2;
        for (int k=0; k<=n-3; k++) {
            if (! (m & (1ll << k))) {
                matr[v][n] = 0;
            }
            v++;
        }


        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                cout << (char)('0' + matr[i][j]);
            }
            cout << "\n";
        }
        continue;

    }
    return 0;
}
