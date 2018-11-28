#include <cstdio>
#include <algorithm>
using namespace std;

int n, m, a[110][110];
int maxr[110], maxc[110];
int b[110][110];

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d %d", &n, &m);
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                scanf("%d", &a[i][j]);
        for (int i = 0; i < n; i++) {
            maxr[i] = a[i][0];
            for (int j = 1; j < m; j++)
                maxr[i] = max(maxr[i], a[i][j]);
        }
        for (int j = 0; j < m; j++) {
            maxc[j] = a[0][j];
            for (int i = 1; i < n; i++)
                maxc[j] = max(maxc[j], a[i][j]);
        }
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                b[i][j] = min(100, min(maxr[i], maxc[j]));
        bool ans = 1;
        for (int i = 0; ans && i < n; i++)
            for (int j = 0; ans && j < m; j++)
                ans = a[i][j] == b[i][j];
        printf("Case #%d: %s\n", t, ans ? "YES" : "NO");
    }
}
