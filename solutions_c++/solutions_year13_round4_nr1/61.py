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

const ll MOD = 1000002013LL;
int N, M;

struct rec
{
	int n, p;
	bool operator<(const rec & r) const
	{
		if (n != r.n)
			return n < r.n;
		return p > r.p;
	}
} in[2*1007];

ll add(ll a, ll b) { return (a+b) % MOD; }
ll mul(ll a, ll b) { return a*b%MOD; }

ll cost(ll a, ll b)
{
	if (a == b) return 0;
	ll d = b-a;
	ll res = ((ll)N+(N-d+1))*d / 2;
	if (res < 0)
		DEBUG("AAAAAAAAAAAAAAAAAAAAAAAAAA");
	return res % MOD;
}

void Solve(int tc)
{
	cin >> N >> M;
	ll real = 0, act = 0;
	REP(i, M)
	{
		int a, b, p;
		cin >> a >> b >> p;
		in[2*i].n = a;
		in[2*i].p = p;
		in[2*i+1].n = b;
		in[2*i+1].p = -p;
		real = add(real, mul(cost(a, b), p));
		if (real < 0)
			DEBUG("BBBBBBBBBBBBBBBBBBBBBBBBBB")
	}
	sort(in, in+2*M);

	priority_queue<pair<int, int> > manage;
	REP(i, 2*M)
	{
		if (in[i].p > 0)
			manage.push(make_pair(in[i].n, in[i].p));
		while (in[i].p < 0)
		{
			pair<int, int> temp = manage.top();
			manage.pop();
			int p = min(temp.second, -in[i].p);
			in[i].p += p;
			temp.second -= p;
			if (temp.second)
				manage.push(temp);
			act = add(act, mul(cost(temp.first, in[i].n), p));
			if (act < 0)
				DEBUG("CCCCCCCCCCCCCCCCCCCCCCCC");
		}
	}

	printf("Case #%d: %lld\n", tc, (real-act+MOD) % MOD);
}

int main()
{
	int T;
	scanf("%d\n", &T);
	FOR(tc,1,T) Solve(tc);

	return 0;
}