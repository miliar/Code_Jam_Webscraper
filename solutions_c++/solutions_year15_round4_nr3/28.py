#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <cassert>
#include <numeric>
#include <string>
#include <cstring>
#include <cmath>
using namespace std;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif

typedef long long int int64;

const int maxn = (int) 1e5 + 100;
const int maxm = (int) 1e5 + 100;




struct Edge
{
	int to, cap, flow;
	int rid;
	Edge() : to(), cap(), flow(), rid() {}
	Edge(int _to, int _cap, int _flow, int _rid) : to(_to), cap(_cap), flow(_flow), rid(_rid) {}
};

vector <Edge> g[2 * maxn]; 


void addEdge(int v, int to, int cap)
{
	g[v].push_back(Edge(to, cap, 0, (int) g[to].size() ) );
	g[to].push_back(Edge(v, 0, 0, (int) g[v].size() - 1) );
}

const int inf = (int) 1e9 + 100;
const int infF = (int) 1e9;
int d[2 * maxm];
int qu[maxn];

bool bfs(int n, int s, int t)
{
	for (int i = 0; i < n; i++)
		d[i] = -1;
	d[s] = 0;
	int qul = 0, qur = 0;
	qu[qur++] = s;

	while (qul < qur)
	{
		int v = qu[qul++];
		for (int i = 0; i < (int) g[v].size(); i++)
		{
			int nv = g[v][i].to;
			if (d[nv] != -1)
				continue;
			if (g[v][i].flow == g[v][i].cap)
				continue;
			d[nv] = d[v] + 1;
			qu[qur++] = nv;
		}
	}
	return d[t] != -1;
}

int gid[maxn];

int dfs(int v, int t, int income)
{
	if (income == 0 || v == t)
		return income;
	int answer = 0;
	for (int &cid = gid[v]; cid < (int) g[v].size(); cid++)
	{
		if (income - answer == 0)
			break;
		int nv = g[v][cid].to;
		if (d[nv] != d[v] + 1)
			continue;
		int ecap = g[v][cid].cap - g[v][cid].flow;
		if (ecap == 0)
			continue;
		int outcome = min(income - answer, ecap);
		int realoutcome = dfs(nv, t, outcome);

		answer += realoutcome;
		g[v][cid].flow += realoutcome;
		g[nv][g[v][cid].rid].flow -= realoutcome;

		if (realoutcome == outcome && outcome != ecap)
			break;

	}
	return answer;
}


int dinic(int n, int s, int t)
{
	int ans = 0;
	while (bfs(n, s, t) )
	{
		for (int i = 0; i < n; i++)
			gid[i] = 0;
		ans += dfs(s, t, inf);
//		fprintf(stderr, "ans = %d\n", ans);
	}
	return ans;
}










map <string, int> M;
char s[maxn];

void init()
{
	int numv = (int) M.size() * 2 + 2;
	M.clear();
	for (int i = 0; i < numv; i++)
		g[i].clear();
}

int getId(string _s)
{
	if (!M.count(_s) )
	{
		int sz = (int) M.size();
		M[_s] = sz;
		addEdge(2 + 2 * sz, 2 + 2 * sz + 1, 1);
	}
	return M[_s];
}

void addWord(string _s, int sid)
{
	int wid = getId(_s);
	if (sid == 0)
	{
		addEdge(0, 2 + 2 * wid, infF);
	}
	else if (sid == 1)
	{
		addEdge(2 + 2 * wid + 1, 1, infF);
	}
}

void readSentence(int sid)
{
	scanf("%[^\n]\n", s);
	string cur = "";
	vector <string> v;
	int len = strlen(s);
	for (int i = 0; i <= len; i++)
	{
		if (s[i] == ' ' || s[i] == 0)
		{
			if (cur != "")
			{
				v.push_back(cur);
				cur = "";
			}
		}
		else
		{
			cur.push_back(s[i] );
		}
	}
	for (int i = 0; i < (int) v.size(); i++)
	{
		addWord(v[i], sid);
	}
	if (sid == 2)
	{
		for (int i = 0; i < (int) v.size(); i++)
			for (int j = i + 1; j < (int) v.size(); j++)
			{
				int a = getId(v[i] );
				int b = getId(v[j] );
				if (a == b)
					continue;
				addEdge(2 + 2 * a + 1, 2 + 2 * b, infF);
				addEdge(2 + 2 * b + 1, 2 + 2 * a, infF);
			}
	}
}


void solve()
{
	init();

	int t;
	scanf("%d\n", &t);
	for (int i = 0; i < t; i++)
	{
		readSentence(min(i, 2) );
	}
	int ans = dinic(2 * (int) M.size() + 2, 0, 1);
	printf("%d\n", ans);
}

void multitest()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		printf("Case #%d: ", i);
		eprintf("Case #%d .. %d\n", i, n);
		solve();
	}


}

int main(int argc, char **)
{
	if (argc == 1)
		multitest();
	else
		solve();

	return 0;
}


