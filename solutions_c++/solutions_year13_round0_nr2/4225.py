#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

#define MAXN 109

const int dx[4] = {0, 1, 0, -1};
const int dy[4] = {-1, 0, 1, 0};

int a[MAXN][MAXN];
bool open[MAXN][MAXN];

int T, N, M, i, j, h;

bool ok(int x, int y) {
    return x >= 0 && x < M && y >= 0 && y < N;
}

int cnt(int x, int y, int dir, int res = 0) {
    open[x][y] = true;
    if (!( ok(x+dx[dir], y+dy[dir]) && ( a[x+dx[dir]][y+dy[dir]] == h || open[x+dx[dir]][y+dy[dir]] ) ))
        return res;
    else
        return cnt(x + dx[dir], y + dy[dir], dir, res + 1);
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output2.txt", "w", stdout);
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        memset(open, false, sizeof(open));
        bool fail = false;
        cin >> N >> M;
        for (j = 0; j < N; j++) {
            for (i = 0; i < M; i++) {
                scanf("%d", &a[i][j]);
                //printf("%d ", a[i][j]);
            }
            //printf("\n");
        }

        for (h = 1; h <= 100; h++) {
            for (i = 0; i < M; i++)
            for (j = 0; j < N; j++)
            if (a[i][j] == h) {
                int c[4];
                for (int k = 0; k < 4; k++)
                    c[k] = cnt(i, j, k);
                if (c[0] + c[2] + 1 < N && c[1] + c[3] + 1 < M) {
                    fail = true;
                    //cout << "FAIL on " << h << endl;
                }
            }
        }

        cout << "Case #" << tc << ": " << ((fail) ? "NO" : "YES") << endl;
    }
}
