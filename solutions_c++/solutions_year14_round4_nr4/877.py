#pragma comment(linker, "/STACK:255000000")
#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <functional>
#include <stack>
#include <memory.h>
#include <algorithm>
#include <math.h>
#include <valarray>
#include <complex>
#include <bitset>
#include <ctime>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> vint;
typedef vector<vint> vvint;
typedef complex<double> comp;
typedef pair<int, int> pint;

long double eps = 1e-7;
const int BASE = (int) 1e9;
const long double PI = 3.1415926535897932384626433832795;
const int MOD = (int) 1e9 + 7;
const int HMOD = (1 << 18) - 1;
const int INF = 1 << 30;
const LL LLINF = 1ll << 60;
const int N = 310000;

int t, n, m;
string s[10];
int a[10];
map<int, int> M;
vector<int> v[4];

map<int, int> trie[1100];
int sz = 1;

void Add(int cur)
{
	int v = 0;
	for (int i = 0; i < s[cur].length(); i++)
	{
		int c = s[cur][i];
		if (trie[v].find(c) == trie[v].end()) 
		{
			trie[v][c] = sz;
			v = sz++;
		}
		else
			v = trie[v][c];
	}
}

int Calc()
{
	int res = 0;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < v[i].size(); j++)
			Add(v[i][j]);
		res += sz;
		for (int i = 0; i < sz; i++)
			trie[i].clear();
		sz = 1;
	}
	return res;
}

void Go(int cur)
{
	if (cur == m)
	{
		for (int i = 0; i < 4; i++)
			v[i].clear();
		for (int i = 0; i < m; i++)
			v[a[i]].push_back(i);
		for (int i = 0; i < n; i++)
			if (v[i].empty())
				return;
		int res = Calc();
		M[res] = M[res] + 1;
	}
	else
	{
		for (int i = 0; i < n; i++)
		{
			a[cur] = i;
			Go(cur + 1);
		}
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for (int k = 0; k < t; k++)
	{
		scanf("%d%d", &m, &n);
		for (int i = 0; i < m; i++)
			cin >> s[i];
		M.clear();
		Go(0);
		printf("Case #%d: %d %d\n", k + 1, (--M.end())->first, (--M.end())->second); 
	}
	return 0;
}