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
int r, c, w;

int main( ) {

    if( FILE ) {
        if( FILE & 1 ) freopen( INPUT , "r", stdin  );
        if( FILE & 2 ) freopen( OUTPUT, "w", stdout );
    }

    cin >> nTest;
    for( int t = 1; t <= nTest; t++ ) {
        cin >> r >> c >> w;
        int ans = int ( ceil( r*c/(w*1.0) ) );
        ans += min( r, c ) > 1;
        ans += ( w-1 );
        cout << "Case #" << t << ": " << min( ans, r*c ) << "\n";
    }

    return 0;
}
