#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int p, q, n;
int dp[110][1010][210];
int bio[110][1010][210];
int g[110], h[110];
int cookie;

int rec (int x, int m, int y) {
    if (x == n) return 0;
    int &ref = dp[x][m][y];
    int &bio_ref = bio[x][m][y];

    if (bio_ref == cookie) return ref;
    bio_ref = cookie;
    ref = 0;

    if (m * p >= y)
        ref = g[x] + rec(x + 1, m - (y + p - 1) / p, h[x+1]);

    int nx = x;
    int ny = y - q;
    if (ny <= 0) {
        nx = x + 1;
        ny = h[x+1];
    }

    ref = max(ref, rec(nx, m + 1, ny));
    return ref;
}

void solve ()
{
    scanf ("%d%d%d", &p, &q, &n);

    for (int i = 0; i < n; ++i)
        scanf ("%d%d", h+i, g+i);

    ++cookie;
    printf ("%d\n", rec (0, 1, h[0]));
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


