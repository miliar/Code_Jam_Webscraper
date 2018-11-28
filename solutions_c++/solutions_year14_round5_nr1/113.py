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

const int MAX = 1000007;
int N;
ll p, q, r, s;
ll in[MAX];

void Solve(int tc)
{
	cin >> N >> p >> q >> r >> s;
	REP(i, N)
	{
		in[i] = (i * p + q) % r + s;
		if (i) in[i] += in[i-1];
	}
	ll res = 0, S = in[N-1];
	REP(i, N)
	{
		ll S1 = (i?in[i-1]:0), S2, S3;
		if (S-S1 <= S1)
			res = max(res, S-S1);
		else
		{
			// S1, S2 <= S3
			int be = i, en = N-1, f = i-1;
			while (be <= en)
			{
				int m = (be+en) / 2;
				S2 = in[m]-in[i-1], S3 = S-S1-S2;
				if (S1 <= S3 && S2 <= S3)
				{
					f = m;
					be = m+1;
				}
				else
					en = m-1;
			}
			S2 = in[f]-in[i-1], S3 = S-S1-S2;
			res = max(res, S1+S2);
			// S1, S3 <= S2
			be = i, en = N-1, f = N-1;
			while (be <= en)
			{
				int m = (be+en) / 2;
				S2 = in[m]-in[i-1], S3 = S-S1-S2;
				if (S1 <= S2 && S3 <= S2)
				{
					f = m;
					en = m-1;
				}
				else
					be = m+1;
			}
			S2 = in[f]-in[i-1], S3 = S-S1-S2;
			res = max(res, S1+S3);
			// S2, S3 <= S1
			be = i, en = N-1, f = i-1;
			while (be <= en)
			{
				int m = (be+en) / 2;
				S2 = in[m]-in[i-1], S3 = S-S1-S2;
				if (S2 <= S1)
				{
					f = m;
					be = m+1;
				}
				else
					en = m-1;
			}
			S2 = in[f]-in[i-1], S3 = S-S1-S2;
			if (S3 <= S1)
				res = max(res, S2+S3);
		}
	}
	printf("Case #%d: %.12lf\n", tc, (double)res / (double)S);
}

int main()
{
	int T;
	scanf("%d\n", &T);
	FOR(tc,1,T) Solve(tc);

	return 0;
}