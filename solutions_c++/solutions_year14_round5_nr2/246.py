#include <bits/stdc++.h>
using namespace std;

int n, dianaDamage, towerDamage, h[1010], g[1010];
map < vector <int>, int > f[2];

int dp(int turn, vector <int> h)
{
	if (f[turn].count(h)) return f[turn][h];
	
	if (!turn)
	{
		int res = dp(1, h);
		for (int i = 0; i < n; i++)
			if (h[i] > 0)
			{
				h[i] -= dianaDamage;
				res = max(res, dp(1, h) + (h[i] < 1 ? g[i] : 0));
				h[i] += dianaDamage;				
			}
		return f[turn][h] = res;
	}

	vector <int> hh = h;
	int found = 0;
	for (int i = 0; i < n; i++)
		if (h[i] > 0)
		{
			h[i] -= towerDamage;
			found = 1;
			break;
		}
		
	if (!found) return f[turn][hh] = 0;
	return f[turn][hh] = dp(0, h);
}

int main()
{
	freopen("b.in", "r", stdin); 
	freopen("b.out", "w", stdout);
	int test;
	cin >> test;
	for (int noTest = 1; noTest <= test; noTest++)
	{
		cin >> dianaDamage >> towerDamage >> n;
		vector <int> h(n);
		for (int i = 0; i < n; i++) cin >> h[i] >> g[i];
		f[0].clear();
		f[1].clear();
		printf("Case #%d: %d\n", noTest, dp(0, h));
	}
}
