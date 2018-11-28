#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int maxn  = 111 ;

char g[maxn][maxn];
int N , M ;
const int dx[] = {0 ,-1, 0 , 1} ;
const int dy[] = {1, 0, -1, 0} ;
int get_dir(char c) {
    if(c == '>') return 0 ;
    if(c == '^') return 1 ;
    if(c == '<') return 2 ;
    if(c == 'v') return 3 ;
    return -1 ;
}

bool check(int x ,int y , int dir) {
    while(1) {
        int nx = x + dx[dir] ;
        int ny = y + dy[dir];
        if(nx < 1 || nx>N || ny<1 || ny>M) break ;
        x = nx , y = ny ;
        if(get_dir(g[x][y]) != -1) return true ;
    }
    return false ;
}



int main()
{
    freopen("A-large.in", "r" ,stdin) ;
    freopen("large.txt", "w", stdout) ;


    int T , cas = 1;
    scanf("%d", &T) ;
    while(T--) {
        scanf("%d%d", &N, &M) ;
        for(int i=1; i<=N; i++) scanf("%s", g[i]+1) ;
        bool flag = true ;
        int ans = 0 ;
        for(int x=1; x<=N; x++) {
            for(int y=1; y<=M; y++) {
                int dir = get_dir(g[x][y]) ;
                if(dir != -1) {
                    if(check(x , y , dir)) continue ;
                    bool tmp = false ;
                    for(int d=0; d<4; d++) {
                        if(d == dir) continue ;
                        if(check(x , y , d)) {
                            tmp = true;
                            break ;
                        }
                    }
                    if(tmp) ans ++ ;
                    else {
                        flag = false ;
                        break ;
                    }
                }
            }
        }

        printf("Case #%d: " , cas++) ;
        if(flag) printf("%d\n" , ans) ;
        else puts("IMPOSSIBLE");
    }
    return 0;
}
