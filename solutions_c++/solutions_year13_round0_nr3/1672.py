#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
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

#define _DEBUG 1
#ifdef _DEBUG
	#define DEBUG printf
#else
	#define DEBUG if (0) printf
#endif

// NTU The Lyons' Template
//----------------------------------------------------------------------

bool palin( LL n )
{
	LL c = n, d=0LL;
	while (c)
	{
		d = (d*10LL) + c%10LL;
		c /= 10LL;
	}
	return (d == n);
}

int main()
{
	vector <LL> FS;
	REP (x,1,10000001)
		if (palin(x) && palin( (LL)x*x ))
		{
			//printf("> %d %I64d\n", x, (LL)x*x);
			FS.pb( (LL)x * x );
		}
	
	int T;
	scanf("%d", &T);
	REP (TT, 1, T+1)
	{
		LL A, B;
		scanf("%I64d%I64d", &A, &B);
		printf( "Case #%d: %d\n", TT, (int)(upper_bound( ALL(FS), B ) - lower_bound( ALL(FS), A )) );
	}
	
	return 0;
}
