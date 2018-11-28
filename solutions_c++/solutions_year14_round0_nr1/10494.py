#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
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

bool num[20];

void play() {
	int r;
	scanf("%d", &r); --r;
	REP(y,0,4)
		REP(x,0,4) {
			int z;
			scanf("%d", &z);
			num[z] &= (y==r);
		}
}

void solve(int T) {
	RESET(num,1);
	play();
	play();
	int ans = 0;
	REP( x,1,17 )
		if (num[x]) {
			if (ans == 0) ans = x;
			else ans = -1;
		}
	
	printf("Case #%d: ", T);
	switch (ans) {
		case 0	: printf("Volunteer cheated!\n");	break;
		case -1	: printf("Bad magician!\n");		break;
		default	: printf("%d\n",ans);				break;
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	REP (t,0,T) solve(t+1);
	return 0;
}
