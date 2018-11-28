#include <cstdio>
#include <cstring>

using namespace std;

const int MAXN = 510;

int n, m, k;
int a[MAXN][MAXN];
int bio[MAXN][MAXN];

int dx[] = { -1, 0, 1, 0 };
int dy[] = { 0, 1, 0, -1 };

int rec (int x, int y, int dir) {
    if (a[y][x]) return 0;
    if (bio[y][x]) return 0;
    bio[y][x] = 1;

    if (y == n - 1) return 1;

    for (int i = (dir + 3) % 4, j = 0; j < 3; ++j, i = (i + 1) % 4) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (nx < 0 || ny < 0 || nx >= m || ny >= n) continue;
        if (rec(nx, ny, i)) return 1;
    }

    return 0;
}

void solve ()
{
    memset (a, 0, sizeof a);
    memset (bio, 0, sizeof bio);

    scanf ("%d%d%d", &m, &n, &k);

    for (int i = 0; i < k; ++i) {
        int x1, y1, x2, y2;
        scanf ("%d%d%d%d", &x1, &y1, &x2, &y2);
        for (int ii = y1; ii <= y2; ++ii)
            for (int jj = x1; jj <= x2; ++jj)
                a[ii][jj] = 1;
    }

    int ans = 0;
    for (int i = 0; i < m; ++i) {
        ans += rec(i, 0, 1);
        /*       printf ("\n");
                 for (int i = 0; i < n; ++i, printf ("\n"))
                 for (int j = 0; j < m; ++j) printf ("%d", bio[i][j]);*/
    }

    printf ("%d\n", ans);
}

int main (int argc, char *argv[])
{
    int No; scanf ("%d", &No);
    for (int i = 0; i < No; ++i) {
        if (argc == 1) printf ("Case #%d: ", i + 1);
        solve();
    }

    return 0;
}


