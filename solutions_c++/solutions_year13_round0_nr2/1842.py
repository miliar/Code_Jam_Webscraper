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

int lawn[102][102];

bool solve()
{
	int R, C;
	RESET( lawn, 0 );
	scanf("%d%d", &R, &C);
	REP(y,0,R) REP(x,0,C) scanf("%d", &lawn[y][x]);
	
	int RH[R+3], CH[C+3];
	RESET( RH, 0 );
	RESET( CH, 0 );
	REP(y,0,R)
	{
		REP(x,0,C) RH[y] = max( RH[y], lawn[y][x] );
		REP(x,0,C) if (lawn[y][x] < RH[y])
		{
			if ((CH[x] != 0) && (CH[x] != lawn[y][x])) return false;
			CH[x] = lawn[y][x];
		}
	}
	
	REP(x,0,C) REP(y,0,R)
		if ((CH[x]!=0) && (lawn[y][x] > CH[x])) return false;
	
	return true;
}

int main()
{
	int T;
	scanf("%d", &T);
	REP( TT, 1, T+1 )
		printf( "Case #%d: %s\n", TT, ((solve())?"YES":"NO") );
	return 0;
}
