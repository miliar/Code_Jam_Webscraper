#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

const int N = 200;

int T, n, m, a[N][N], dx[4] = {-1, 0, 1, 0}, dy[4] = {0, -1, 0, 1};
char str[N][N];
bool vis[N][N], mark[N][N];
pair <int, int> d[N][N][5];

void work() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            vis[i][j] = mark[i][j] = false;
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (str[i][j] == '.') {
                continue;
            }
            if (str[i][j] == '^') {
                a[i][j] = 0;
            }
            if (str[i][j] == '<') {
                a[i][j] = 1;
            }
            if (str[i][j] == 'v') {
                a[i][j] = 2;
            }
            if (str[i][j] == '>') {
                a[i][j] = 3;
            }
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (str[i][j] == '.') {
                continue;
            }
            bool flag = false;
            for (int k = 0; k < 4; k++) {
                int ii = i;
                int jj = j;
                while (true) {
                    ii += dx[k];
                    jj += dy[k];
                    if (ii < 0 || ii >= n || jj < 0 || jj >= m || str[ii][jj] != '.') {
                        flag |= (ii >= 0 && ii < n && jj >= 0 && jj < m);
                        d[i][j][k] = make_pair(ii, jj);
                        break;
                    }
                }
            }
            if (!flag) {
                printf("IMPOSSIBLE\n");
                return;
            }
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (str[i][j] == '.' || vis[i][j]) {
                continue;
            }
            int ii = i;
            int jj = j;
            int kk = a[i][j];
            vis[ii][jj] = true;
            while (true) {
                pair <int, int> t = d[ii][jj][kk];
                if (t.first < 0 || t.first >= n || t.second < 0 || t.second >= m) {
                    mark[ii][jj] = true;
                    break;
                }
                if (vis[t.first][t.second]) {
                    break;
                }
                ii = t.first;
                jj = t.second;
                kk = a[ii][jj];
                vis[ii][jj] = true;
            }
        }
    }
    int ret = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (mark[i][j]) {
                ++ret;
            }
        }
    }
    printf("%d\n", ret);
}

int main() {

    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    scanf("%d", &T);

    for (int t = 1; t <= T; t++) {
        scanf("%d %d", &n, &m);
        for (int i = 0; i < n; i++) {
            scanf("%s", str[i]);
        }
        printf("Case #%d: ", t);
        work();
    }

    return 0;

}
