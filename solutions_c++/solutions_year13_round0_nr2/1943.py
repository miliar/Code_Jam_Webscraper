#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>

using namespace std;

int a[111][111], b[111][111];

void solve() {
    int n, m;
    cin >> n >> m;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++) {
            cin >> a[i][j];
            b[i][j] = 100;
        }

    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++) {
//            for (int x = 1; x <= n; x++)  {
//                for (int y = 1; y <= m; y++)
//                    cout << b[x][y] << " ";
//                cout << endl;
//            }
//            cout << endl;
            if (b[i][j] == a[i][j]) continue;
            if (b[i][j] < a[i][j]) {
                cout << "NO" << endl;
                return;
            }
            bool ok = true;
            for (int k = 1; k <= m; k++)
                if (a[i][k] > a[i][j]) {
                    ok = false;
                    break;
                }
            if (ok) {
                for (int k = 1; k <= m; k++)
                    if (b[i][k] > a[i][j])
                        b[i][k] = a[i][j];
                continue;
            }
            ok = true;
            for (int k = 1; k <= n; k++)
                if (a[k][j] > a[i][j]) {
                    ok = false;
                    break;
                }
            if (ok) {
                for (int k = 1; k <= n; k++)
                    if (b[k][j] > a[i][j])
                        b[k][j] = a[i][j];
                continue;
            }
        }
    for (int i = 1; i <= n; i++)
        for (int j = 1 ; j <= m; j++)
            if (b[i][j] != a[i][j]) {
                cout << "NO" << endl;
                return;
            }
    cout << "YES" << endl;
}

int main() {

    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);

    int T, test = 0;
    cin >> T;
    while (T > 0) {
        ++test;
        cout << "Case #" << test <<": ";
        solve();
        --T;
    }

}
