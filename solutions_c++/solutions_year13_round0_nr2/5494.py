#include <iostream>
#include <cstdio>

using namespace std;

int check(int a[105][105], int m, int n, int p, int q) {
    int s = a[p][q];
    int flag = 1;
    for (int i = 0; i < n; i++) {
        if (a[p][i] > s) {
            flag = 0;
            break;
        }
    }

    if (flag == 0) {
        for (int j = 0; j < m; j++) {
            if (a[j][q] > s) {
                return 0;
            }
        }
    }

    return 1;
}
int main ( ) {
    int a[105][105], t, k = 0, m, n, tog;
    scanf ("%d", &t);
    while (t--) {
        k++;
        tog = 0;
        scanf ("%d%d" , &m, &n);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                cin >> a[i][j];
                }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n && tog == 0; j++) {
                if (!check(a, m, n, i, j)) {
                    cout << "Case #" << k << ": " << "NO\n";
                    tog = 1;
                    break;
                }
            }
        }
        if (tog == 0) {
             cout << "Case #" << k << ": " << "YES\n";
        }
    }
    return 0;
}
