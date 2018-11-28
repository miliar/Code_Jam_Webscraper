#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <utility>
#include <algorithm>
#include <memory.h>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>

using namespace std;

#pragma comment (linker, "/STACK:64000000")

#define pb push_back
#define pii pair<int, int>
#define pdi pair<double, int>
#define pdii pair<pdi, int>
#define pll pair<ll, ll>
#define pib pair<int, bool>
#define pli pair<ll, int>
#define pil pair<int, ll>
#define vi vector<int>
#define inf 2000000000
#define mod 1000000007
#define mod2 536870911
#define y1 uhgeg
#define eps 1e-9
#define prime 3001
#define N 200005
#define clean(mas) memset(mas, 0, sizeof(mas))

typedef long long ll;
typedef unsigned long long ull;


int n, m, j, i, l, h, k, t, q1, q2, q, e[1000000], f[1000000], ans;
string s, ss;
map<string, int> mp;
vector<int> v[100];

void rec(int step)
{
	if (step > n)
	{
		int res = 0;
		for (int j = 1; j <= l; j++)
		{
			if (f[j] && e[j])
			{
				res++;
			}
		}
		ans = min(res, ans);
	}
	else
	{
		for (int j = 0; j < v[step].size(); j++)
		{
			e[v[step][j]]++;
		}
		rec(step + 1);
		for (int j = 0; j < v[step].size(); j++)
		{
			e[v[step][j]]--;
			f[v[step][j]]++;
		}
		rec(step + 1);
		for (int j = 0; j < v[step].size(); j++)
		{
			f[v[step][j]]--;
		}
	}
}

void solve()
{
	cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		cin >> n;
		if (tt > 1)
		{
			clean(e);
			clean(f);
			mp.clear();
			l = 0;
			for (j = 1; j <= n; j++)
			{
				v[j].clear();
			}
		}
		getline(cin, s);
		for (j = 1; j <= n; j++)
		{
			getline(cin, s);
			for (i = 0; i < s.size(); )
			{
				q1 = q2 = i;
				while (q2 + 1 < s.size() && s[q2 + 1] != ' ')
				{
					q2++;
				}
				ss = s.substr(q1, q2 - q1 + 1);
				if (!mp.count(ss))
				{
					q = mp[ss] = ++l;
				}
				else
				{
					q = mp[ss];
				}
				v[j].pb(q);
				if (j == 1)
				{
					e[q]++;
				}
				if (j == 2)
				{
					f[q]++;
				}
				i = q2 + 2;
			}
		}
		ans = l;
		rec(3);
		printf ("Case #%d: %d\n", tt, ans);
	}
}

int main()
{
	ios_base::sync_with_stdio(false);cin.tie(0);
	freopen("C-small-attempt0.in", "rt", stdin); freopen("output.txt", "wt", stdout);
	srand(3333);
	solve();
	return 0;
}