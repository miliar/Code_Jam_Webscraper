#include <cstdio>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <vector>
#include <string>
#include <string.h>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <numeric>
#include <cctype>
#include <bitset>
#include <cassert>
#define fi first
#define se second
#define rep(i,n) for(int i = 0; i < (n); ++i)
#define rrep(i,n) for(int i = 1; i <= (n); ++i)
#define drep(i,n) for(int i = (n)-1; i >= 0; --i)
#define gep(i,g,j) for(int i = g.head[j]; i != -1; i = g.e[i].next)
#define each(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define rng(a) a.begin(),a.end()
#define maxs(x,y) x = max(x,y)
#define mins(x,y) x = min(x,y)
#define pb push_back
#define sz(x) (int)(x).size()
#define pcnt __builtin_popcount

using namespace std;
typedef long long int ll;
typedef pair<string, string> P;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<P> vp;
inline int in() { int x; scanf("%d", &x); return x; }

inline void priv(vi a) { rep(i, sz(a)) printf("%d%c", a[i], i == sz(a) - 1 ? '\n' : ' '); }
template<typename T>istream& operator>>(istream&i, vector<T>&v)
{
	for (T&x : v)i >> x; return i;
}
template<typename T>string join(vector<T>&v)
{
	stringstream s; for (T&x : v)s << ' ' << x; return s.str().substr(1);
}
template<typename T>ostream& operator<<(ostream&o, vector<T>&v)
{
	if (sz(v))o << join(v); return o;
}

const int MX = 100005, INF = 1001001001;
const ll LINF = 1e18;
const double eps = 1e-10;

struct Solver
{
	void solve(int cno)
	{
		int n = in();
		int f[26] = { 0 };
		int sum = 0;
		rep(i, n)
		{
			f[i] = in();
			sum += f[i];
		}
		if (n == 2)
		{
			printf("Case #%d: ", cno);
			while (f[0] > 0)
			{
				printf("%c%c ", 'A', 'B');
				f[0]--;
			}
			printf("\n");
			return;
		}
		printf("Case #%d: ", cno);
		while (sum > 0)
		{
			int mx = 0, ind = 0;
			rep(i, n)
			{
				mx = max(mx, f[i]);
				if (f[i] == mx)
					ind = i;
			}
			f[ind]--;
			sum--;
			printf("%c", ind + 'A');
			if (sum == 0)
				break;
			int mx1 = 0, ind1 = 0;
			rep(i, n)
			{
				mx1 = max(mx1, f[i]);
				if (f[i] == mx1)
					ind1 = i;
			}
			bool b = false;
			f[ind1]--;
			sum--;
			rep(i, n)
			{
				if (f[i] > sum - f[i])
				{
					b = true;
					break;
				}
			}
			if (b)
			{
				f[ind1]++;
				sum++;
				printf(" ");
			}
			else
				printf("%c ", ind1 + 'A');
		}
		printf("\n");
	}
};

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tn = in();
	rrep(ti, tn)
	{
		Solver solver;
		solver.solve(ti);
	}
	return 0;
}

