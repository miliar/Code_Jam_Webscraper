#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <vector>
#include <memory.h>
#include <map>
#include <set>
#include <bitset>
#include <algorithm>
#include <cmath>
#include <stack>
#include <string>
#include <cstring>
#include <string.h>
#include <sstream>
#include <cmath>
#include <math.h>
#include <queue>
#include <deque>
#include <cassert>
#include <time.h>

#define forn(i,n) for (int i = 0; i < (int)n; i++)
#define fornd(i, n) for (int i = (int)n - 1; i >= 0; i--)
#define forab(i,a,b) for (int i = (int)a; i <= (int)b; i++)
#define forabd(i, b, a) for (int i = (int)(b); i >= (int)(a); i--)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define _(a, val) memset (a, val, sizeof (a))
#define sz(a) (int)(a).size()
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()

#ifdef _DEBUG
#define dbg(...) {fprintf(stderr, __VA_ARGS__); fflush(stderr);}
#define dbgx(x) {cerr << #x << " = " << x << endl;}
#define dbgv(v) {cerr << #v << " = {"; for (typeof(v.begin()) it = v.begin(); it != v.end(); it ++) cerr << *it << ", "; cerr << "}"; cerr << endl;}
#else
#define dbg(...) { }
#define dbgx(x) { }
#define dbgv(v) { }
#endif

typedef long long lint;
typedef unsigned long long ull;
typedef long double ld;

const lint LINF = 1000000000000000000LL;
const int INF = 1000000000;
const long double eps = 1e-9;
const long double PI = 3.1415926535897932384626433832795l;

using namespace std;

void prepare (string s)
{
#ifdef _DEBUG
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
#else
	if (s.length() != 0)
	{
		freopen ((s + ".in").c_str(), "r", stdin);
		freopen ((s + ".out").c_str(), "w", stdout);
	}
#endif
}

const int NMAX = 155;
int m, n;
char tmp[NMAX];
string s[NMAX];
int a[NMAX];
int ans_node, ans_cnt;

void read()
{
	scanf("%d %d\n", &m, &n);
	forn(i, m)
	{
		scanf("%s", tmp);
		s[i] = tmp;
	}
}

void upd(int val)
{
	if (val > ans_node)
	{
		ans_node = val;
		ans_cnt = 1;
	}
	else
		if (val == ans_node)
		{
			ans_cnt ++;
		}
}

int get()
{
	bool used[NMAX];
	_(used, 0);
	forn(i, m) used[a[i]] = true;
	forn(i, n) if (!used[i]) return -1;
	int res = 0;
	forn(i, n)
	{
		vector<string> v;
		forn(j, m)
		{
			if (a[j] == i)
				v.pb ( s[j] );
		}
		sort(all(v));
		int r = 0;
		forn(i, sz(v)) r += sz(v[i]);
		for(int j = 1; j < sz(v); j++)
		{
			for(int k = 0; k < min(sz(v[j]), sz(v[j - 1])); k++)
			{
				if (v[j][k] == v[j - 1][k])
					r --;
				else
					break;
			}
		}
		res += r + 1;
	}
	return res;
}

void go(int id)
{
	if (id == m)
	{
		upd( get() );
		return;
	}
	
	for(int i = 0; i < n; i++)
	{
		a[id] = i;
		go( id + 1 );
	}
}

void solve()
{
	ans_node = 0;
	ans_cnt = 0;
	go( 0 );
	
	printf("%d %d\n", ans_node, ans_cnt);
}

int main ()
{
	prepare ("");
	
	int t;
	scanf("%d", &t);
	forn(i, t)
	{
		printf("Case #%d: ", i + 1);
		read();
		solve();
	}

	return 0;
}
