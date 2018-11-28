#include<cstdio>
#include<vector>
#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;
int n, m, t, g[100][100];
bool di, p[101][2][100][100];
int main(){
    scanf("%d", &t);
    for(int tc = 1; tc <= t; ++tc){
        memset(p, 0, sizeof(p));
        scanf("%d %d", &n, &m);
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < m; ++j){
                scanf("%d", &g[i][j]);
                p[g[i][j]][0][i][j]=p[g[i][j]][1][j][i]=true;
            }
        }
        di = false;
        for(int h = 1; h <= 100 && !di;){
            //system("pause");
            //printf("%d:\n", h);
            bool nope = false, havestuff = false, skip=false;
            int id = -1;
            for(int i = 0; i < n; ++i){
                nope = false;bool hvstf = false;
                for(int j = 0; j < m && !nope; ++j){
                    if(g[i][j] != -1 && !p[h][0][i][j]){
                        nope = true;
                        //printf("%d, %d: (%d, %d)\n", i, j, g[i][j], p[h][0][i][j]);
                    }
                    if(g[i][j] != -1 && p[h][0][i][j]) havestuff = hvstf = true;
                }
                if(!nope&&hvstf){
                    for(int j = 0; j < m; j++) g[i][j] = -1;
                    skip = true;
            //printf("skipped row at %d\n", i);
                    break;
                }
            }
            //printf("have stuff? %d\n", havestuff);
            if(skip) continue;
            for(int i = 0; i < m; ++i){
                nope = false;bool hvstf = false;
                for(int j = 0; j < n; ++j){
                    if(g[j][i] != -1 && !p[h][1][i][j]) nope = true;
                    if(g[j][i] != -1 && p[h][1][i][j]) havestuff = hvstf = true;
                }
                if(!nope&&hvstf){
                    for(int j = 0; j < n; j++) g[j][i] = -1;
                    skip = true;
                //printf("skipped col at %d\n", i);
                    break;
                }
            }
            //printf("have stuff? %d\n", havestuff);
            if(skip) continue;
            if(havestuff) di = true;
            else ++h;
            //printf("di is %d\n", di);
        }
        if(!di) printf("Case #%d: YES\n", tc);
        else printf("Case #%d: NO\n", tc);
    }
    //system("pause");
}
