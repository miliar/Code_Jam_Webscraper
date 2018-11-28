/**
 * Tittle:	Dijkstra
 * Author:	Cheng-Shih, Wong
 * Date:	2015/04/11
 */

// include files
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>

using namespace std;

// definitions
#define FOR(i,a,b) for( int i=(a),_n=(b); i<=_n; ++i )
#define clr(x,v) memset( x, v, sizeof(x) )
#define pb push_back
#define N 10005

typedef long long ll;
typedef vector<ll> VLL;

class Ele {
public:
	bool s;
	char d;

	Ele( bool _s=false, char _d='1' ): s(_s), d(_d) {}

	Ele( char c ) {
		s = false;
		d = c;
	}

	Ele( const char *str ) {
		s = false;
		if( *str == '-' ) {
			s = true;
			++str;
		}
		d = *str;
	}

	const Ele operator*( const Ele &op ) const {
		switch( d ) {
		case '1':
			return Ele( s^op.s, op.d );
		case 'i':
			if( op.d=='1' ) return Ele( s^op.s, 'i' );
			if( op.d=='i' ) return Ele( s^op.s^1, '1' );
			if( op.d=='j' ) return Ele( s^op.s, 'k' );
			if( op.d=='k' ) return Ele( s^op.s^1, 'j' );
		case 'j':
			if( op.d=='1' ) return Ele( s^op.s, 'j' );
			if( op.d=='i' ) return Ele( s^op.s^1, 'k' );
			if( op.d=='j' ) return Ele( s^op.s^1, '1' );
			if( op.d=='k' ) return Ele( s^op.s, 'i' );
		case 'k':
			if( op.d=='1' ) return Ele( s^op.s, 'k' );
			if( op.d=='i' ) return Ele( s^op.s, 'j' );
			if( op.d=='j' ) return Ele( s^op.s^1, 'i' );
			if( op.d=='k' ) return Ele( s^op.s^1, '1' );
		}
	}

	const string toS( void ) const {
		string ret;
		if( s ) ret += '-';
		ret += d;
		return ret;
	}

	const bool operator==( const Ele &op ) const {
		return (s==op.s && d==op.d);
	}
};

// declarations
int t;
ll L, X;
char buf[N];
Ele pre[N];
VLL xl, xr;
ll maxl;

// functions
const Ele rg( int l, int r )
{
	--l;
	return pre[l]*pre[l]*pre[l]*pre[r];
}

const Ele calc( ll l, ll r )
{
	ll lk = (l+L-1)/L;
	ll rk = (r+L-1)/L;
	ll lm = ((l-1)%L)+1;
	ll rm = ((r-1)%L)+1;

	if( lk==rk ) return rg(lm,rm);

	ll p = rk-(lk+1);
	
	Ele m;
	if( p&1LL ) m = pre[L];
	else m = "1";
	if( p&2LL ) m = m*"-1";

	return rg(lm,L)*m*pre[rm];
}

bool check( void )
{
	FOR( i, 0, xl.size()-1 ) FOR( j, 0, xr.size()-1 ) {
		if( xl[i] <= xr[j] ) {
			if( calc(xl[i],xr[j])==Ele("j") )
				return true;
		}
	}

	return false;
}

// main function
int main( void )
{
	Ele tmp;
	
	// input
	scanf( "%d", &t );

	FOR( ti, 1, t ) {
		scanf( "%lld%lld", &L, &X );
		scanf( "%s", buf+1 );

		printf( "Case #%d: ", ti );

		maxl = X*L;
		
		if( maxl < 3 ) {
			puts("NO");
			continue;
		}

		// solve
		pre[0] = Ele("1");
		pre[1] = Ele(buf[1]);
		FOR( i, 2, L ) 
			pre[i] = pre[i-1]*Ele(buf[i]);

		xl.clear();
		xr.clear();

		FOR( i, 1, 6*L+1 ) {
			if( (i+1)<maxl && calc(1,i)==Ele("i") ) {
				xl.pb(i+1);
			}
			if( (maxl-i)>1 && calc(maxl-i+1,maxl)==Ele("k") ) {
				xr.pb(maxl-i);
			}
		}

		// output
		if( check() ) puts("YES");
		else puts("NO");
	}
	
	return 0;
}
