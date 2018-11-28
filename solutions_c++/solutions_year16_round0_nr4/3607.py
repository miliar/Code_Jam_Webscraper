#include <bits/stdc++.h>

#define INF 0x3F3F3F3F
#define rep(i, a, b) for (int i = int(a); i < int(b); i++)
#define pb push_back
#define pi 3.1415926535897932384626433832795028841971
#define debug(x) cout << #x << " = " << x << endl;
#define debug2(x,y) cout << #x << " = " << x << " --- " << #y << " " << y << "\n";
#define debugM( x, l, c ) { rep( i, 0, l ){ rep( j, 0, c ) printf("%d ", x[i][j]); printf("\n");}}
#define all(S) (S).begin(), (S).end()
#define MAXV 1010000
#define MAXN 110
#define F first
#define S second
#define EPS 1e-9
#define mk make_pair

// freopen("in.txt", "r", stdin);
// freopen("out.txt", "w", stdout);


using namespace std;

typedef pair <int, int> ii;
typedef unsigned long long int ll;

ll readInt();

ll fastPow( int b, int p ){
	if( !p ) return 1;
	if( p == 1 ) return b;
	if( p&1 ){
		return b * fastPow( b, p/2 );
	}
	else return fastPow( b, p/2 );
}

void S(){
	char c[10000];
	while( gets(c) ){
		cout << c << endl;
	}
}

int main(){

	freopen("D-small-attempt1.in", "r", stdin);
	freopen("D.sol", "w", stdout);
//	S();
	
	ll n = readInt();
	rep( test, 1, n+1 ){
		ll k = readInt();
		ll c = readInt();
		ll s = readInt();
		printf("Case #%d:", test );
		if( k == s ){
			rep( i, 1, k+1 ) printf(" %d", i);
			printf("\n");
			continue;
		}
		if( c * s < k ){
			printf(" IMPOSSIBLE\n");
			continue;
		}
		ll i = 1, spc = s, aux = 1, x = 0;
		for( ll u = 1; u <= k; u += c ){
			x = 0;
			rep( i, 1, c ){
				x += fastPow( k, c-i ) * ( u-1 );
			}
			x += min( c*aux++, k );
			printf(" %llu", x );	
		}
		printf("\n");
	}
//	*/
}

ll readInt () {
    bool minus = false;
    ll result = 0; char ch;

    ch = getchar();
    while (true) {
        if (ch == '-')
            break;
        if (ch >= '0' && ch <= '9') break;
        ch = getchar();
    }
    if (ch == '-')  minus = true;
    else result = ch-'0';
    while (true) {
        ch = getchar();
        if (ch < '0' || ch > '9') break;
        result = result*10 + (ch-'0');
    }
    if (minus) return -result;
    else return result;
}


