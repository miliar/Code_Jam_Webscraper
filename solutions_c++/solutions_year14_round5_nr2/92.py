#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <algorithm>
#include <iomanip>
#include <queue>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <stack>
#include <bitset>
#include <sstream>
#include <fstream>

typedef unsigned long long ull;
#define mp make_pair
#define pb push_back

const long double eps = 1e-9;
const double pi = acos(-1.0);
const long long inf = 1e18;

using namespace std;

int p, q, n, h[ 111 ], g[ 111 ];
int f[ 111 ][ 222 ][ 1111 ], dp[ 111 ][ 1111 ][ 2 ];

void upd( int &a, int b )
{
    a = max( a, b );
}

void solve()
{
    cin >> p >> q >> n;
    for ( int i = 1; i <= n; i++ ) cin >> h[i] >> g[i];
    memset( f, -1, sizeof( f ) );
    memset( dp, -1, sizeof( dp ) );
    f[ 1 ][ h[1] ][ 0 ] = 0;
    for ( int i = 1; i <= n; i++ )
    {
        for ( int k = 0; k <= 1000; k++ )
        {
            for ( int j = h[i]; j > 0; j-- )
            {
                if ( f[i][j][k] == -1 ) continue;
                //cout << "f " << i << " " << j << " " << k << " " << f[i][j][k] << "\n"; 
                // Diana beats this monster
                {
                    if ( j - p - q >= 1 ) upd( f[ i ][ j - p - q ][ k ], f[i][j][k] );
                    else if ( j - p < 1 ) upd( dp[ i ][ k ][ 1 ], f[i][j][k] + g[i] );
                    else if ( j - p - q < 1 ) upd( dp[ i ][ k ][ 0 ], f[i][j][k] );
                }
                // Diana doens't beat this monster
                {
                    if ( j - q >= 1 ) upd( f[ i ][ j - q ][ k + 1 ], f[i][j][k] );
                    else if ( j - q < 1 ) upd( dp[ i ][ k + 1 ][ 0 ], f[i][j][k] );
                }
            }  
        }

        if ( i == n ) continue;  

        for ( int k = 0; k <= 1000; k++ )
        {
            //if ( dp[i][k][0] != -1 ) cout << "DP " << i << " " << k << " 0 " << dp[i][k][0] << "\n";
            if ( dp[i][k][0] != -1 )
                for ( int num = 0;; num++ )
                {
                    if ( num > k ) break;
                    int health = h[ i + 1 ] - p * num;
                    if ( health >= 1 ) upd( f[ i + 1 ][ health ][ k - num ], dp[i][k][0] );
                    else if ( health < 1 ) 
                    {
                        upd( dp[i + 1][ 0 ][ k - num ], dp[i][k][0] + g[i + 1] );
                        break;
                    }
                }
            //if ( dp[i][k][1] != -1 ) cout << "DP " << i << " " << k << " 1 " << dp[i][k][1] << "\n";
            if ( dp[i][k][1] != -1 )
                for ( int num = 0;; num++ )
                {
                    if ( num > k ) break;
                    int health = h[ i + 1 ] - p * num;
                    if ( health >= 1 ) 
                    {
                        health -= q;
                        if ( health >= 1 )
                            upd( f[ i + 1 ][ health ][ k - num ], dp[i][k][1] );
                        else if ( health < 1 ) 
                            upd( dp[ i + 1 ][ k - num ][ 0 ], dp[i][k][1] );
                    }
                    else if ( health < 1 ) 
                    {
                        upd( dp[ i + 1 ][ k - num ][ 1 ], dp[i][k][1] + g[i + 1] );
                        break;
                    }
                }
        }
    }
    int answer = 0;
    for ( int i = 0; i <= 1000; i++ ) 
    {
        //if ( dp[n][i][0] != -1 ) cout << "DP " << n << " " << i << " 0 " << dp[n][i][0] << "\n";
        //if ( dp[n][i][1] != -1 ) cout << "DP " << n << " " << i << " 1 " << dp[n][i][1] << "\n";
        upd( answer, max( dp[n][i][0], dp[n][i][1] ) );
    }
    cout << answer;
}

int main (int argc, const char * argv[])
{
    int testcase; scanf("%d", &testcase);
    for ( int test = 1; test <= testcase; test++ ) 
    {
        printf("Case #%d: ", test);
        solve();
        printf("\n");
    }
    return 0;
}