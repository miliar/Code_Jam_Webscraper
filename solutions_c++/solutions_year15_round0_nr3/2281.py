#include <bits/stdc++.h>

#define FILE 	1
#define INPUT 	"CSmall.in"
#define OUTPUT 	"CSmall.out"

#define MP 	    make_pair
#define MT 	    make_tuple
#define PB 	    push_back
#define FI 	    first
#define SE 	    second

#define MAX 	int(1e5+10)
#define INF 	INT_MAX
#define EPS 	int(1e-7)
#define MOD 	int(1e7+7)
#define PI 	    acos(-1)

#define I       2
#define J       3
#define K       4

typedef long long ll;

using namespace std;

map< char, int > id;
int result[5][5] = { {  0  ,  0  ,  0  ,  0  ,  0  },
                     {  0  ,  1  ,  I  ,  J  ,  K  },
                     {  0  ,  I  , -1  ,  K  , -J  },
                     {  0  ,  J  , -K  , -1  ,  I  },
                     {  0  ,  K  ,  J  , -I  , -1  } };
int nTest, L, X, accum[ MAX ];
string S;

int main( ) {

    if( FILE ) {
        freopen( INPUT , "r", stdin  );
        freopen( OUTPUT, "w", stdout );
    }

    id[ 'i' ] = I; id[ 'j' ] = J; id[ 'k' ] = K;

    cin >> nTest;

    for( int t = 1; t <= nTest; t++ ) {
        cin >> L >> X >> S;
        bool ans = false;
        for( int i = 0; i < L*X; i++ ) {
            int curNum = id[ S[ i%L ] ];
            if( i ) accum[ i ] = result[ abs(accum[ i-1 ]) ][ curNum ] * (accum[ i-1 ] < 0 ? -1 : 1);
            else accum[ i ] = curNum;
        }
        if( accum[L*X-1] == -1 ) {
            for( int i = 0; i < L*X-2 && !ans; i++ )
                if( accum[i] == I )
                    for( int j = i+1; j < L*X-1 && !ans; j++ )
                        if( accum[j] == K )
                            ans = true;
        }

        cout << "Case #" << t << ": ";
        if( ans ) cout << "YES\n";
        else cout << "NO\n";
    }

    return 0;
}
