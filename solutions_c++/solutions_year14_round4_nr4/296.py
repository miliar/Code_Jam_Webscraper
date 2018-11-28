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

const int MOD = 1000000007;
int M, N;
string in[10];

int nodes(vector<string> & v)
{
	sort(v.begin(), v.end());
	int res = 1;
	REP(i, v.size())
	{
		res += v[i].size();
		if (i)
		{
			int j = 0;
			while (j < v[i].size() && j < v[i-1].size() && v[i][j] == v[i-1][j])
				++j;
			res -= j;
		}
	}
	return res;
}

vector<string> vs[10];

void Solve(int tc)
{
	cin >> M >> N;
	REP(i, M) cin >> in[i];

	int X = 1;
	REP(i, M) X *= N;

	int res1 = 0, res2 = 0;
	REP(i, X)
	{
		REP(j, N) vs[j].clear();
		int temp = i;	
		REP(j, M)
		{
			vs[temp%N].push_back(in[j]);
			temp /= N;
		}
		bool ok = true;
		REP(j, N)
			if (vs[j].empty())
				ok = false;
		if (!ok) continue;

		int act = 0;
		REP(j, N)
			act += nodes(vs[j]);
		if (act > res1) { res1 = act; res2 = 0; }
		if (act == res1) ++res2;
	}
	printf("Case #%d: %d %d\n", tc, res1, res2);
}

int main()
{
	int T;
	scanf("%d\n", &T);
	FOR(tc,1,T) Solve(tc);

	return 0;
}