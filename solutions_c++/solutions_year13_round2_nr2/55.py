#include <bits/stdc++.h>
using namespace std;

#define fr(a,b,c) for( int a = b ; a < c ; ++a )
#define si(x) scanf("%d", &x)

struct S {
	int a,b,c,d;
	S(){}
	S(int a,int b, int c,int d): a(a), b(b), c(c),d(d) {}
	bool operator<(const S & s) const {
		if( a != s.a ) return a < s.a;
		if( b != s.b ) return b < s.b;
		if( c != s.c ) return c < s.c;
		return d < s.d;
	}
};

int af, bf, n;
map<S,double> mapa;
double go(int a, int b, int c, int d) {
	if( a == af && b == bf ) return 1.;
	if( d == n ) return 0.;
	if( mapa.count(S(a,b,c,d)) ) return mapa[S(a,b,c,d)];
	if( b == a && c == a ) {
		return mapa[S(a,b,c,d)] = go(a+2,0,0,d+1);
	}
	if( b == a ) {
		return mapa[S(a,b,c,d)] = go(a,b,c+1,d+1);
	}
	if( c == a ) {
		return mapa[S(a,b,c,d)] = go(a,b+1,c,d+1);
	}
	return mapa[S(a,b,c,d)] = go(a,b+1,c,d+1)*.5 + go(a,b,c+1,d+1)*.5;
}

int main() {
	int tc, caso = 1;
	si(tc);
	while( tc--  ){
		printf("Case #%d: ", caso++);
		int x,y;
		si(n), si(x), si(y);
		if( x < 0 ) x = -x;
		if( x == 0 ) {
			af = y+2;
			bf = 0;
		} else {
			af = y+x;
			bf = y+1;
		}
		mapa.clear();
		int aa = 0;
		while( n > 2*aa+1 ) n -= 2*aa+1, aa+=2;
		if( af < aa ) {
			printf("%.8lf\n", 1.);		
		} else if ( af > aa+2 ) {
			printf("%.8lf\n", 0.);		
		} else {
			printf("%.8lf\n", go(aa,0,0,0));
		}
		cerr << tc << endl;
	}
	return 0;
}

