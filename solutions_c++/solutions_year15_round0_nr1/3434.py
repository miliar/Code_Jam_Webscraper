#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
    int z;
    scanf( "%d", &z );

    for( int t = 1; t <= z; t++ )
    {
        int n;
        scanf( "%d", &n );

        char buf[ 1010 ];
        scanf( "%s", buf );
        
        int tab[ 1010 ];
        for( int i = 0; i <=n; i++ )
            tab[ i ] = buf[ i ] - '0';
        
        int res = 0;
        int pref[ 1010 ];
        pref[ 0 ] = tab[ 0 ];
        for( int i = 1; i <= n; i++ )
        {
            if( pref[ i - 1 ] < i )
            {
                res += i - pref[ i - 1 ];
                pref[ i ] = tab[ i ] + i;
            }
            else
                pref[ i ] = pref[ i - 1 ] + tab[ i ];
        }
        printf( "Case #%d: %d\n", t, res );
    }
}
