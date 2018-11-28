#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <cstdlib>
#include <vector>

using namespace std;

const int MAXN = 105 ;

int n, m ;
int _ ;
int ind[MAXN * MAXN] , outd[MAXN * MAXN] ;
char s[MAXN][MAXN] ;

int node(int x , int y){
    return x * m + y ;
}

int dx[] = {-1 , 0 , 1 , 0} ;
int dy[] = {0 , 1 , 0 , -1} ;

int col[MAXN] , row[MAXN] ;

bool out(int x,int y){
    return x < 0 || x >= n || y < 0 || y >= m ;
}

int main(){
    freopen("input.txt" , "r" , stdin) ;
    freopen("output.txt" , "w" , stdout) ;
    scanf("%d" , &_) ;
    for (int cas = 1 ; cas <= _ ; cas++){
        scanf("%d%d" , &n ,&m) ;
        for (int i = 0 ; i < n ; i++)
            scanf("%s" , s[i]) ;
        memset(ind,0,sizeof(ind)) ;
        memset(outd,0,sizeof(outd)) ;
        memset(col,0,sizeof(col)) ;
        memset(row,0,sizeof(row)) ;

        for (int i = 0 ; i < n ; i++)
            for (int j = 0 ; j < m ; j++)
                if (s[i][j] != '.'){
                row[i]++ ; col[j]++ ;
                int x = node(i,j) ;
                int k ;
                if (s[i][j] == '^') k = 0 ;
                if (s[i][j] == '>') k = 1 ;
                if (s[i][j] == 'v') k = 2 ;
                if (s[i][j] == '<') k = 3 ;
                int tx = i , ty = j ;
                do{
                    tx += dx[k] ; ty += dy[k] ;
                    if (out(tx,ty)) break ;
                    if (s[tx][ty] != '.'){
                        outd[node(i,j)]++ ;
                        ind[node(tx,ty)]++  ;
                        break ;
                    }
                }while (true) ;
            }
        bool imp = false ;
        int ans = 0 ;
        for (int i = 0 ; i < n ; i++)
            for (int j = 0 ; j < m ; j++)
            if (s[i][j] != '.'){
                if (col[j] == 1 && row[i] == 1) imp = true ;
                if (outd[node(i,j)] == 0) ans++ ;
        }
        printf("Case #%d: ",cas) ;
        if (imp) printf("IMPOSSIBLE\n");
        else printf("%d\n",ans) ;
    }
    return 0 ;
}
