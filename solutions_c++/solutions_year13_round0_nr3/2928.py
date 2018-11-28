#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <iomanip>
#include <sstream>
#include <utility>
#include <string>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cmath>
#include <ctime>
#include <assert.h>
#include <string.h>
#include <limits>
using namespace std;

#define INF 100000000
#define PI 3.1415926535897932384626433832795
#define PI_HALF 1.570796327
#define EPS 1e-9

typedef unsigned int UI;
typedef long long LL;
typedef unsigned long long ULL;
typedef pair< int, int > PII;
typedef pair< LL, LL > PLL;
typedef vector< int > VI;
typedef vector< LL > VLL;
typedef vector< string > VS;
typedef vector< PII > VPII;
typedef vector< PLL > VPLL;

#define X first
#define Y second
#define PB push_back
#define MP make_pair
#define SZ(c) (int)(c).size()
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort( ALL( c ) )
#define SORT_(c,f) sort( ALL( c ), f )
#define FILL(x,v) memset( x, v, sizeof( x ) );

#define REP(i,n) for ( int i = 0, max_ = (n); i < max_; ++i )
#define REPD(i,n) for ( int i = (n) - 1; i >= 0; --i )
#define FOR(i,a,b) for ( int i = (a), max_ = (b); i < max_; ++i )
#define FORD(i,a,b) for ( int i = (a) - 1, min_ = (b); i >= min_; --i )

int ToInt ( string & s, int len ) { int r = 0; REP(i,len) { r *= 10; r += s[i] - '0'; } return r; }
int GCD ( int a, int b ) { return b != 0 ? GCD(b, a % b) : a; }
int LCM ( int a, int b ) { return a*(b / GCD(a,b)); }
LL Pow ( LL n, LL e ) { if ( e == 0 ) return 1; if ( e == 1 ) return n; else if ( e & 1 ) { LL t = Pow(n,e/2); return n*t*t; } else { LL t = Pow(n,e/2); return t*t; } }

bool IsPalindrome ( LL n )
{
	VI v;
	while ( n > 0 )
	{
		v.PB( n % 10 );
		n /= 10;
	}

	REP(i,SZ(v))
		if ( v[ i ] != v[ SZ(v) - 1 - i ] )
			return false;
	return true;
}

int main ()
{
	freopen( "C-small-attempt0.in", "r", stdin );
	freopen( "f.out", "w", stdout );

	const int MAX = 100001;

	VI v;
	FOR(i,1,MAX)
	{
		if ( !IsPalindrome( i ) ) continue;
		LL n = i*(LL)i;
		if ( !IsPalindrome( n ) ) continue;
		v.PB( n );
	}

	int T, A, B, C = 0;
	cin >> T;
	while ( T-- )
	{
		cin >> A >> B;
		auto s = lower_bound( ALL(v), A );
		auto e = lower_bound( ALL(v), B );
		if ( *e > B ) --e;
		LL res = e - s + 1;
		printf( "Case #%d: %I64d\n", ++C, res );
	}

	return 0;
}