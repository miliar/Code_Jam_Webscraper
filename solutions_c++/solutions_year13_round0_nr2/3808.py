#include <cstdio>

const int MAXN = 100;

int t[MAXN][MAXN];
int maxx[MAXN], maxy[MAXN];
int tests, n, m;

bool chk()
{
    for (int y=0; y<n; ++y) {
        for (int x=0; x<m; ++x) {
            if (t[x][y] < maxx[x] && t[x][y] < maxy[y]) return false;
        }
    }
    return true;
}

int main()
{
    scanf("%d", &tests);
    for (int ti=1; ti<=tests; ++ti) {
        scanf("%d%d", &n, &m);
        for (int i=0; i<MAXN; ++i) maxx[i] = maxy[i] = 0;
        for (int y=0; y<n; ++y) {
            for (int x=0; x<m; ++x) {
                scanf("%d", &t[x][y]);
                if (t[x][y] > maxx[x]) maxx[x] = t[x][y];
                if (t[x][y] > maxy[y]) maxy[y] = t[x][y];
            }
        }
        if (chk()) printf("Case #%d: YES\n", ti);
        else printf("Case #%d: NO\n", ti);
    }
}
