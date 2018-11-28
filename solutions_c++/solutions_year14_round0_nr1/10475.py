#include <iostream>
#include <cstdio>
#define N 16

using namespace std;

int main()
{
    freopen( "A-small-attempt0.in", "r", stdin );
    freopen( "A-small-attempt0.out", "w", stdout );
    int n;
    scanf( "%d", &n );
    for( int k = 1; k <= n; k++ )
    {
        int in[N];
        int row = 0;
        int t1[N/4] = {0};
        int t2[N/4] = {0};
        scanf( "%d", &row );
        for( int i = 0; i < N; i++ )
        {
            scanf( "%d", &in[i] );
        }
        for( int i = 0; i < 4; i++ )
        {
            t1[i] = in[ (row-1)*4 + i ];
        }
        scanf( "%d", &row );
        for( int i = 0; i < N; i++ )
        {
            scanf( "%d", &in[i] );
        }
        for( int i = 0; i < 4; i++ )
        {
            t2[i] = in[ (row-1)*4+i ];
        }
        int times = 0;
        int ans = 0;
        for( int i = 0; i < 4; i++ )
        {
            for( int j = 0; j < 4; j++ )
            {
                if( t1[i] == t2[j] )
                {
                    if( times < 1 )
                    {
                        ans = i;
                    }
                    times++;
                }
            }
        }
        printf( "Case #%d: ", k );
        if( times != 0 )
        {
            if( times == 1 )
            {
                printf( "%d\n", t1[ans] );
            }
            else
            {
                printf( "Bad magician!\n");
            }
        }
        else
        {
            printf( "Volunteer cheated!\n" );
        }
    }
    return 0;
}
