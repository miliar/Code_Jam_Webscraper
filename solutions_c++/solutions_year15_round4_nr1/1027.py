#include <bits/stdc++.h>
using namespace std;
const int N = 104;
char Map[N][N];
int in[N][N], out[N][N];
int cntrow[N], cntcol[N];
int gox[4] = {0, 0, -1, 1};
int goy[4] = {-1, 1, 0, 0};
int main(){
freopen("in1.in", "r", stdin);
    freopen("out1.out", "w" , stdout);
    int TC, tc, i, j, n, m, x, y;
    scanf("%d", &TC);
    for(tc = 1; tc <= TC; tc ++){
        scanf("%d%d", &n, &m);
        for(i = 1; i <= n; i++){
            scanf("%s", Map[i]+1);
        }
        memset(in, 0, sizeof(in));
        memset(out, 0, sizeof(out));
        memset(cntcol, 0, sizeof(cntcol));
        memset(cntrow, 0, sizeof(cntrow));
        int dir;
        for(i = 1; i <= n; i++){
            for(j = 1; j <= m; j++){
                if(Map[i][j] == '.')    continue;
                cntcol[j] ++;
                cntrow[i] ++;
                if(Map[i][j] == '^'){
                    dir = 2;
                }
                else if(Map[i][j] == 'v'){
                    dir = 3;
                }else if(Map[i][j] =='>') {
                    dir = 1;
                }else dir = 0;
                x = i + gox[dir];
                y = j + goy[dir];
                while(x && y && x <= n && y <= m){
                    if(Map[x][y] != '.'){
                        out[i][j] ++;
                        in[x][y] ++;
                        break;
                    }
                    x += gox[dir];
                    y += goy[dir];
                }
            }
        }
        bool gg = false;
        int ans = 0;

        for(i = 1; i <= n && !gg; i++){
            for(j = 1; j <= m; j++){
                if(Map[i][j] == '.')    continue;
                if(!out[i][j] && !in[i][j] && (cntrow[i]==1&&cntcol[j] == 1)){
                    gg = true;
                    break;
                }
                if(out[i][j] == 0)  ans ++;
            }
        }
        printf("Case #%d: ", tc);
        if(gg){
            printf("IMPOSSIBLE\n");
        }else printf("%d\n", ans);

    }
    return 0;
}
