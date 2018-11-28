    #include <cstdio>
#include<algorithm>

using namespace std;

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, casen = 0, n, m, x, y, maxx, count;
    int grid[101][101];
    bool mark[101][101];
    scanf("%d", &t);
    while (casen < t) {
        printf("Case #%d: ", ++casen);
        scanf("%d%d", &n, &m);
        count = n*m;
        for (x = 0; x < n; x++) for (y = 0; y < m; y++) {
            scanf("%d", grid[x]+y);
            mark[x][y] = 0;
        }
        for (x = 0; x < n; x++) {
            maxx = 0;
            for (y = 0; y < m; y++) maxx = max(maxx, grid[x][y]);
            for (y = 0; y < m; y++) if (grid[x][y] == maxx && !mark[x][y]) {
                mark[x][y] = 1;
                count--;
            }
        }
        for (x = 0; x < m; x++) {
            maxx = 0;
            for (y = 0; y < n; y++) maxx = max(maxx, grid[y][x]);
            for (y = 0; y < n; y++) if (grid[y][x] == maxx && !mark[y][x]) {
                mark[y][x] = 1;
                count--;
            }
        }
        printf("%s\n", count? "NO": "YES");
    }
    return 0;
}

