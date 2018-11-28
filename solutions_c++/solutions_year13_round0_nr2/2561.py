#include <cstdio>
#include <cstring>
#include <string>
using namespace std;
const int MAXN = 105;

int t, i, j, t_case, max_line[MAXN], max_col[MAXN], a[MAXN][MAXN];
int n, m;

int main()  {

    freopen("lawn.in","r",stdin);
    freopen("lawn.out","w",stdout);
    
    scanf("%d",&t);

    for(t_case = 1; t_case <= t; ++t_case) {

        scanf("%d %d",&n,&m);
        string answer = "YES";

        memset(max_line, 0, sizeof(max_line));
        memset(max_col, 0, sizeof(max_col));

        for(i = 1; i <= n; ++i)
            for(j = 1; j <= m; ++j) {
                scanf("%d",&a[i][j]);
                max_line[i] = max(max_line[i], a[i][j]);
                max_col[j] = max(max_col[j], a[i][j]);
            }

        for(i = 1; i <= n; ++i)
            for(j = 1; j <= m; ++j)
                if(a[i][j] < max_line[i] && a[i][j] < max_col[j])
                    answer = "NO";

        printf("Case #%d: %s\n", t_case, answer.c_str());
    }

    return 0;
}
