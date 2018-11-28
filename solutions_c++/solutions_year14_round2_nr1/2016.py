#include <cstdio>
#include <string>
#include <cstring>
using namespace std;

int N;
string letters[ 110 ];
int occur[ 110 ][ 110 ];
int average[ 110 ];
char str[ 110 ][ 110 ];

void proccess( int s ) {
    letters[ s ].push_back( str[ s ][ 0 ] );
    occur[ s ][ 0 ] = 1;

    int last = 0;
    for( int i = 1; str[ s ][ i ]; i++ ) {
        if( str[ s ][ i ] == letters[ s ][ last ] )
            occur[ s ][ last ]++;
        else {
            last++;
            letters[ s ].push_back( str[ s ][ i ] );
            occur[ s ][ last ] = 1;
        }
    }
}

bool check( ) {
    string pat = letters[ 0 ];

    for( int j = 0; j < letters[ 0 ].size(); j++ )
        average[ j ] += occur[ 0 ][ j ];

    for( int i = 1; i < N; i++ )
        if( letters[ i ] != pat )
            return false;
        else {
            for( int j = 0; j < letters[ i ].size(); j++ )
                average[ j ] += occur[ i ][ j ];
        }

    return true;
}

int main() {
    int T;

    freopen( "input.in", "r", stdin );
    freopen( "output.out", "w", stdout );

    scanf( "%d", &T );
    for( int t = 1; t <= T; t++ ) {
        scanf( "%d", &N );

        memset( occur, 0, sizeof( occur ) );
        for( int i = 0; i < N; i++ ) {
            scanf( "%s", str[ i ] );
            letters[ i ].clear();
            proccess( i );
        }

        memset( average, 0, sizeof( average ) );
        if( check() ) {
            int ans = 0;
            for( int i = 0; i < N; i++ )
                for( int j = 0; j < letters[ i ].size(); j++ )
                    ans += abs( occur[ i ][ j ] - average[ j ] / N );
            printf( "Case #%d: %d\n", t, ans );
        }
        else
            printf( "Case #%d: Fegla Won\n", t );

    }


    fclose( stdin );
    fclose( stdout );

    return 0;
}
