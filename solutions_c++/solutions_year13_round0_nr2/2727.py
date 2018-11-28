#include <iostream>
#include <cstdio>
using namespace std;

int a[111][111];
int m, n;

bool check() {
    for(int i = 1; i <= m; ++i)
        for(int j = 1; j <= n; ++j) {
            int maxRow = -1, maxCol = -1;
            for(int ii = 1; ii <= m; ++ii)
                maxRow = max(maxRow, a[ii][j]);

            for(int jj = 1; jj <= n; ++jj)
                maxCol = max(maxCol, a[i][jj]);

            if (a[i][j] != min(maxRow, maxCol))
                return false;
        }
    return true;
}

int main() {
    freopen("B.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int ntest; cin >> ntest;
    for(int test = 0; test < ntest; ++test) {
        cin >> m >> n;
        for(int i = 1; i <= m; ++i)
            for(int j = 1; j <= n; ++j)
                cin >> a[i][j];
        cout << "Case #" << test+1 << ": ";
        if (check()) cout << "YES";
        else cout << "NO";
        cout << endl;
    }
}
