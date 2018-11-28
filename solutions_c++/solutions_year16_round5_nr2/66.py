#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;

typedef pair<int, int> pii;
#define mp make_pair

const int IT = (int)4e4;
const int N = 111;
int n, m;
char a[N];
int p[N];
char s[10][N];
vector<int> g[N];
int par[N];
bool open[N];
int ans[N];
char w[N];

void getRandomWord()
{
	for (int i = 0; i < n; i++)
		p[i] = i;
	for (int i = 0; i < n; i++)
	{
		open[i] = par[i] == -1;
	}
	int sz = 0;
	while(sz < n)
	{
		int x = rand() % (n - sz);
		int v = p[x];
		while(!open[v])
			v = par[v];
		x = 0;
		while(p[x] != v) x++;
		swap(p[x], p[n - sz - 1]);
		w[sz++] = a[v];
		for (int y : g[v])
			open[y] = true;
	}
	w[n] = (char)0;
	return;
}

char q[2 * N];
int z[2 * N];

bool contain(char* s, char* p)
{
	int p_len = strlen(p);
	for (int i = 0; i < p_len; i++)
		q[i] = p[i];
	q[p_len] = '#';
	int len = strlen(s);
	for (int i = 0; i < len; i++)
		q[p_len + 1 + i] = s[i];
	len += p_len + 1;
	for (int i = 0; i < len; i++)
		z[i] = 0;
	int l = 0, r = 0;
	for (int i = 1; i < len; i++)
	{
		if (i < r)
			z[i] = min(z[i - l], r - i);
		while(i + z[i] < len && q[z[i]] == q[i + z[i]]) z[i]++;
		if (i + z[i] > r)
		{
			l = i;
			r = i + z[i];
		}
	}
	for (int i = p_len + 1; i < len; i++)
		if (z[i] == p_len)
			return true;
	return false;
}

void solve()
{
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		g[i].clear();
	for (int i = 0; i < n; i++)
	{
		int x;
		scanf("%d", &x);
		par[i] = x - 1;
		if (x == 0) continue;
		g[x - 1].push_back(i);
	}
	scanf(" %s ", a);
	scanf("%d", &m);
	for (int i = 0; i < m; i++)
		scanf(" %s ", s[i]);
	for (int i = 0; i < m; i++)
		ans[i] = 0;
	for (int it = 0; it < IT; it++)
	{
		getRandomWord();
		for (int i = 0; i < m; i++)
			if (contain(w, s[i]))
				ans[i]++;
	}
	for (int i = 0; i < m; i++)
		printf(" %.7lf", (double)ans[i] / IT);
	printf("\n");
	return;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		cerr << i << endl;
		printf("Case #%d:", i);
		solve();
	}

	return 0;
}