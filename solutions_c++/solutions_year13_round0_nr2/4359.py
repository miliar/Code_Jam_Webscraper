#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>

using namespace std;
const int maxn = 128;

int T, n, m;
int grass[maxn][maxn];
int row_max[maxn], col_max[maxn];

int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};

void read() {
    cin >> n >> m;
    for (int i = 0; i < n; ++ i)
        for (int j = 0; j < m; ++ j)
            cin >> grass[i][j];
}

bool solve() {
    for (int row = 0; row < n; ++ row) {
        row_max[row] = 0;
        for (int col = 0; col < m; ++ col)
            row_max[row] = max(row_max[row], grass[row][col]);
    }
    for (int col = 0; col < m; ++ col) {
        col_max[col] = 0;
        for (int row = 0; row < n; ++ row)
            col_max[col] = max(col_max[col], grass[row][col]);
    }
    for (int row = 0; row < n; ++ row)
        for (int col = 0; col < m; ++ col) {
            if (grass[row][col] < row_max[row] && grass[row][col] < col_max[col])
                return false;
        }
    return true;
}

int main() {
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    cin >> T;
    for (int i = 1; i <= T; ++ i) {
        read();
        cout << "Case #" << i << ": " << (solve() ? "YES" : "NO") << endl;
    }
    return 0;
}
