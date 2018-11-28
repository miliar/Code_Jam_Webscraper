#include <cstdio>

int arr[ 100 ][ 100 ];

int main()
{
    int t;
    scanf( "%d", &t );
    for( int ncase = 1; ncase <= t; ++ncase )
    {
        printf( "Case #%d: ", ncase );
        
        int n, m;
        scanf( "%d %d", &n, &m );

        int maxrow[ 100 ] = { 0 };
        int maxcol[ 100 ] = { 0 };

        for( int i = 0; i < n; ++i )
            for( int j = 0; j < m; ++j )
            {
                scanf( "%d", &arr[ i ][ j ] );
                if( arr[ i ][ j ] > maxrow[ i ] )
                    maxrow[ i ] = arr[ i ][ j ];
                if( arr[ i ][ j ] > maxcol[ j ] )
                    maxcol[ j ] = arr[ i ][ j ];
            }
        bool check[ 100 ][ 100 ] = { 0 };

        for( int i = 0; i < n; ++i )
            for( int j = 0; j < m; ++j )
                if( arr[ i ][ j ] == maxrow[ i ] ||
                    arr[ i ][ j ] == maxcol[ j ] )
                    check[ i ][ j ] = 1;

        bool res = true;
        for( int i = 0; i < n && res; ++i )
            for( int j = 0; j < m && res; ++j )
                if( !check[ i ][ j ] )
                    res = false;
        printf( "%s\n", res ? "YES" : "NO" );
    }
}
