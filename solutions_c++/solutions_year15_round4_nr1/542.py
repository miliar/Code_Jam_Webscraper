const int MAXN = 200 ;

const char DC[5] = ">v^<" ;

const int DIR[4][2] = {
    {0, 1} ,
    {1, 0} ,
    {-1, 0} ,
    {0, -1}
} ;

#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std ;

#define fo(i,a,b) for(int i = a; i <= b; i ++ )

int N , M ;
char Map[MAXN][MAXN] ;

void Init() { fo(i,0,N-1) cin >> Map[i] ; }
void Solve() {
    int ans = 0 ;
    fo(i,0,N-1) fo(j,0,M-1) if ( Map[i][j] != '.' ) {
        int x , y , dx , dy ;
        bool pan ;
        fo(k,0,3) if ( DC[k] == Map[i][j] ) dx = DIR[k][0] , dy = DIR[k][1] ;
        for ( x = i+dx , y = j+dy , pan = false ; 0 <= x && x < N && 0 <= y && y < M ; x += dx , y += dy )
            if ( Map[x][y] != '.' ) { pan = true ; break ; }
        if ( pan ) continue ;
        fo(k,0,3) {
            dx = DIR[k][0] ; dy = DIR[k][1] ; x = i + dx ; y = j + dy ;
            for ( ; 0 <= x && x < N && 0 <= y && y < M ; x += dx , y += dy )
                if ( Map[x][y] != '.' ) { pan = true ; break ; }
        }
        if ( pan ) ans ++ ;
        else { cout << "IMPOSSIBLE\n" ; return ; }
    }
    cout << ans << "\n" ;
}


int main() {
    //freopen("A.in" , "r" , stdin) ; freopen("A.out" , "w" , stdout) ;
    //freopen("A-small-attempt0.in" , "r" , stdin) ; freopen("A-small-attempt0.out" , "w" , stdout) ;
    freopen("A-large.in" , "r" , stdin) ; freopen("A-large.out" , "w" , stdout) ;
    int Test ; cin >> Test ;
    for ( int i = 1 ; i <= Test ; i ++ ) {
        cin >> N >> M ;
        Init() ;
        cout << "Case #" << i << ": " ;
        Solve() ;
    }
}
