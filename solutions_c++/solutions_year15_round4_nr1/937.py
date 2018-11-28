#include <iostream>
#include <cstdio>
#include <cmath>
#include <memory.h>

using namespace std;

bool a1[105][105], a2[105][105], a3[105][105], a4[105][105];
char a[105][105];

int main() {
    freopen("A-large(1).in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        memset(a1, 0, sizeof(a1));
        memset(a2, 0, sizeof(a2));
        memset(a3, 0, sizeof(a3));
        memset(a4, 0, sizeof(a4));
        int n, m;
        cin >> n >> m;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                cin >> a[i][j];
        for (int i = 0; i < n; ++i)
            for (int j = 1; j < m; ++j)
                if (a1[i][j - 1] || a[i][j - 1] != '.')
                    a1[i][j] = true;
        for (int i = 0; i < n; ++i)
            for (int j = m - 2; j > -1; --j)
                if (a2[i][j + 1] || a[i][j + 1] != '.')
                    a2[i][j] = true;
        for (int j = 0; j < m; ++j)
            for (int i = 1; i < n; ++i)
                if (a3[i - 1][j] || a[i - 1][j] != '.')
                    a3[i][j] = true;
        for (int j = 0; j < m; ++j)
            for (int i = n - 2; i > -1; --i)
                if (a4[i + 1][j] || a[i + 1][j] != '.')
                    a4[i][j] = true;
        int ans = 0;
        int fl = 0;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j) {
                if (a[i][j] != '.' && !a1[i][j] && !a2[i][j] && !a3[i][j] && !a4[i][j] && fl == 0) {
                    cout << "Case #" << t + 1 << ": " << "IMPOSSIBLE" << "\n";
                    fl = 1;
                } else {
                    if (a[i][j] == '.') continue;
                    if (a1[i][j] && a[i][j] == '<') continue;
                    if (a2[i][j] && a[i][j] == '>') continue;
                    if (a3[i][j] && a[i][j] == '^') continue;
                    if (a4[i][j] && a[i][j] == 'v') continue;
                    ++ans;
                }
        }
        if (fl == 0)
            cout << "Case #" << t + 1 << ": " << ans << "\n";
    }
    return 0;
}
