#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>
#include <cassert>
#include <map>

using namespace std;

typedef long long ll;
typedef long double ldb;

#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)

const int MAXN = 1e6 + 10;

int n, d;

struct list {
	int to;
	list *nxt;
};

list mem[MAXN];
list *h[MAXN];

int s[MAXN];

struct event {
	int x;
	bool f;

	event(): x(), f() {}
	event(int x, bool f): x(x), f(f) {}

	bool operator <(const event & e) const {
		if (x != e.x)
			return x < e.x;
		return f < e.f;
	}
};

vector<event> e;

void dfs(int v, int mn, int mx) {
	if (mn > mx)
		return;

	e.push_back(event(mn, false));
	e.push_back(event(mx, true));

	for(list *tmp = h[v]; tmp; tmp = tmp->nxt) {
		int u = tmp->to;
		dfs(u, max(mn, s[u] - d), min(mx, s[u]));
	}
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	scanf("%d ", &T);
	forn(testNum, T) {
		printf("Case #%d: ", testNum + 1);

		scanf("%d%d", &n, &d);
		
		forn(i, n)
			h[i] = NULL;

		int s0, as, cs, rs, m0, am, cm, rm;
		scanf("%d%d%d%d%d%d%d%d", &s0, &as, &cs, &rs, &m0, &am, &cm, &rm);

		s[0] = s0;
		ll _s = s0, _m = m0; 

		forab(i, 1, n) {
			_s = (_s * as + cs) % rs;
			_m = (_m * am + cm) % rm;

			s[i] =_s;

			int v = _m % i;
			mem[i].to = i;
			mem[i].nxt = h[v];
			h[v] = &mem[i];
		}

		e.clear();
		dfs(0, s[0] - d, s[0]);

		sort(e.begin(), e.end());
		int k = 0, ans = 0;
		for(auto cur : e) {
			k += (cur.f ? -1 : 1);
			ans = max(ans, k);
		}

		printf("%d\n", ans);
	}
	return 0;
}
