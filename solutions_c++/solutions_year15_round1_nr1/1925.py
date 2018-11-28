#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
    int t;
    scanf( "%d", &t );

    for( int z = 1; z <= t; z++ )
    {
        int n;
        scanf( "%d", &n );

        int tab[ 1010 ];
        for( int i = 0; i < n; i++ )
            scanf( "%d", &tab[ i ] );

        int res1 = 0;
        for( int i = 1; i < n; i++ )
        {
            if( tab[ i ] < tab[ i - 1 ] )
                res1 += tab[ i - 1 ] - tab[ i ];
        }

        int res2 = 0;
        int mpts = 0;
        for( int i = 1; i < n; i++ )
        {
            if( tab[ i ] < tab[ i - 1 ] - mpts )
            {
                mpts += tab[ i - 1 ] - tab[ i ] - mpts;
            }
        }
        for( int i = 0; i < n - 1 ; i++ )
            res2 += min( tab[ i ], mpts );

        printf( "Case #%d: %d %d\n", z, res1, res2 );
    }
}
