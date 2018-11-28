#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

const int MAXN = 110;
int n, m;
int sp[MAXN][MAXN], tg[MAXN][MAXN], col_max[MAXN], row_max[MAXN];

int main()
{
    int T, cas = 1;
	freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%d", &T);
    while(T--){
        memset(col_max, 0, sizeof(col_max));
        memset(row_max, 0, sizeof(row_max));
        scanf("%d %d", &n, &m);
        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++){
                scanf("%d", &sp[i][j]);
                tg[i][j] = 100;
                col_max[j] = max(col_max[j], sp[i][j]);
                row_max[i] = max(row_max[i], sp[i][j]);
			}
        int ok = 1;
        for(int i = 0; i < n && ok; i++)
            for(int j = 0; j < m && ok; j++){
                tg[i][j] = min(row_max[i], col_max[j]);
			    if(tg[i][j] != sp[i][j])
                    ok = 0;
			}
        printf("Case #%d: ", cas++);
        if(ok)puts("YES");
		else puts("NO");
	}
    return 0;
}