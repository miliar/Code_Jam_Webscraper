#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <cstring>

using namespace std;

const int maxn = 1e4 + 5;

int n, disk, s[ maxn ];
bool mark[ maxn ];

int main()
{
    freopen( "A-large.in", "r", stdin );
    freopen( "A-large.out", "w", stdout );
    int cases;
    scanf( "%d", &cases );
    for ( int case_no = 1; case_no <= cases; case_no++ )
    {
        scanf( "%d %d", &n, &disk );
        for ( int i = 0; i < n; i++ ) scanf( "%d", &s[ i ] );
        sort( s, s + n );
        memset( mark, false, sizeof( mark ) );
        int sol = 0;
        for ( int i = n - 1; i >= 0; i-- )
        {
            if ( mark[ i ] ) continue;
            sol++;
            mark[ i ] = true;
            for ( int j = i - 1; j >= 0; j-- )
                if ( ! mark[ j ] && s[ j ] + s[ i ] <= disk )
            {
                mark[ j ] = true;
                break;
            }
        }
        printf( "Case #%d: %d\n", case_no, sol );
    }
    return 0;
}

