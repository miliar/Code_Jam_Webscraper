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

int n, a[ 1000100 ];
long long b[ 1000100 ];

long long fsum( int l, int r )
{
    return b[r] - b[l - 1];
}

long long calc_pref()
{
    long long result = inf;
    for ( int i = 1; i <= n; i++ ) b[i] = b[i - 1] + a[i - 1];   
    for ( int l = 0; l < n; l++ )
    {
        int left = l + 1, right = n, value = l + 1;
        while ( left <= right )
        {
            int middle = ( left + right ) / 2;
            if ( fsum( l + 1, middle ) <= fsum( middle + 1, n ) )
            {
                value = max( middle, value );
                left = middle + 1;
            } else right = middle - 1;
        }
        if ( max( fsum( l + 1, value ), fsum( value + 1, n ) ) <= b[ l ] ) result = min( result, b[l] );
        if ( value < n && max( fsum( l + 1, value + 1 ), fsum( value + 2, n ) ) <= b[ l ] ) result = min( result, b[l] );
    }
    //cout << "Pref: " << result << "\n";
    return result;
}

long long roundup( long long a, long long b )
{
    if ( a % b == 0 ) return a / b;
    return a / b + 1;
}

long long calc_center()
{
    long long result = inf;
    for ( int i = 1; i <= n; i++ ) b[i] = b[i - 1] + a[i - 1];
    for ( int l = 0; l < n; l++ )
    {
        long long limit = max( 2 * b[l], roundup( b[n] + b[l], 2 ) );
        if ( b[n] < limit ) continue;
        int left = l + 1, right = n, value = n;
        while ( left <= right )
        {
            int middle = ( left + right ) / 2;
            if ( b[ middle ] >= limit )
            {
                value = min( middle, value );
                right = middle - 1;
            } else left = middle + 1;
        }
        result = min( result, b[ value ] - b[ l ] );
    }
    return result;
}

void solve()
{   
    int p, q, r, s;
    scanf("%d%d%d%d%d", &n, &p, &q, &r, &s);
    for ( int i = 0; i < n; i++ ) a[i] = ( 1ll * i * p + q ) % r + s;
    long long answer = calc_pref();
    reverse( a, a + n );
    answer = min( answer, calc_pref() );
    answer = min( answer, calc_center() );
    cout << fixed << setprecision( 12 ) << (long double)( b[n] - answer ) / (long double)b[n];
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