#include <bits/stdc++.h>

#define FILE 	3
#define INPUT 	"ALarge.in"
#define OUTPUT 	"ALarge.out"

#define MP 	    make_pair
#define MT 	    make_tuple
#define PB 	    push_back
#define FI 	    first
#define SE 	    second

#define MAX 	int(1e3+100)
#define INF 	INT_MAX
#define EPS 	int(1e-7)
#define MOD 	int(1e7+7)
#define PI 	    acos(-1)

typedef long long ll;

using namespace std;

int nTest, N, M[ MAX ], ans[ 2 ];

int main( ) {

    if( FILE ) {
        if( FILE & 1 ) freopen( INPUT , "r", stdin  );
        if( FILE & 2 ) freopen( OUTPUT, "w", stdout );
    }

    cin >> nTest;

    for( int t = 1; t <= nTest; t++ ) {
        cin >> N;
        for( int i = 0; i < N; i++ ) cin >> M[ i ];

        ans[ 0 ] = ans[ 1 ] = 0;

        for( int i = 0; i < N-1; i++ )
            if( M[ i ] > M[ i+1 ] )
                ans[ 0 ] += M[ i ]-M[i+1];

        int cant = 0;
        for( int i = 0; i < N-1; i++ )
            cant = max( cant, M[ i ]-M[i+1] );
        for( int i = 0; i < N-1; i++ )
            ans[ 1 ] += min( cant, M[ i ] );

        cout << "Case #" << t << ": " << ans[ 0 ] << " " << ans[ 1 ] << "\n";
    }

    return 0;
}
