#include <bits/stdc++.h>

#define FILE 	3
#define INPUT 	"ASmall.in"
#define OUTPUT 	"ASmall.out"

#define MP 	    make_pair
#define MT 	    make_tuple
#define PB 	    push_back
#define FI 	    first
#define SE 	    second

#define MAX 	int(1e6+10)
#define INF 	INT_MAX
#define EPS 	int(1e-7)
#define MOD 	int(1e7+7)
#define PI 	    acos(-1)

typedef long long ll;

using namespace std;

int nTest;
int n;
int dp[ MAX ];

int reverseNumber( int x ) {
    int ret = 0;
    while( x ) {
        ret = ret*10 + x%10;
        x /= 10;
    }
    return ret;
}

void solve( ) {
    memset( dp, -1, sizeof( dp ) );
    dp[ 0 ] = 0;
    for( int i = 1; i < MAX; i++ ) {
        int r = reverseNumber( i );
        if( dp[ i ] == -1 ) dp[ i ] = dp[ i-1 ]+1;
        else dp[ i ] = min( dp[i-1]+1, dp[i] );
        if( r <= i || r >= MAX ) continue;
        if( dp[ r ] == -1 ) dp[ r ] = dp[ i ]+1;
        else dp[ r ] = min( dp[i]+1, dp[r] );
    }
}

int main( ) {

    if( FILE ) {
        if( FILE & 1 ) freopen( INPUT , "r", stdin  );
        if( FILE & 2 ) freopen( OUTPUT, "w", stdout );
    }

    solve( );

    cin >> nTest;
    for( int t = 1; t <= nTest; t++ ) {
        cin >> n;
        cout << "Case #" << t << ": " << dp[ n ] << "\n";
    }

    return 0;
}
