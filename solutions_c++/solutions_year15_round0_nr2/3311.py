#include <cstdio>
#include <algorithm>

#define INF 2000000000

using namespace std;

int main()
{
    int z;
    scanf( "%d", &z );

    for( int t = 1; t <= z; t++ )
    {
        int d;
        scanf( "%d", &d );

        int p[ 1010 ];
        int max_p = -INF;
        for( int i = 0; i < d; i++ )
        {
            scanf( "%d", &p[ i ] );
            max_p = max( p[ i ], max_p );
        }
        
        int res = INF;
        for( int i = 1; i <= max_p; i++ )
        {
            int time = 0;
            for( int j = 0; j < d; j++ )
            {
                if( p[ j ] > i )
                {
                    time += p[ j ] / i;
                    if( p[ j ] % i == 0 )
                        time -= 1;
                }
            }
            res = min( res, i + time );
        }
        printf( "Case #%d: %d\n", t, res );
    }
}
