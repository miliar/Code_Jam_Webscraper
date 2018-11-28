#include <cstdio>
#include <algorithm>
using namespace std;

const int max_n = 100;
const int max_m = 100;
const int inf = 987654321;
int n, m, a[max_n][max_m];
int x[max_n], y[max_m];
int main()
{
    int T; scanf("%d", &T);
    for(int tt = 1; tt <= T; tt++)
    {
        scanf("%d %d", &n, &m);
        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++)
                scanf("%d", &a[i][j]);
        for(int i = 0; i < n; i++) x[i] = -inf;
        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++)
                x[i] = max(x[i], a[i][j]);
        for(int j = 0; j < m; j++) y[j] = -inf;
        for(int j = 0; j < m; j++)
            for(int i = 0; i < n; i++)
                y[j] = max(y[j], a[i][j]);
        bool ok = true;
        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++)
                if(a[i][j] != min(x[i], y[j]))
                    ok = false;
        printf("Case #%d: ", tt);
        if(ok) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
