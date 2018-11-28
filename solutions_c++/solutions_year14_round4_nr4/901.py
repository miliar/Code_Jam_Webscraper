#include <stdio.h>
#include <string.h>
#include <math.h>
#include <cstdio>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <algorithm>
#include <time.h>
using namespace std;

int m, n, mx, wy;
vector <string> vs;
int g[10];

vector <vector <string> > vss;

int calc (int ind)
{
	if (vss[ind].size() == 0)
		return 0;

	int ret = 0;

	int h = 0;
	int nxt[100][100];

	memset (nxt, -1, sizeof(nxt));

	for (int i=0;i<vss[ind].size();i++)
	{
		string s = vss[ind][i];
		int cur = 0;
		for (int j=0;j<s.size();j++)
		{
			if (nxt[cur][s[j]-'A'] == -1)
			{
				h++;
				nxt[cur][s[j]-'A'] = h;
			}
			cur = nxt[cur][s[j]-'A'];
		}
	}
	return h+1;
}

void test ()
{
	vss.clear();
	vss.resize(n);

	for (int i=0;i<m;i++)
		vss[g[i]].push_back(vs[i]);

	int ret = 0;
	for (int i=0;i<n;i++)
		ret += calc (i);
	if (ret > mx)
	{
		mx = ret;
		wy = 1;
	}
	else if (ret == mx)
		wy++;
}

void sol (int ind)
{
	if (ind == m)
	{
		test();
		return;
	}

	for (int i=0;i<n;i++)
	{
		g[ind] = i;
		sol (ind+1);
	}
	return ;
}

int main ()
{
	freopen ("C-small.in", "r", stdin);
	freopen ("C-small.out", "w", stdout);

	int t;

	scanf ("%d", &t);
	
	for (int tc = 1; tc <= t; tc++)
	{
		vs.clear();

		cin >> m >> n;
		for (int i=0;i<m;i++)
		{
			string s;
			cin >> s;
			vs.push_back(s);
		}

		mx = 0;
		wy = 0;

		sol (0);

		printf ("Case #%d: %d %d\n", tc, mx, wy);

	}

	return 0;
}



