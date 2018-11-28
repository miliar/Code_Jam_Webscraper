#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <utility>
#include <sstream>
#include <string>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <cstring>
using namespace std;

#define fi first
#define sc second
#define MP make_pair
#define pb push_back
#define PI acos(-1.0) //alternative #define PI (2.0 * acos(0.0))
#define vi vector<int>
#define vii vector<ii>
#define ALL(c) (c).begin(), (c).end()
#define RESET( c,a ) memset( (c), a, sizeof(c) )
#define REP( a,b,c ) for ( int a=b, _c=c; a<_c; ++a )
#define RED( a,b,c ) for ( int a=b, _c=c; a>=_c; --a )
#define REPI( it, c ) for ( __typeof( (c).begin() ) it=(c).begin(); it!=(c).end(); ++it )

const int big = 2000000000;
const double INF = 1e9;
const double EPS = 1e-9;

typedef long long LL;
typedef pair<int,int> pii;
typedef pair<LL,LL> pLL;

//#define _DEBUG 1
#ifdef _DEBUG
	#define DEBUG printf
#else
	#define DEBUG if (0) printf
#endif

// NTU The Lyons' Template
//----------------------------------------------------------------------

void solve( int T )
{
	int N;
	LL P;
	cin >> N >> P;
	
	//DEBUG("%d %I64d\n", N, P);
	
	LL cura=0LL;
	LL curb=(1LL<<N)-1LL;
	vector <LL> a, b;
	
	REP( x, 0, N+1 )
	{
		a.pb( min( cura, (1LL<<N)-1LL ) );
		b.pb( max( curb, 0LL ) );
		cura = (cura+1LL)<<1;
		curb -= ( 1LL<<x );
	}
	
	//REPI( it, a ) DEBUG( "> %I64d\n", *it );
	
	printf( "Case #%d:", T );
	
	int idx = 0;
	cura = N-1;
	curb = P;
	while ( (cura>=0) && (1LL<<cura) < curb )
	{
		curb -= (1LL<<cura);
		--cura;
		++idx;
	}
	printf( " %I64d", a[idx] );
	
	idx=0;
	cura = N;
	curb = P;
	while ((1LL<<cura) > curb)
	{
		--cura;
		++idx;
	}
	printf( " %I64d\n", b[idx] );
	
}

int main()
{
	int T;
	scanf("%d", &T);
	REP(TT,0,T) solve( TT+1 );
	return 0;
}
