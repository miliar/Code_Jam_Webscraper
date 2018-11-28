#include <iostream>
#include <cstdio>

using namespace std;

int check_matrix(int a[200][200], int m, int n, int p, int q) {
    int t = a[p][q];
    int f = 1;
    int i, j;
    for (i = 0; i < n; i++) {
        if (a[p][i] > t) {
            f = 0;
            break;
        }
    }

    if (f == 0) {
        for (j = 0; j < m; j++) {
            if (a[j][q] > t) {
                return 0;
            }
        }
    }

    return 1;
}
int main ( ) {
    int a[200][200], t, k = 0, m, n, g, p, i, j;
    cin >> t;
    for (p = 0; p < t; p++) {
        g = 0;
        cin >> m >> n;
        for (i = 0; i < m; i++) {
            for (j = 0; j < n; j++) {
                cin >> a[i][j];
            }
        }

        for (i = 0; i < m; i++) {
            for (j = 0; j < n && g == 0; j++) {
                if (!check_matrix(a, m, n, i, j)) {
                    cout << "Case #" << p+1 << ": " << "NO\n";
                    g = 1;
                    break;
                }
            }
        }
        if (g == 0) {
             cout << "Case #" << p + 1 << ": " << "YES\n";
        }
    }
    return 0;
}
