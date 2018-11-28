#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std; 

#define DEBUG(x) cerr << '>' << #x << ':' << x << endl;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

const int INF = 1<<29;
typedef long long ll;

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=n&(-n); return res; }

template<class T> void chmax(T & a, const T & b) { a = max(a, b); }
template<class T> void chmin(T & a, const T & b) { a = min(a, b); }
///////////////////////////////////////////////////////////////////////////////////////////////////////////////

const int MAX = 107;
int P, Q, N, H[MAX], G[MAX];

int dp[2][101][201][1000];
int go(int turn, int n, int h, int saved)
{
	if (n == N)
		return 0;

	int & res = dp[turn][n][h][saved];
	if (res != -1)
		return res;
	res = 0;

	if (turn == 0) // Diana
	{
		// save arrow
		res = max(res, go(1, n, h, saved+1));
		// shoot
		if (h-P <= 0)
			res = max(res, go(1, n+1, H[n+1], saved) + G[n]);
		else
			res = max(res, go(1, n, h-P, saved));
	}
	else
	{
		// shoot from saved
		if (h == H[n])
		{
			int hh = h;
			REP(i, saved)
			{
				hh -= P;
				if (hh <= 0)
				{
					res = max(res, go(1, n+1, H[n+1], saved-i-1) + G[n]);
					break;
				}
				res = max(res, go(1, n, hh, saved-i-1));
			}
		}
		
		if (h-Q <= 0)
			res = max(res, go(0, n+1, H[n+1], saved));
		else
			res = max(res, go(0, n, h-Q, saved));
	}
	return res;
}

void Solve(int tc)
{
	cin >> P >> Q >> N;
	REP(i, N)
		cin >> H[i] >> G[i];
	memset(dp, -1, sizeof(dp));
	printf("Case #%d: %d\n", tc, go(0, 0, H[0], 0));
}

int main()
{
	int T;
	scanf("%d\n", &T);
	FOR(tc,1,T) Solve(tc);

	return 0;
}