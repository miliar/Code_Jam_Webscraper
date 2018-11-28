#pragma comment(linker, "/STACK:32000000")
#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <stdarg.h>
#include <memory.h>
#include <string.h>

using namespace std;

const double pi = 3.1415926535897932384626433832795;
#define ALL(x) x.begin(), x.end()
typedef long long LL;
#define MP make_pair
#define PB push_back
#define CLR(a,b) memset(a, b, sizeof(a))
template<class T> inline T Sqr(const T &x) { return x*x; }
template<class T> inline T Abs(const T &x) { return x >= 0 ? x : -x; }

void init()
{

}


#define maxn 60

int n, k1, k2;
char buf[maxn];
bool g[maxn][maxn];
bool seen[maxn];
vector<pair<int, int> > elems;
int best, m, n_used = 0;
bool used[maxn];

void dfs(int v)
{
	seen[v] = true;
	if (v < n) k1++; else k2++;
	for (int i = 0; i < 2 * n; i++)
		if (g[v][i] && !seen[i])
			dfs(i);
}

void rec(int cur_sum, int diff, int cnt, int idx)
{
	if (diff == 0)
	{
		if (n_used == m)
		{
			best = min(best, cur_sum + cnt * cnt / 4);
			return;
		}
		for (int i = 0; i < m; i++)
			if (!used[i])
			{
				used[i] = true;
				n_used++;
				rec(cur_sum + cnt * cnt / 4, elems[i].first - elems[i].second, elems[i].first + elems[i].second, i);
				used[i] = false;
				n_used--;
				return;
			}
	}

	// looking for next
	for (int j = idx + 1; j < m; j++) if (!used[j])
	{
		used[j] = true;
		n_used++;
		rec(cur_sum, diff + elems[j].first - elems[j].second, cnt + elems[j].first + elems[j].second, j);
		used[j] = false;
		n_used--;
	}
}

void solvecase()
{
	scanf("%d", &n);
	int n_edges = 0;
	CLR(g, 0);
	for (int i = 0; i < n; i++)
	{
		scanf("%s", buf);
		for (int j = 0; j < n; j++) if (buf[j] == '1')
		{
			g[i][j+n] = true;
			g[j+n][i] = true;
			n_edges++;
		}
	}
	elems.clear();
	CLR(seen, 0);
	for (int i = 0; i < 2 * n; i++)
		if (!seen[i])
		{
			k1 = 0;
			k2 = 0;
			dfs(i);
			elems.push_back(MP(k1, k2));
		}

	best = 100000;
	m = (int)elems.size();
	//printf("%d\n", m);
	//for (auto e : elems) printf("(%d, %d)\n", e.first, e.second);

	rec(0, 0, 0, 0);
	printf("%d", best - n_edges);
}

void solve() {
	init();
	int n_tests;
	scanf("%d", &n_tests);
	for (int i = 1; i <= n_tests; i++)
	{
		printf("Case #%d: ", i);
		solvecase();
		printf("\n");
	}
}

#define problem_letter "D"
//#define fname "testcpp"
#define fname problem_letter "-small-attempt0"
//#define fname problem_letter "-small-attempt1"
//#define fname problem_letter "-small-attempt2"
//#define fname problem_letter "-large"
//#define fname problem_letter "-small-practice"
//#define fname problem_letter "-large-practice"

int main()
{
	freopen(fname ".in", "r", stdin);
	freopen(fname ".out", "w", stdout);
	solve();
	return 0;
}
