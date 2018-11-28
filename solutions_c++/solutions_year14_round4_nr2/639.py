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

const int maxn = 1000 + 5;

int n, x[ maxn ], sol;

int main()
{
    freopen( "B-large.in", "r", stdin );
    freopen( "B-large.out", "w", stdout );
    int cases;
    scanf( "%d", &cases );
    for ( int case_no = 1; case_no <= cases; case_no++ )
    {
        scanf( "%d", &n );
        for ( int i = 0; i < n; i++ ) scanf( "%d", &x[ i ] );
        int left = 0, right = n - 1, sol = 0;
        for ( int i = 0; i < n; i++ )
        {
            int min_id = -1;
            for ( int j = left; j <= right; j++ )
                if ( min_id == -1 || x[ j ] < x[ min_id ] ) min_id = j;
            if ( min_id - left < right - min_id )
            {
                while ( min_id > left )
                {
                    swap( x[ min_id ], x[ min_id - 1 ] );
                    sol++;
                    min_id--;
                }
                left++;
            }
            else
            {
                while ( min_id < right )
                {
                    swap( x[ min_id ], x[ min_id + 1 ] );
                    sol++;
                    min_id++;
                }
                right--;
            }
        }
        printf( "Case #%d: %d\n", case_no, sol );
    }
    return 0;
}

