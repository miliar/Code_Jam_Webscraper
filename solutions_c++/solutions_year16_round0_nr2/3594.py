#include <cstdio>
#include <cstring>

using namespace std;

int main(){
    int t;
    scanf( "%d", &t );

    for( int i = 1; i <= t; i++ ){
        
        char buf[ 110 ];
        scanf( "%s", buf );
        
        int n = strlen( buf );
        int tab[ 110 ];
        tab[ n - 1 ] = buf[ n - 1 ] == '+' ? 0 : 1;
        
        for( int j = n - 2; j >= 0; j-- ){
            if( tab[ j + 1 ] % 2 == 0 && buf[ j ] == '-' )
                tab[ j ] = tab[ j + 1 ] + 1;
            else if( tab[ j + 1 ] % 2 == 1 && buf[ j ] == '+' )
                tab[ j ] = tab[ j + 1 ] + 1;
            else
                tab[ j ] = tab[ j + 1 ];
        }
        printf( "Case #%d: %d\n", i, tab[ 0 ] );
    }
}
