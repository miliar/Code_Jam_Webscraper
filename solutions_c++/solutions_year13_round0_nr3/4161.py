// File Name   : c.cpp
// Development : Saturday 13 April 2013 07:37:05 PM IST
// Author      : Xeronix

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <bitset>
#include <sstream>
#include <stack>
#include <queue>
#include <numeric>
#include <utility>
#include <cctype>
#include <list>
#include <valarray>
#include <sstream>
#include <complex>
#include <deque>
#include <new>
#include <map>
#include <set>

#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <signal.h>
#include <time.h>
#include <float.h>

#define TR(c,i) for ( typeof((c).begin()) i = (c).begin(); i != (c).end(); i++ ) 
#define SWAP(a,b) {typeof(a) T; T=a; a=b; b=T;}
#define FOR(i,a,b) for( i = a; i <= b; i++ )
#define ROF(i,a,b) for( i = a; i >= b; i-- )
#define MEM(t,n) ( t * )malloc( (n)*sizeof( t ) )
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define ALL(v) (v).begin(), (v).end()
#define SORT(v) sort( ALL(v) )
#define SET(x,a) memset(x,a,sizeof(x))
#define IN(x,a) (x.find(a) != x.end()) 

#define DIST(x1,y1,x2,y2) SQ(x1-x2)+SQ(y1-y2)
#define DISTS(p,q) SQ(p.x-q.x)+SQ(p.y-q.y)
#define SQ(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define F first
#define S second

#define DEB(x) cout << #x << " = " << x << endl;
#define DEBA(x,n) { int i; cout << "{\n"; FOR(i,0,n-1)cout << i << " " << x[i] << endl; cout << "}\n"; }
#define DEBT(x) { cout << "{\n"; TR( x,it ) cout << *it << "\n" ; cout << "}\n"; }
#define DEBM(x) { cout << "{\n"; TR( x,it ) cout << it->F << " : " << it->S << "\n"; cout << "}\n"; }

#define SYNC ios_base::sync_with_stdio(false);
#define C(format,n) scanf( "%"#format, &n )
#define P(format,n) printf( "%"#format, n )

//#define LIM
#ifdef LIM
	int S, D, Y, O;
	char *inp, *out, *ipos, *opos, DIG[30];
	#define FRMI inp=( char * )malloc( LIM*sizeof( char ) );fread_unlocked( inp,1,LIM,stdin );ipos=inp;
	#define FWM out=( char * )malloc( LIM*sizeof( char ) );opos=out;
	#define FWO fwrite_unlocked( out,opos-out,1,stdout );
	#define GETI(n) n=0;while(*ipos<33){ipos++;}if(*ipos=='-'){S=-1;ipos++;}else{S=1;}while(*ipos>='0'){n=10*n+(*ipos-'0');ipos++;}n*=S;
	#define PUTI(n) O=n;D=0;if(O<0){*opos++='-';O*=-1;}if(!O)*opos++='0';else{while(O){Y=O/10;DIG[D++]=O-Y*10+'0';O=Y;}\
	while(D--)*opos++=DIG[D];}
	#define PUTC(c) *opos++=c;
#endif

using namespace std;

template<class T> inline string tostring( T n ){ stringstream ss; ss << n; ss.flush(); return ss.str(); }
template<class T> inline string tobinary( T n ){ string s = n ? "" : "0"; while( n ) { s += ( ( n & 1 ) + '0' ); n >>= 1; } return s; }
template<class T> inline int digits( T n ){ int cnt = n ? 0 : 1; while( n ){ n /= 10; cnt++; } return cnt; }
template<class T1, class T2> inline T2 gcd( T1 a, T2 b ){ return !b ? a : gcd( b, a%b ); }
template<class T> inline T abs( T a ){ return a < 0 ? -a : a; }

inline bool is_palin( long long n ) {
	string s = tostring(n);
	int l = s.length();
	int i, j;

	for( i = 0, j = l-1; i < j; i++, j-- ) {
		if( s[i] != s[j] ) {
			return false;
		}
	}

	return true;
}

long long fp[39] = { 1LL, 4LL, 9LL, 121LL, 484LL, 10201LL, 12321LL, 14641LL, 40804LL, 44944LL, 1002001LL, 1234321LL, 4008004LL, 100020001LL, 102030201LL, 104060401LL, 121242121LL, 123454321LL, 125686521LL, 400080004LL, 404090404LL, 10000200001LL, 10221412201LL, 12102420121LL, 12345654321LL, 40000800004LL, 1000002000001LL, 1002003002001LL, 1004006004001LL, 1020304030201LL, 1022325232201LL, 1024348434201LL, 1210024200121LL, 1212225222121LL, 1214428244121LL, 1232346432321LL, 1234567654321LL, 4000008000004LL, 4004009004004LL };

inline int solve() {
	long long a, b;
	C(lld,a); C(lld,b);

	long long *pa = lower_bound( fp, fp+39, a );
	long long *pb = lower_bound( fp, fp+39, b );

	if( binary_search( fp,fp+39,b ) ) {
		return pb-pa+1;
	} else {
		return pb-pa;
	}
}

int main() {
	int t, i;

	for( C(d,t), i = 1; i <= t; i++ ) {
		printf( "Case #%d: %d\n", i, solve() );
	}

	return 0;
}
