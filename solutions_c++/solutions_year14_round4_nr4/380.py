#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker,"/STACK:64000000")
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <cassert>
#include <time.h>
#include <bitset>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a,b) memset( (a), b, sizeof( a ) )
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()
#ifdef WIN32
#define dbg(...) {fprintf(stderr, __VA_ARGS__); fflush(stderr);}
#define dbgx(x) {cerr << #x << " = " << x << endl;}
#define dbgv(v) {cerr << #v << " = {"; for (typeof(v.begin()) it = v.begin(); it != v.end(); it ++) cerr << *it << ", "; cerr << "}"; cerr << endl;}
#else
#define dbg(...) { }
#define dbgx(x) { }
#define dbgv(v) { }
#endif

typedef unsigned long long ull;
typedef long long lint;
typedef pair < int , int > pii;
typedef long double ld;

const int INF = 1000 * 1000 * 1000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-9;

void prepare()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
}

const int nmax = 105;

struct Trie
{
	int nxt[nmax][26];
	int N;

	void clear()
	{
		_(nxt,-1);
		N = 1;
	}

	void addVert(int _p,int _pc)
	{
		nxt[_p][_pc] = N;
		N++;
	}

	void addWord(string &s)
	{
		int len = sz(s);
		int v = 0;
		for (int i = 0; i < len; i ++)
		{
			char c = s[i] - 'A';
			if (nxt[v][c] == -1)
			{
				addVert(v,s[i] - 'A');
			}
			v = nxt[v][c];
		}
	}
}t[5];

int m, n;
char buf[200];
string s[nmax];
int ans = 0, ways = 0;
int col[nmax], used[nmax];

void read()
{
	scanf("%d%d",&m,&n);
	for (int i = 0; i < m; i ++)
	{
		scanf("%s",buf);
		s[i] = buf;
	}
}

int calcSize()
{
	for (int i = 0; i < n; i ++)
		t[i].clear();
	for (int i = 0; i < m; i ++)
	{
		t[col[i]].addWord(s[i]);
	}
	int ret = 0;
	for (int i = 0; i < n; i ++)
		ret += t[i].N;
	return ret;
}

void rec(int i)
{
	if (i == m)
	{
		for (int j = 0; j < n; j ++)
		{
			if (used[j] == 0)
			{
				return;
			}
		}
		int cur = calcSize();
		if (cur > ans)
		{
			ans = cur;
			ways = 1;
		}
		else
		if (cur == ans)
		{
			ways++;
		}
		return;
	}

	for (int c = 0; c < n; c ++)
	{
		col[i] = c;
		used[c]++;
		rec(i + 1);
		col[i] = -1;
		used[c]--;
	}
}

bool solve()
{
	read();
	_(col, -1);
	ans = ways = 0;
	rec(0);
	printf("%d %d\n", ans, ways);
	return false;
}

int main()
{
	prepare();
	int t;
	scanf("%d",&t);
	for (int i = 0; i < t; i ++)
	{
		dbg("Test %d\n", i);
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}
