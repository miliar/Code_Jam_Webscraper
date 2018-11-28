#include <iostream>
#include <algorithm>

using namespace std;

int n, m;
int a[101][101];
int step() {
    
    int ii = -1, jj = -1;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (a[i][j] != -1) {
                if (ii == -1 || a[i][j] < a[ii][jj]) {
                    ii = i; jj = j;
                }
            }
        }
    }
    if (ii == -1)
        return -1;
    bool ok = true;
    int ret = 0;
    for (int i = 0; i < n; ++i) {
        if (a[i][jj] > a[ii][jj])
            ok = false;
    }
    if (ok) {
        ret = 1;
        for (int i = 0; i < n; ++i)
            a[i][jj] = -1;
    }
    ok = true;
    for (int j = 0; j < m; ++j) {
        if (a[ii][j] > a[ii][jj])
            ok = false;
    }
    if (ok) {
        ret = 1;
        for (int j = 0; j < m; ++j)
            a[ii][j] = -1;
    }
    return ret;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> n >> m;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                cin >> a[i][j];
        bool res = true;
        while (1) {
            int s = step();
            if (s == -1)
                break;
            if (s == 0) {
                res = false;
                break;
            }
        }
        cout << "Case #" << t << ": ";
        if (res)
            cout << "YES\n";
        else
            cout << "NO\n";
    }
    
    return 0;
}