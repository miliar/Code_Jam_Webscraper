#include <set>
#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;
#define N 12
using namespace std;
int t , n , m , cs , ans , anscnt;
char c[ N ][ N ];
set<int> S[ N ];
typedef set<int>::iterator si;
struct node{
    char ctmp;
    node * nxt[ 26 ];
    node(){
        memset( nxt , 0 , sizeof( nxt ) );
    }
}*root;
void init(){
    scanf( "%d%d" , &n , &m );
    ans = 0; anscnt = 0;
    for( int i = 0 ; i < n ; i ++ )
        scanf( "%s" , c[ i ] );
}
void clean( node * now ){
    if( !now ) return;
    for( int i = 0 ; i < 26 ; i ++ )
        clean( now->nxt[ i ] );
    delete now;
}
void cal(){
    int tcnt = 0;
    for( int i = 1 ; i <= m ; i ++ ){
        root = new node; int ttcnt = 1;
        if( S[ i ].size() == 0 ) return;
        for( si it = S[ i ].begin() ; it != S[ i ].end() ; it ++ ){
            int tn = *it , len = strlen( c[ tn ] );
            node *now = root;
            for( int j = 0 ; j < len ; j ++ ){
                if( !now->nxt[ c[ tn ][ j ] - 'A' ] ){
                    ttcnt ++;
                    now->nxt[ c[ tn ][ j ] - 'A' ] = new node;
                }
                now = now->nxt[ c[ tn ][ j ] - 'A' ];
            }
        }
        clean( root );
        tcnt += ttcnt;
    }
    if( tcnt == ans ) anscnt ++;
    else if( tcnt > ans ) ans = tcnt , anscnt = 1;
}
void DFS( int now ){
    if( now == n ){
        cal();
        return;
    }
    for( int i = 1 ; i <= m ; i ++ ){
        S[ i ].insert( now );
        DFS( now + 1 );
        S[ i ].erase( now );
    }
}
void solve(){
    DFS( 0 );
    printf( "Case #%d: %d %d\n" , ++ cs , ans , anscnt );
}
int main(){

    freopen( "D-small-attempt0.in" , "r" , stdin );
    freopen( "D-small-attempt0.out" , "w" , stdout );

    scanf( "%d" , &t ); while( t -- ){
        init();
        solve();
    }

    fclose( stdin );
    fclose( stdout );
}
