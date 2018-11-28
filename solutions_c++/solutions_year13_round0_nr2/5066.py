#include <cstdio>
#include <cstring>
#include <iostream>

const int N = 100 + 1;

int n, m;
int height[N][N], row[N], column[N];

int main() {
    int test_count;
    scanf("%d", &test_count);
    for (int t = 1; t <= test_count; ++ t) {
        scanf("%d%d", &n, &m);
        memset(row, 0, sizeof(row));
        memset(column, 0, sizeof(column));
        for (int i = 0; i < n; ++ i) {
            for (int j = 0; j < m; ++ j) {
                scanf("%d", &height[i][j]);
                row[i] = std::max(row[i], height[i][j]);
                column[j] = std::max(column[j], height[i][j]);
            }
        }
        bool flag = true;
        for (int i = 0; i < n && flag; ++ i) {
            for (int j = 0; j < m && flag; ++ j) {
                if (row[i] > height[i][j] && column[j] > height[i][j]) {
                    flag = false;
                }
            }
        }
        printf("Case #%d: %s\n", t, flag ? "YES" : "NO");
    }
    return 0;
}
