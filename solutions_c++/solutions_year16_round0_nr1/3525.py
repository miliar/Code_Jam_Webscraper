#include <cstdio>

using namespace std;

int main(){
    int t;
    scanf( "%d", &t );

    for( int T = 1; T <= t; T++ ){
        int n;
        scanf( "%d", &n );

        if( n == 0 ){
            printf( "Case #%d: INSOMNIA\n",  T );
            continue;
        }

        bool dig[ 10 ];
        for( int i = 0; i < 10; i++ )
            dig[ i ] = false;
        int digits = 0;
        bool solved = false; 
        for( int i = 1; i <= 200; i++ ){
            int m = i * n;
            
            while( m != 0 ){
                int d = m % 10;
                if( !dig[ d ] )
                    digits++;
                dig[ d ] = true; 
                
                if( digits == 10 )
                    break;
                m = m / 10;
            }
            if( digits == 10 ){
                printf( "Case #%d: %d\n", T, i * n );
                solved = true;
                break;
            }
        }
        if( !solved ){
            printf( "Ooops!\n" );
            return 0;
        }
    }
}
