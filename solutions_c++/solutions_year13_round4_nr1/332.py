#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
using namespace std;

const long long mod = 1000002013;

vector < pair < int , int > > v;
pair < int , int > e[2005];
int p[1005][2], am[1005];
int n, m;

long long getCost (int l, int r, int kol)
{
	long long cur = n * 1LL * (r - l);
	cur %= mod;
		
	cur -= ( (r - l) * 1LL * (r - l - 1) ) / 2;
	cur %= mod;
	cur += mod;
	cur %= mod;

	cur = cur * 1LL * kol;
	cur %= mod;

	return cur;
}

long long calcStupid ()
{
	long long res = 0;

	for (int i = 0; i < m; i++)
	{
		res += getCost(p[i][0], p[i][1], am[i] );
		res %= mod;
	}

	return res;
}

bool cmp (pair < int , int > d1, pair < int , int > d2)
{
	if (p[d1.first][d1.second] != p[d2.first][d2.second] )
		return p[d1.first][d1.second] < p[d2.first][d2.second];
	if (d1.second != d2.second)
		return d1.second < d2.second;
	return d1.first < d2.first;
}

long long getAns ()
{
	for (int i = 0; i < m; i++)
	{
		e[i * 2] = make_pair(i, 0);
		e[i * 2 + 1] = make_pair(i, 1);
	}
	sort(e, e + 2 * m, cmp);

	long long res = 0;

	int to = m * 2;
	int lastPos = -1;
	for (int i = 0; i < to; i++)
	{
		if (lastPos == -1)
		{
			if (e[i].second != 0)
				throw 42;

			lastPos = p[e[i].first][1];

			v.push_back(make_pair(p[e[i].first][0], am[e[i].first] ) );

			continue;
		}

		if (p[e[i].first][e[i].second] > lastPos)
		{
			lastPos = -1;
			i--;
			continue;
		}

		if (e[i].second == 0)
		{
			v.push_back(make_pair(p[e[i].first][0], am[e[i].first] ) );

			lastPos = max(lastPos, p[e[i].first][1] );
		}else
		{
			int rem = am[e[i].first];

			while (rem != 0)
			{
				if (v.back().second >= rem)
				{
					res += getCost(v.back().first, p[e[i].first][1], rem);
					res %= mod;

					v.back().second -= rem;
					if (v.back().second == 0)
						v.pop_back();

					rem = 0;
				}else
				{
					res += getCost(v.back().first, p[e[i].first][1], v.back().second);
					res %= mod;
					rem -= v.back().second;

					v.pop_back();
				}
			}
		}
	}

	return res;
}

void solve ()
{
	long long ansStupid = calcStupid();
	long long ansBest = getAns();

	long long res = (ansStupid - ansBest) % mod;
	res += mod;
	res %= mod;

	printf("%lld", res);
}

int main ()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int test, t;

	scanf("%d\n", &test);
	for (t = 0; t < test; t++)
	{
		if (t)
			printf("\n");

		printf("Case #%d: ", t + 1);

		// input

		scanf("%d%d", &n, &m);
		for (int i = 0; i < m; i++)
		{
			scanf("%d%d%d", &p[i][0], &p[i][1], &am[i] );
		}

		// #input

		solve();
	}

	return 0;
}