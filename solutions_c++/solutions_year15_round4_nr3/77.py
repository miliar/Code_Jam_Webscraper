#pragma comment(linker, "/STACK:512000000")
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <sstream>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

typedef long double ld;
typedef long long ll;
typedef pair<int, int> pii;

const int NMAX = 10005;
const int CMAX = 205;

map<string, int> num;
string s[NMAX];
int ty[NMAX];

int get_num(string& w)
{
	if (num.count(w) == 0)
	{
		int id = (int)num.size();
		num.insert(mp(w, id));
		s[id] = w;
	}
	return num[w];
		
}

vector<int> t[CMAX];

int N;

struct Edge
{
	int v, c, f, e;
};

vector<Edge> g[NMAX];

void add_edge(int u, int v)
{
	Edge e;
	e.v = v;
	e.c = 1;
	e.f = 0;
	e.e = (int)g[v].size();
	g[u].pb(e);

	e.v = u;
	e.c = 0;
	e.e = (int)g[u].size() - 1;
	g[v].pb(e);
}

int src, dst;

bool used[NMAX];
int pr[NMAX];

void make_flow()
{
	int v = dst;
	while (v != src)
	{
		g[v][pr[v]].f--;
		int u = g[v][pr[v]].v;
		int id = g[v][pr[v]].e;
		g[u][id].f++;
		v = u;
	}
}

bool bfs()
{
	forn(i, N)
	{
		used[i] = 0;
		pr[i] = -1;
	}

	queue<int> q;
	q.push(src);
	used[src] = true;
	
	while (!q.empty())
	{
		int u = q.front(); q.pop();

		forv(i, g[u])
		{
			int v = g[u][i].v;
			if (g[u][i].f < g[u][i].c && !used[v])
			{
				used[v] = true;
				q.push(v);
				pr[v] = g[u][i].e;

				if (v == dst)
				{
					make_flow();
					return true;
				}
			}				
		}
	}
	return false;
}

void solve(int test)
{
	cerr << test << endl;
	num.clear();
	memset(ty, 0, sizeof(ty));

    printf("Case #%d: ", test);

	int cnt; scanf("%d\n", &cnt);

	int n1, n2;

	forn(i, cnt)
	{
		t[i].clear();
		string str;
		getline(cin, str);
		istringstream sin(str);
		string w;
		while (sin >> w)
		{
			if (w == "") break;
			int id = get_num(w);
			if (i == 0) ty[id] |= 1;
			else if (i == 1) ty[id] |= 2;
			else t[i].pb(id);
		}

		if (i == 1) n1 = (int)num.size();
	}
	n2 = (int)num.size() - n1;
	N = n1 + 2 * n2 + 2;

	src = N - 2;
	dst = N - 1;

	forn(i, N) g[i].clear();

	int ans = 0;
	forn(i, n1)
	{
		if (ty[i] == 1)
			add_edge(src, i);
		if (ty[i] == 2)
			add_edge(i, dst);
		if (ty[i] == 3)
			ans++;
	}	

	for (int i = 2; i < cnt; i++)
	{
		forv(j, t[i])
		{
			forv(k, t[i])
			{
				if (t[i][j] == t[i][k]) continue;
				int u = t[i][j];
				int v = t[i][k];				
				if (u < n1 && (ty[u] == 3 || ty[u] == 2)) continue;
				if (v < n1 && (ty[v] == 3 || ty[v] == 1)) continue;

				if (u >= n1) u += n2;
				add_edge(u, v);				 
			}
		}
	} 

	for (int i = n1; i < n1 + n2; i++)
		add_edge(i, i + n2); 

	while (bfs()) ans++;

	cout << ans << endl;
	
}
int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);

    int tc;
    scanf("%d\n", &tc);
    forn(it, tc) solve(it + 1);
    
    return 0;
}
