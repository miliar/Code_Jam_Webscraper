#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <sstream>
#include <fstream>
#include <functional>
#include <cassert>
#include <complex>
#include <valarray>
using namespace std;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif

typedef long long ll;
typedef pair<int, int> pii;
#define X first
#define Y second
#define mp make_pair

typedef long double ld;

const int N = 110;
char str[N];
vector <int> g[N];
string words[N];
int n, m;

void read()
{
	scanf("%d", &n);
	for (int i = 0; i <= n; i++)
		g[i].clear();
	for (int i = 1; i <= n; i++)
	{
		int p;
		scanf("%d", &p);
		g[p].push_back(i);
	}
	str[0] = '?';
	scanf(" %s", str + 1);
	scanf("%d", &m);
	for (int i = 0; i < m; i++)
		cin >> words[i];
}

ld dp[N];
ld C[N][N];
int sz[N];

ld getC(int a, int k)
{
	if (k > a || k < 0)
		return 0;
	return C[a][k];
}

void init()
{
	for (int i = 0; i < N; i++)
		for (int s = 0; s <= i; s++)
		{
			if (i == s || s == 0)
				C[i][s] = 1;
			else
				C[i][s] = C[i - 1][s] + C[i - 1][s - 1];
		}
}

void dfs(int v)
{
	dp[v] = 1;
	sz[v] = 0;
	int sum = 0;
	for (int to : g[v])
	{
		dfs(to);
		sum += sz[to];
		dp[v] *= dp[to] * getC(sum, sz[to]);
	}
	sz[v] = sum + 1;
//	eprintf("%d: %d %Lf\n", v, sz[v], dp[v]);
}

void solveTree()
{
	dfs(0);
}

set <int> cands;
int sumPref[N];
int sumSuff[N];
ld dpPref[N];
ld dpSuff[N];

ld getValue(int v)
{
	int sum = 0;
	ld value = 1;
	for (int to : g[v])
	{
		sum += sz[to];
		value *= dp[to] * getC(sum, sz[to]);
	}
	for (int to : cands)
	{
		if (to == v)
			continue;
		sum += sz[to];
		value *= dp[to] * getC(sum, sz[to]);
	}
	return value;
}

string seq;
int candsRow[N];

void chooseNext(ld &p)
{
	int it = 0;
	for (int v : cands)
		candsRow[it++] = v;

	for (int i = 0; i < it; i++)
	{
		sumPref[i] = (i == 0 ? 0 : sumPref[i - 1]) + sz[candsRow[i]];
		dpPref[i] = (i == 0 ? 1 : dpPref[i - 1]) * dp[candsRow[i]] * getC(sumPref[i], sz[candsRow[i]]);
	}
	dpSuff[it] = 1;
	sumSuff[it] = 0;
	for (int i = it - 1; i >= 0; i--)
	{
		sumSuff[i] = (i == it - 1 ? 0 : sumSuff[i + 1]) + sz[candsRow[i]];
		dpSuff[i] = (i == it - 1 ? 1 : dpSuff[i + 1]) * dp[candsRow[i]] * getC(sumSuff[i], sz[candsRow[i]]);
	}

	it = 0;
	for (int v : cands)
	{
		ld value = (it == 0 ? 1 : dpPref[it - 1]);
		int curSum = (it == 0 ? 0 : sumPref[it - 1]);
		for (int to : g[v])
		{
			curSum += sz[to];
			value *= dp[to] * getC(curSum, sz[to]);
		}
		value *= dpSuff[it + 1] * getC(curSum + sumSuff[it + 1], sumSuff[it + 1]);
		if (value <= p)
			p -= value;
		else
		{
			seq.push_back(str[v]);
			cands.erase(v);
			for (int to : g[v])
				cands.insert(to);
			break;
		}
		it++;
	}
}

int cntGood[N];
int cntAll[N];

bool contain(const string &a, const string &b)
{
	for (int i = 0; i <= (int)a.length() - (int)b.length(); i++)
	{
		if (a.substr(i, (int)b.length()) == b)
			return true;
	}
	return false;
}

void genFixed(ld p)
{
	cands.clear();
	for (int to : g[0])
		cands.insert(to);

	seq.clear();
	for (int i = 0; i < n; i++)
		chooseNext(p);
	for (int i = 0; i < m; i++)
	{
		if (contain(seq, words[i]))
			cntGood[i]++;
		cntAll[i]++;
	}
}

void genRandom()
{
	ld p = rand() * 1. / RAND_MAX * dp[0];
	genFixed(p);
}

void solve()
{
	memset(cntGood, 0, sizeof(cntGood));
	memset(cntAll, 0, sizeof(cntAll));
	solveTree();
	if (dp[0] < 1000)
	{
		for (int i = 0; i < dp[0]; i++)
			genFixed(i);
	}
	else
	{
		int IT = 10000;
		for (int i = 0; i < IT; i++)
			genRandom();
	}
	for (int i = 0; i < m; i++)
		printf("%.4lf ", cntGood[i] * 1. / cntAll[i]);
	puts("");
}

int main()
{
	init();

	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		eprintf("Test %d\n", i + 1);
		printf("Case #%d: ", i + 1);
		read();
		solve();
	}
	return 0;
}
