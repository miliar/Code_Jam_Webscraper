#include <bits/stdc++.h>
using namespace std;

int t, n;
int a[5];
int c[3];
int l[15][3][3];
string rs;

void init();

string dp(int n, int u)
{
	if(n == 0)
	{
		if(u == 0) return "P";
		if(u == 1) return "R";
		if(u == 2) return "S";
	}

	int v = (u + 1) % 3;
	string s1 = dp(n - 1, u);
	string s2 = dp(n - 1, v);
	if(s1 <= s2) return s1 + s2;
	else return s2 + s1;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	init();
	cin >> t;
	for(int tt = 1; tt <= t; tt++)
	{
		cout << "Case #" << tt << ": ";
		string rs = "";
		cin >> n >> a[1] >> a[0] >> a[2];
		bool ok = false;
		for(int i = 0; i < 3; i++)
		{
			bool kt = true;
			for(int j = 0; j < 3; j++)
				if(a[j] != l[n][i][j]) kt = false;
			if(kt)
			{
				string s = dp(n, i);
				if(rs == "" || s < rs) rs = s;
				ok = true;
			}
		}
		if(!ok)
			cout << "IMPOSSIBLE\n";
		else cout << rs << "\n";
	}
	return 0;
}

void init()
{
	int tmp[3];
	memset(l, 0, sizeof l);
	for(int type = 0; type < 3; type++)
	{
		memset(c, 0, sizeof c);
		c[type] = 1;
		for(int i = 1; i <= 12; i++)
		{
			for(int u = 0; u < 3; u++)
				tmp[u] = c[u];
			for(int u = 0; u < 3; u++)
				c[u] += tmp[(u + 2)%3];
			for(int u = 0; u < 3; u++)
				l[i][type][u] = c[u];
		}
	}
}