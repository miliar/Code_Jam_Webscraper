#include <cstdio>

bool judge( int k )
{
    int arr[ 10 ], l = 0, j = k;
    while( j != 0 )
    {
        arr[ l++ ] = j % 10;
        j /= 10;
    }
    for( int i = l / 2 - 1; i >= 0; --i )
        if( arr[ i ] != arr[ l - 1 - i ] ) return false;
    return true;
}

int main()
{
    int t;
    scanf( "%d", &t );
    for( int ncase = 1; ncase <= t; ++ncase )
    {
        printf( "Case #%d: ", ncase );
        
        int a, b;
        scanf( "%d %d", &a, &b );
        
        int res = 0;
        for( int i = 1; i * i <= b; ++i )
            if( i * i >= a && judge( i ) )
                if( judge( i * i ) )
                {
                    ++res;
                    //printf( "\n%d:%d\n", i, i * i );
                }
        printf( "%d\n", res );
    }
}
