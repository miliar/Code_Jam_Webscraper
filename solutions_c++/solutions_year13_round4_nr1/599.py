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

const LL MOD = 1000002013LL;

void solve( int T )
{
	int N, M;
	int o, e, p;
	stack <pii> cur;
	priority_queue <pii> ip, op;
	
	LL ori=0LL, fake=0LL;
	
	cin >> N >> M;
	while (M--)
	{
		cin >> o >> e >> p;
		ip.push( MP( -o,p ) );
		op.push( MP( -e,p ) );
		ori = (ori + (( (((LL)(e-o) * N - ((LL)(e-o) * (e-o-1LL)/2LL)) %MOD) * p ) %MOD )) %MOD;
	}
	
	DEBUG("lho %d %d %d %d\n", ip.top().fi, ip.top().sc, op.top().fi, op.top().sc);
	
	while (!op.empty())
	{
		if ((!ip.empty()) && (-ip.top().fi <= -op.top().fi))
		{
			pii t = ip.top(); ip.pop();
			cur.push( MP( -t.fi, t.sc ) );
			DEBUG( "> in %d %d\n", -t.fi, t.sc );
		}
		else
		{
			pii t=cur.top(), u=op.top();
				cur.pop(); op.pop();
			u.fi = -u.fi;
			
			DEBUG( "> out %d %d\n", u.fi, u.sc );
			
			while (u.sc > 0)
			{
				if (u.sc > t.sc)
				{
					DEBUG( ">  > by %d %d\n", t.fi, t.sc );
					fake += ( (((LL)(u.fi-t.fi) * N - ((LL)(u.fi-t.fi) * (u.fi-t.fi-1LL)/2LL)) %MOD ) * (LL)t.sc ) %MOD;
					u.sc -= t.sc;
					t = cur.top();
					cur.pop();
				}
				else
				{
					DEBUG( ">  > end %d %d\n", t.fi, t.sc );
					fake += ( (((LL)(u.fi-t.fi) * N - ((LL)(u.fi-t.fi) * (u.fi-t.fi-1LL)/2LL)) %MOD ) * (LL)u.sc ) %MOD;
					t.sc -= u.sc;
					u.sc = 0;
				}
			}
			if (t.sc > 0)
			{
				DEBUG( "> retake %d %d\n", t.fi, t.sc );
				cur.push( t );
			}
		}
	}
	
	LL sel = ori - fake;
	while (sel < 0LL) sel += MOD;
	printf( "Case #%d: %I64d\n", T, sel );
	
}

int main()
{
	int T;
	scanf("%d", &T);
	REP(TT,0,T) solve( TT+1 );
	return 0;
}
