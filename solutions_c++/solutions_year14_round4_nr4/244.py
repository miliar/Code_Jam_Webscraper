#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <vector>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <deque>
#include <cassert>

using namespace std;

#ifdef WIN32
	#define I64 "%I64d"
#else
	#define I64 "%lld"
#endif

typedef long long ll;

#define F first
#define S second
#define mp make_pair
#define pb push_back
#define all(s) s.begin(), s.end()
#define sz(s) (int(s.size()))
#define fname "a"
#define ms(a,x) memset(a, x, sizeof(a))
#define forit(it,s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); ++it)
#define MAXN 20
#define MAXV 1000

int n, m;
int ans, ans2;
vector <int> a[MAXN];
int g[MAXV][26], cc;
int c[MAXV][26];
string s[MAXN];
char ch[MAXV];

inline int build(int ind)
{
	++cc;
	int res = 1;
	for (int i = 0; i < sz(a[ind]); ++i)
	{
		int pos = a[ind][i];
		int len = s[pos].size();
		int cur = 0;
		for (int j = 0; j < len; ++j)
		{
			int t = s[pos][j] - 'A';
			if (c[cur][t] != cc)
			{
				c[cur][t] = cc;
				g[cur][t] = res++;
			}
			cur = g[cur][t];
		}
	}
	return res;
}

inline void go(int v)
{
	if (v == m)
	{
		bool ok = 1;
		for (int i = 0; i < n && ok; ++i)
			if (sz(a[i]) == 0)
				ok = 0;
		if (!ok) return;
		int s = 0;
		for (int i = 0; i < n; ++i)
			s += build(i);
		if (s > ans)
		{
			ans = s;
			ans2 = 0;
		}
		if (s == ans)
			++ans2;
		return;
	}
	for (int i = 0; i < n; ++i)
	{
		a[i].pb(v);
		go(v + 1);
		a[i].pop_back();
	}
}

inline void solve()
{
	scanf("%d%d", &m, &n);
	for (int i = 0; i < m; ++i)
	{
		scanf("%s", ch);
		s[i] = ch;
	}
	for (int i = 0; i < n; ++i)
		a[i].clear();
	ans = 0;
	ans2 = 0;
	go(0);
	printf("%d %d\n", ans, ans2);
}

int main()
{
	#ifdef LOCAL
	freopen(fname".in", "r", stdin);
	freopen(fname".out", "w", stdout);
	#endif

	int tt;
	scanf("%d", &tt);
	for (int t = 0; t < tt; ++t)
	{
		printf("Case #%d: ", t + 1);
		solve();
	}
	return 0;
}
