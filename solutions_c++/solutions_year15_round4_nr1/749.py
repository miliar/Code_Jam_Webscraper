#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
#include <algorithm>

using namespace std;
const int Mn = 100 + 10;
int map[Mn][Mn];
int r,c;
#define U 1
#define D 2
#define L 3
#define R 4
#define B 0
int dx[] = {0,-1, 1, 0, 0};
int dy[] = {0, 0, 0,-1, 1};
inline bool inrange(int x,int y) {
    return x >= 1 && x <= r && y >= 1 && y <= c;
}
inline bool exist(int x, int y, int dir) {
     for(int i = 1;inrange(x + i * dx[dir], y + i * dy[dir]); ++i) {
        int tx = x + i * dx[dir];
        int ty = y + i * dy[dir];
        if(map[tx][ty]) 
            return true;
    }
    return false;
}
inline int check(int x, int y) {
   if(exist(x, y, map[x][y]))
        return 0;
    int tot(0);
    for(int i = 1; i <= 4; ++i)
        tot += exist(x,y,i);
    if(!tot)
        return -1;
    return 1;
}
int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++cas) {

        scanf("%d%d",&r,&c);
        for(int i = 1; i <= r; ++i) {
            char s[Mn];
            scanf("%s",s + 1);
            for(int j = 1; s[j]; ++j) {
                if(s[j] == '.') {
                    map[i][j] = B;    
                } else if(s[j] == '^') {
                    map[i][j] = U;    
                } else if(s[j] == 'v') {
                    map[i][j] = D;
                } else if(s[j] == '<') {
                    map[i][j] = L;
                } else if(s[j] == '>') {
                    map[i][j] = R;
                }
            }   
        }
        bool flag = true;
        int ans(0);
        for(int i = 1; i <= r && flag; ++i)
            for(int j = 1; j <= c && flag; ++j) {
                if(map[i][j] != B) {
                    int t = check(i,j);
                    if(t == -1) {
                        flag = false;
                    } else {
                        ans += t;
                    }
                }
            }
        if(!flag) {
            printf("Case #%d: IMPOSSIBLE\n",cas);
        } else {
            printf("Case #%d: %d\n",cas,ans);
        }
    }
    return 0;
}
