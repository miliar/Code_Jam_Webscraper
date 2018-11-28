#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int main(void) {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n, m, a[110][110], maxrow[110], maxcol[110], t, i, j, T;

    scanf("%d", &T);

    for (t=1; t<=T; ++t) {
        printf("Case #%d: ", t);

        memset(maxrow, 0, sizeof(maxrow));
        memset(maxcol, 0, sizeof(maxcol));

        scanf("%d %d", &n, &m);
        for (i=0; i<n; ++i) {
            for (j=0; j<m; ++j) {
                scanf("%d", &a[i][j]);
                maxrow[i] = max(maxrow[i], a[i][j]);
                maxcol[j] = max(maxcol[j], a[i][j]);
            }
        }

        for (i=0; i<n; ++i) for (j=0; j<m; ++j)
            if ( maxrow[i] > a[i][j] && maxcol[j] > a[i][j] ) goto s;

        printf("YES\n"); continue;
s:
        printf("NO\n");
    }

    return 0;
}
