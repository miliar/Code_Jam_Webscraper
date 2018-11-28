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

ll N, P;
bool can_lose(ll n)
{
	ll res = 0, sz = 1LL<<N, smaller = n;
	while (smaller)
	{
		sz /= 2;
		res += sz;
		smaller = (smaller-1)/2;
	}
	return res >= P;
}

ll ans1()
{
	ll be = 0, en = (1LL<<N)-1, res = 0;
	while (be <= en)
	{
		ll m = (be+en) / 2;
		if (can_lose(m))
			en = m-1;
		else
		{
			res = m;
			be = m+1;
		}
	}
	return res;
}

bool can_win(ll n)
{
	ll res = (1LL<<N)-1, sz = 1LL<<N, smaller = n;
	while (smaller+1 < sz)
	{
		sz /= 2;
		res -= sz;
		smaller = (smaller+1)/2;
	}
	return res < P;
}

ll ans2()
{
	ll be = 0, en = (1LL<<N)-1, res = 0;
	while (be <= en)
	{
		ll m = (be+en) / 2;
		if (can_win(m))
		{
			res = m;
			be = m+1;
		}
		else
			en = m-1;
	}
	return res;
}

void Solve(int tc)
{
	cin >> N >> P;
	printf("Case #%d: %lld %lld\n", tc, ans1(), ans2());
}

int main()
{
	int T;
	scanf("%d\n", &T);
	FOR(tc,1,T) Solve(tc);

	return 0;
}