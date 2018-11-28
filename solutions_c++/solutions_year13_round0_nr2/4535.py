/*
    Marko Bakovic
    Google Code Jam
    Problem B. Lawnmower
*/

#include <cstdio>
#include <algorithm>

using namespace std;

const int maxn = 100 + 5;

int n, m, cases, cntCases, grass[ maxn ][ maxn ];

int main()
{
    freopen( "B-large.in", "r", stdin );
    freopen( "B-large.out", "w", stdout );
    scanf( "%d", &cases );

    while ( cases-- )
    {
        scanf( "%d %d", &n, &m );
        for ( int i = 0; i < n; i++ )
            for ( int j = 0; j < m; j++ ) scanf( "%d", &grass[ i ][ j ] );
        bool found = false;
        for ( int i = 0; i < n; i++ )
            for ( int j = 0; j < m; j++ )
            {
                bool foundRow = false, foundCol = false;
                for ( int k = 0; k < n; k++ )
                    if ( grass[ i ][ j ] < grass[ k ][ j ] )
                {
                    foundRow = true;
                    break;
                }
                for ( int k = 0; k < m; k++ )
                    if ( grass[ i ][ j ] < grass[ i ][ k ] )
                {
                    foundCol = true;
                    break;
                }
                if ( foundRow && foundCol )
                {
                    found = true;
                    break;
                }
            }
        cntCases++;
        printf( "Case #%d: ", cntCases );
        if ( found ) printf( "NO\n" );
        else printf( "YES\n" );
    }

    return 0;
}
