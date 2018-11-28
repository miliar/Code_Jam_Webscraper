#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <string>

using namespace std;

int n, sets, in[ 10 ], sol, sol_cnt;
string word[ 10 ];
vector < string > V[ 5 ];

int solve()
{
    for ( int i = 0; i < sets; i++ ) V[ i ].clear();
    for ( int i = 0; i < n; i++ ) V[ in[ i ] ].push_back( word[ i ] );
    for ( int i = 0; i < sets; i++ ) sort( V[ i ].begin(), V[ i ].end() );
    int ret = 0, len_prev;
    string prev;
    for ( int i = 0; i < sets; i++ )
        for ( int j = 0; j < V[ i ].size(); j++ )
        {
            if ( j == 0 )
            {
                ret += V[ i ][ 0 ].length() + 1;
                prev = V[ i ][ 0 ];
                len_prev = V[ i ][ 0 ].length();
            }
            else
            {
                int len = V[ i ][ j ].length();
                ret += len;
                for ( int k = 0; k < min( len, len_prev ); k++ )
                    if ( prev[ k ] == V[ i ][ j ][ k ] ) ret--;
                    else break;
                len_prev = len;
                prev = V[ i ][ j ];
            }
        }
    return ret;
}

void dfs( int curr )
{
    if ( curr == n )
    {
        int temp = solve();
        if ( temp > sol ) sol = temp, sol_cnt = 1;
        else if ( temp == sol ) sol_cnt++;
    }
    else
    {
        for ( int i = 0; i < sets; i++ )
        {
            in[ curr ] = i;
            dfs( curr + 1 );
        }
    }
}

int main()
{
    freopen( "D-small-attempt0.in", "r", stdin );
    freopen( "D-small-attempt0.out", "w", stdout );
    int cases;
    scanf( "%d", &cases );
    for ( int case_no = 1; case_no <= cases; case_no++ )
    {
        scanf( "%d %d", &n, &sets );
        sol = sol_cnt = 0;
        for ( int i = 0; i < n; i++ ) cin >> word[ i ];
        dfs( 0 );
        printf( "Case #%d: %d %d\n", case_no, sol, sol_cnt );
    }
    return 0;
}

