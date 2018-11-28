#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;

int T,R,C;
char g[110][110];
int vis[110][110];
int dir[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
int prex,prey,edx,edy;
int flag;

char DR[4] = {'^','v','<','>'};
int gg[110][110];

int main(){
    freopen("A-small-attempt5.in","r",stdin);
    freopen("A.txt","w",stdout);
    scanf("%d",&T);
    for(int tt = 1; tt <= T; ++tt){
        scanf("%d%d",&R,&C);
        memset(vis,0,sizeof(vis));
        for(int i = 1; i <= R; ++i){
            scanf("%s",g[i] + 1);
        }
        int ans = 0;
        for(int j = 1; j <= C; ++j){
            if(g[1][j] == '^'){
                g[1][j] = 'v';
                ans++;
            }
            if(g[1][j] == '.'){
                for(int i = 1; i <= R; ++i) if(g[i][j] != '.'){
                    g[i][j] = 'v';
                    ans++;
                    break;
                }
            }
        }
        for(int j = 1; j <= C; ++j){
            if(g[R][j] == 'v'){
                g[R][j] = '^';
                ans++;
            }
            if(g[R][j] == '.'){
                for(int i = R; i >= 1; --i) if(g[i][j] != '.'){
                    g[i][j] = '^';
                    ans++;
                    break;
                }
            }
        }
        for(int i = 1; i <= R; ++i){
            if(g[i][1] == '<'){
                g[i][1] = '>';
                ans++;
            }
            if(g[i][1] == '.'){
                for(int j = 1; j <= C; ++j) if(g[i][j] != '.'){
                    g[i][j] = '>';
                    ans++;
                    break;
                }
            }
            if(g[i][C] == '>'){
                g[i][C] = '<';
                ans++;
            }
            if(g[i][C] == '.'){
                for(int j = C; j >= 1; --j) if(g[i][j] != '.'){
                    g[i][j] = '<';
                    ans++;
                    break;
                }
            }
        }
        //======================
        int flag = 1;
        for(int j = 1; j <= C; ++j){
            if(g[1][j] == '.'){
                for(int i = 1; i <= R; ++i) if(g[i][j] != '.'){
                    if(g[i][j] == '^'){
                        flag = 0;
                        break;
                    }
                }
            }
        }
        for(int j = 1; j <= C; ++j){
            if(g[R][j] == '.'){
                for(int i = R; i >= 1; --i) if(g[i][j] != '.'){
                    if(g[i][j] == 'v'){
                        flag = 0;
                        break;
                    }
                }
            }
        }
        for(int i = 1; i <= R; ++i){
            if(g[i][1] == '.'){
                for(int j = 1; j <= C; ++j) if(g[i][j] != '.'){
                    if(g[i][j] == '<'){
                        flag = 0;
                        break;
                    }
                }
            }
            if(g[i][C] == '.'){
                for(int j = C; j >= 1; --j) if(g[i][j] != '.'){
                    if(g[i][j] == '>'){
                        flag = 0;
                        break;
                    }
                }
            }
        }
        printf("Case #%d: ",tt);
        if(flag == 0) printf("IMPOSSIBLE\n");
        else{
            printf("%d\n",ans);
        }
    }
    return 0;
}
