#include <bits/stdc++.h>
using namespace std;

#define MAX 205
#define MOD 1000000007
#define all( x ) x.begin() , x.end()
#define unique( c ) ( c ).resize( unique( all( c ) ) - ( c ).begin() )
#define debug( a ) cerr << #a << ": " << a << endl;

int main (){
    freopen("D:/CodeBlocks/in.txt","r",stdin);
    freopen("D:/CodeBlocks/out.txt","w",stdout);
    int t; cin >> t;
    for ( int tc = 0 ; tc < t ; tc++ ){
        int x , r , c; cin >> x >> r >> c;
        if( x == 1 ){
            printf( "Case #%d: GABRIEL\n" , tc + 1 );
        } else if( x == 2 ){
            if( r % 2 != 0 ){
                if( c % 2 != 0 ) printf( "Case #%d: RICHARD\n" , tc + 1 );
                else printf( "Case #%d: GABRIEL\n" , tc + 1 );
            } else printf( "Case #%d: GABRIEL\n" , tc + 1 );
        } else if( x == 3 ){
            if( r == 1 ) printf( "Case #%d: RICHARD\n" , tc + 1 );
            if( r == 2 ){
                if( c == 3 ) printf( "Case #%d: GABRIEL\n" , tc + 1 );
                else printf( "Case #%d: RICHARD\n" , tc + 1 );
            }
            if( r == 3 ){
                if( c == 1 ) printf( "Case #%d: RICHARD\n" , tc + 1 );
                else printf( "Case #%d: GABRIEL\n" , tc + 1 );
            }
            if( r == 4 ){
                if( c == 3 ) printf( "Case #%d: GABRIEL\n" , tc + 1 );
                else printf( "Case #%d: RICHARD\n" , tc + 1 );
            }
        } else if( x == 4 ){
            if( r == 1 ) printf( "Case #%d: RICHARD\n" , tc + 1 );
            if( r == 2 ) printf( "Case #%d: RICHARD\n" , tc + 1 );
            if( r == 3 ){
                if( c == 4 ) printf( "Case #%d: GABRIEL\n" , tc + 1 );
                else printf( "Case #%d: RICHARD\n" , tc + 1 );
            }
            if( r == 4 ){
                if( c == 1 || c == 2 ) printf( "Case #%d: RICHARD\n" , tc + 1 );
                else printf( "Case #%d: GABRIEL\n" , tc + 1 );
            }
        }
    }
    return 0;
}
