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

//#define _DEBUG 1
#ifdef _DEBUG
	#define DEBUG printf
#else
	#define DEBUG if (0) printf
#endif

// NTU The Lyons' Template
//----------------------------------------------------------------------

#define INF 100000

int N;
int M[102];
LL DP[12][12000];

LL f( int x, LL cur )
{
	if (x >= N) return 0;
	if (DP[x][cur]!= -1) return DP[x][cur];
	LL &ret = DP[x][cur] = INF;
	
	DEBUG("fu %d %I64d\n", x, cur);
	
	if (cur > M[x]) ret = f( x+1, cur+M[x] );
	else
	{
		ret = min( ret, 1LL + f( x+1, cur ) ); //remove
		
		//add
		if (cur > 1LL)
		{
			LL lho = ((M[x]-cur)/(cur-1LL))+1LL;
			
			REP( y,1,21 )
				if ((1<<y) > lho)
				{
					DEBUG("\n>> %d %I64d %I64d => %d\n", x, cur, lho, y);
					ret = min( ret, y + f( x+1, cur + M[x] + ((1<<y)-1)*(cur-1LL)) );
					break;
				}
			//DEBUG(">2\n");
		}
	}
	
	return ret;
}

void solve( int T )
{
	int A;
	RESET( M, 0 );
	RESET( DP, -1 );
	scanf("%d%d", &A, &N);
	REP(x,0,N) scanf("%d", &M[x]);
	sort( M, M+N );
	DEBUG( "wew\n" );
	printf("Case #%d: %I64d\n", T, f( 0, A ));
}

int main()
{
	int T;
	scanf("%d", &T);
	REP( TT, 0, T ) solve( TT+1 );
	return 0;
}
