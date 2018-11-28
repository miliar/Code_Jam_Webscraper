#include <iostream>
#include <cstdio>

using namespace std;

int check1(int b[110][110], int m, int n, int w, int z) {
    int s = b[w][z];
    int flbg = 1;
    for (int i = 0; i < n; i++) {
        if (b[w][i] > s) {
            flbg = 0;
            break;
        }
    }

    if (flbg == 0) {
        for (int j = 0; j < m; j++) {
            if (b[j][z] > s) {
                return 0;
            }
        }
    }

    return 1;
}
int main ( ) {
    int b[110][110], t, k = 0, m, n, tog;
    scanf ("%d", &t);
    while (t--) {
        k++;
        tog = 0;
        scanf ("%d%d" , &m, &n);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                cin >> b[i][j];
                }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n && tog == 0; j++) {
                if (!check1(b, m, n, i, j)) {
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
