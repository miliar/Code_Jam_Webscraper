#include <stdio.h>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
#include <queue>
#include <map>

using namespace std;

#define MAXN 100010

#define INF 1e20
#define eps 1e-8
#define mod 998244353

int T;

int R, C;

char bx[110][110];
bool vis[110][110];

bool can(int x, int y, char w) {
    if(w == '^') {
        for(int i = x - 1; i >= 1; i--) {
            if(bx[i][y] != '.') return true;
        }
        return false;
    } else if(w == '<') {
        for(int j = y - 1; j >= 1; j--) {
            if(bx[x][j] != '.') return true;
        }
        return false;
    } else if(w == '>') {
        for(int j = y + 1; j <= C; j++) {
            if(bx[x][j] != '.') return true;
        }
        return false;
    } else if(w == 'v') {
        for(int i = x + 1; i <= R; i++) {
            if(bx[i][y] != '.') return true;
        }
        return false;
    }
}

int main()
{
    freopen("pro.in","r",stdin);
    freopen("pro.out","w",stdout);

    scanf("%d", &T);
    int cas = 1;

    while(T--) {
        printf("Case #%d: ", cas++);
        int ans = 0;
        scanf("%d%d", &R, &C);
        for(int i = 1; i <= R; i++) {
            scanf("%s", bx[i] + 1);
        }

        memset(vis,0,sizeof(vis));

        bool fal = 1;

        for(int i = 1; i <= R; i++) {
            int bj = -1;
            for(int j = 1; j <= C; j++) {
                if(bx[i][j] != '.') {
                    bj = j; break;
                }
            }
            if(bj != -1) {
                if(!can(i, bj, bx[i][bj]) && !vis[i][bj]) {
                    vis[i][bj] = 1;
                    bool fd = 0;
                    if(can(i, bj, '^')) {
                        ans++; 
                        fd = 1;
                    } else if(can(i, bj, '>')) {
                        ans++;
                        fd = 1;
                    } else if(can(i, bj, 'v')) {
                        ans++;
                        fd = 1;
                    }
                    if(!fd) {
                        fal = 0;
                        break;
                    }
                }
            }

            

            bj = -1;
            for(int j = C; j >= 1; j--) {
                if(bx[i][j] != '.') {
                    bj = j; break;
                }
            }
            if(bj != -1) {
                if(!can(i, bj, bx[i][bj]) && !vis[i][bj]) {
                    bool fd = 0;
                    vis[i][bj] = 1;
                    if(can(i, bj, '^')) {
                        ans++; 
                        fd = 1;
                    } else if(can(i, bj, '<')) {
                        ans++;
                        fd = 1;
                    } else if(can(i, bj, 'v')) {
                        ans++;
                        fd = 1;
                    }
                    if(!fd) {
                        fal = 0;
                        break;
                    }
                }
                
            }

            
        }

        if(!fal) {
            printf("IMPOSSIBLE\n");
            continue;
        }

        for(int j = 1; j <= C; j++) {
            int bj = -1;
            for(int i = 1; i <= R; i++) {
                if(bx[i][j] != '.') {
                    bj = i; break;
                }
            }
            if(bj != -1) {
                if(!can(bj, j, bx[bj][j]) && !vis[bj][j]) {
                    bool fd = 0;
                    vis[bj][j] = 1;
                    if(can(bj, j, '<')) {
                        ans++; 
                        fd = 1;
                    } else if(can(bj, j, '>')) {
                        ans++;
                        fd = 1;
                    } else if(can(bj, j, 'v')) {
                        ans++;
                        fd = 1;
                    }
                    if(!fd) {
                        fal = 0;
                        break;
                    }
                }
            }

            

            bj = -1;
            for(int i = R; i >= 1; i--) {
                if(bx[i][j] != '.') {
                    bj = i; break;
                }
            }
            if(bj != -1) {
                if(!can(bj, j, bx[bj][j]) && !vis[bj][j]) {
                    bool fd = 0;
                    vis[bj][j] = 1;
                    if(can(bj, j, '>')) {
                        ans++; 
                        fd = 1;
                    } else if(can(bj, j, '<')) {
                        ans++;
                        fd = 1;
                    } else if(can(bj, j, '^')) {
                        ans++;
                        fd = 1;
                    }
                    if(!fd) {
                        fal = 0;
                        break;
                    }
                }
            }
        }

        if(!fal) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%d\n", ans);
        }
    }
    return 0;
}
