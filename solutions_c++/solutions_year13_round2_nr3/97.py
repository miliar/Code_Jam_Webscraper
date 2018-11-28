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

const int nmax = 1200000;

struct Trie
{
	int nxt[nmax][26];
	int leaf[nmax];
	int N;

	Trie()
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
			char c = s[i] - 'a';
			if (nxt[v][c] == -1)
			{
				addVert(v,s[i] - 'a');
			}
			v = nxt[v][c];
		}
		leaf[v] ++;
	}
}T;


void build_dictionary()
{
	freopen("dictionary.txt", "r", stdin);
	char str[250];
	string s;
	while (scanf("%s",str) >= 0)
	{
		s = str;
		T.addWord(s);
	}
}

void prepare()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
}

int dp[2][nmax][6];
char s[4005];
int len, cur, nxt;

inline void upd(int fid, int i, int j, int val)
{
	int &r = dp[fid][i][j];
	if (r == -1 || r > val)
	{
		r = val;
	}
}

bool solve()
{
	scanf("%s",s);
	len = strlen(s);
	cur = 0;
	nxt = 1;
	_(dp[cur], -1);
	upd(cur, 0, 5, 0);
	for (int pos = 0; pos < len; pos ++)
	{
		_(dp[nxt], -1);
		for (int v = T.N - 1; v >= 0; v --)
		{
			for (int k = 1; k <= 5; k ++)
			{
				if (dp[cur][v][k] != -1)
				{
					if (T.leaf[v])
						upd(cur, 0, k, dp[cur][v][k]);
					int nv = T.nxt[v][s[pos] - 'a'];
					if (nv != -1)
					{
						upd(nxt, nv, min(5, k + 1), dp[cur][v][k]);
					}
				}
			}
			if (dp[cur][v][5] != -1)
			{
				for (int i = 0; i < 26; i ++)
				{
					int nv = T.nxt[v][i];
					if (nv != -1)
					{
						upd(nxt, nv, 1, dp[cur][v][5] + 1);
					}
				}
			}
		}
		swap(cur, nxt);
	}
	int ans = INF;
	for (int i = 0; i < T.N; i ++)
	{
		for (int j = 1; j <= 5; j ++)
		{
			if (dp[cur][i][j] != -1 && T.leaf[i])
				ans = min(ans, dp[cur][i][j]);
		}
	}
	printf("%d\n", ans);
	return false;
}

int main()
{
	build_dictionary();
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
