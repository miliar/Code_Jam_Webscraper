#include <cstdio>
#include <cstring>

using namespace std ;

const int MAXN = 50 + 5 ;
int res[MAXN] ;

bool dfs( int row , int max_row , int mine , int R , int C ) {
    if( row == R ) {
        if( row == 1 ) {
            res[row] = mine ; return true ;
        }
        if( mine % 2 == 0 && mine <= max_row * 2 ) {
            res[row-1] = res[row] = mine / 2 ;
            if( res[row] == C - 1 && C != 1 ) return false ;
            return true ;
        }
        return false ;
    }
    if( row == R - 1 ) return dfs( row + 1 , max_row , mine , R , C ) ;
    if( max_row * ( R - row + 1 ) < mine ) return false ;
    for( int col = 0 ; col <= max_row && col <= mine ; col ++ ) if( col != C - 1 || C == 1 ) {
        res[row] = col ;
        if( dfs( row + 1 , col , mine - col , R , C ) ) return true ;
    }
    return false ;
}

void display( int R , int C ) {
    for( int i = R ; i > 0 ; i -- ) {
        int num1 = C - res[i] , num2 = res[i] ;
        if( i == R ) { num1 -- ; putchar('c') ; }
        for( int j = 0 ; j < num1 ; j ++ ) putchar('.') ;
        for( int j = 0 ; j < num2 ; j ++ ) putchar('*') ;
        putchar('\n') ;
    }
}

int main() {

    freopen("C-large.in","r",stdin) ;
    freopen("C.out","w",stdout) ;

    int step = 0 ;
    int T ; scanf("%d" , &T ) ;
    while( T -- ) {
        memset( res , 0 , sizeof( res ) ) ;
        int R , C , M ; scanf("%d%d%d" , &R , &C , &M ) ;
        printf("Case #%d:\n" , ++ step ) ;
        bool ok = true ;
        if( M == 0 ) {
            for( int i = 1 ; i <= R ; i ++ ) res[i] = 0 ;
        }
        else if( M == R * C - 1 || M == 0 ) {
            for( int i = 1 ; i < R ; i ++ ) res[i] = C ;
            res[R] = C - 1 ;
        }
        else {
            if( !dfs( 1 , C , M , R , C ) ) ok = false ;
        }

        if( ok ) display( R , C ) ;
        else printf("Impossible\n") ;

    }

    return 0 ;
}
