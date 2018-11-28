#include<iostream>
#include<cstdio>
#include<string>
#include<set>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<queue>
using namespace std;
#pragma comment(linker, "/STACK:256777216")

#define LL long long

const int mod = 1000002013;
int n, m, ans;
int s[1000], f[1000], p[1000];
set<int> Xt;
map<int, int> X;
LL train[5000], realX[5000];

LL dist(LL s, LL f, LL pas)
{
	s--;
	pas %= mod;
	LL l = f - s;
	l = (n * l - (l * (l - 1) / 2)) % mod;
	return (l * pas) % mod;
}

void calc(int l, int r)
{
	for (int i = l; i <= r; i++)
	{
		LL m = 1e18;
		for (int j = l; j <= r; j++)
			if (train[j] == 0)
			{
				if (j > l)
					calc(l, j - 1);
				if (j < r)
					calc(j + 1, r);
				return;
			}
			else
				m = min(m, train[j]);

		ans = (ans - dist(realX[l], realX[r], m)) % mod;

		for (int j = l; j <= r; j++)
			train[j] -= m;
	}
}

int main()
{
	#ifndef ONLINE_JUDGE
		freopen("input.txt", "rt", stdin);
		freopen("output.txt", "wt", stdout);
	#endif

	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		int T = 0;
		ans = 0;
		Xt.clear(); X.clear();
		for (int i = 0; i < 5000; i++)
			train[i] = 0;

		cin >> n >> m;
		for (int i = 0; i < m; i++)
		{
			cin >> s[i] >> f[i] >> p[i];
			s[i]++;
			ans = (ans + dist(s[i], f[i], p[i])) % mod;
			Xt.insert(s[i]);
			Xt.insert(f[i]);
			Xt.insert(f[i] + 1);
		}

		for (auto i = Xt.begin(); i != Xt.end(); i++)
		{
			X[*i] = T;
			realX[T] = *i; 
			T++;
		}

		for (int i = 0; i < m; i++)
		{
			int s1 = X[s[i]], f1 = X[f[i]];
			for (int j = s1; j <= f1; j++)
				train[j] = train[j] + p[i];
		}

		calc(0, T - 1); 

		cout << "Case #" << t + 1 << ": ";
		cout << (ans + mod) % mod;
		cout << endl;
	}
}
































