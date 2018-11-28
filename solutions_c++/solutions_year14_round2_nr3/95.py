#pragma comment(linker,"/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <sstream>
#include <stdio.h>

#include <algorithm>
#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <queue>
#include <deque>
#include <stack>

#include <cmath>
#include <string>

#include <cassert>
#include <time.h>
#include <memory.h>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a,b) memset( (a), b, sizeof( a ) )
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()

#define fi(n) for (int i = 0; i < (n); ++ i)
#define fj(n) for (int j = 0; j < (n); ++ j)
#define fin() for (int i = 0; i < n; ++ i)
#define fjm() for (int j = 0; j < m; ++ j)
#define forv(i, v) for (int i = 0; i < sz((v)); ++ i)


#ifdef _DEBUG
#define dbg(...) {fprintf(stderr, __VA_ARGS__); fflush(stderr);}
#define dbgx(x) {cerr << #x << " = " << x << endl;}
#else
#define dbg(...) { }
#define dbgx(x) { }
#endif

typedef unsigned long long ull;
typedef long long lint;
typedef pair < int, int > pii;
typedef long double ld;

const int INF = 1000 * 1000 * 1000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-9;

void prepare(string s)
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	if (sz(s) > 0)
	{
		freopen((s + ".in").c_str(), "r", stdin);
		freopen((s + ".out").c_str(), "w", stdout);
	}
#endif
}

const int MAXN = 54;
string zip[MAXN];

int g[MAXN][MAXN];
int n,m;
set< pair<string, int> > s;
void read()
{
	_(g, 0);
	cin >> n >> m;
	for (int i = 0; i < n;++ i)
	{
		cin >> zip[i];
	}
	fi(m)
	{
		int l,r;
		cin >> l >> r;
		-- l;
		-- r;
		g[l][r] = 1;
		g[r][l] = 1;
	}
	s.clear();
}

int prec[MAXN];


int get_top()
{
	int res = s.begin()->second;
	s.erase(s.begin());
	return res;
}

void push(int id)
{
	s.insert(mp(zip[id], id));
}

vector<int> a;
void upd_set()
{
	for (int i = 0; i < n; ++ i)
	{
		if (find(all(a), i) == a.end())
			s.insert(mp(zip[i], i));
	}

}

bool used[MAXN];
bool inA[MAXN];

void dfs(int x)
{
	used[x] = true;
	for (int i = 0 ; i < n; ++ i)
	{
		if (g[x][i] && !used[i])
			dfs(i);
	}
}

bool check()
{
	int k = a.back();
	int cur = a[sz(a) - 2];

	while (cur >= 0 && g[k][cur] == 0)
	{
		cur = prec[cur];
	}

	if (cur < 0)
		return false;

	_(used, false);
	_(inA, false);

	forv(i,a)
	{
		used[a[i]] = true;
	}
	prec[k] = cur;
	for (int id = k; id >= 0; id = prec[id])
	{
		dfs(id);
	}

	for (int i = 0; i < n; ++ i)
	{
		if (used[i] == false)
		{
			return false;
		}
	}

	return true;
}


void solve()
{
	fin()
	{
		s.insert(mp(zip[i], i));
	}
	a.clear();
	a.push_back(get_top());
	prec[a[0]] = -1;

	for (int i = 1; i < n; ++ i)
	{
		upd_set();
		a.push_back(get_top());
		while (!check())
		{
			a.pop_back();
			a.push_back(get_top());
		}
	}
	string ans;
	for (int i = 0; i < n; ++ i)
		ans += zip[a[i]];
	cout << ans;
}

int main()
{
	prepare("");

	int T;
	cin >> T;
	fi(T)
	{
		read();
		cout << "Case #" << i + 1 << ": ";
		cerr << "Case #" << i + 1 << ": " << endl;
		solve();
		cout << endl;
	}

	return 0;
}
