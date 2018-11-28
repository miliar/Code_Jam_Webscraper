#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

int map[110][110];
int row[110], col[110];
int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int T, Case = 1;
    scanf("%d",&T);
    while(T--){
        memset(row, 0, sizeof(row));
        memset(col, 0, sizeof(col));
        int n, m;
        scanf("%d%d", &n, &m);
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < m; ++j) scanf("%d", &map[i][j]);
        }
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < m; ++j) row[i] = max(row[i], map[i][j]);
        }
        for(int i = 0; i < m; ++i) {
            for(int j = 0; j < n; j++) col[i] = max(col[i], map[j][i]);
        }
        int flag = 0;
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < m; ++j) {
                int zzz = min(row[i], col[j]);
                if( zzz != map[i][j] ) flag = 1;
            }
        }
        printf("Case #%d: ",Case++);
        if(flag == 0) printf("YES\n");
        else printf("NO\n");
    }

    return 0;
}
