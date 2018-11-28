#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <utility>
#include <set>
#include <cassert>
using namespace std;

const int MaxN = 60;
const int MaxL = 10000;
const int INF = 1000000000;

typedef long long s64;

s64 calc(vector<pair<s64, s64> > &a)
{
	s64 v = a[0].second == 1 ? a[1].first : a[0].first;
	if (v == 0)
	{
		for (int i = 0; i < (int)a.size(); i++)
			a[i].second /= 2;
	}
	else
	{
		for (int i = 0, j = 0; i < (int)a.size(); i++)
			if (a[i].second)
			{
				while (a[j].first < a[i].first + v)
				{
					assert(j < (int)a.size());
					j++;
				}
				a[j].second -= a[i].second;
			}
	}
	int t_n = 0;
	for (int i = 0; i < (int)a.size(); i++)
		if (a[i].second)
			a[t_n++] = a[i];
	a.resize(t_n);
	return v;
}

int main()
{
	int nT;
	cin >> nT;

	for (int nt = 1; nt <= nT; nt++)
	{
		vector<pair<s64, s64> > a;

		int a_n;
		scanf("%d", &a_n);
		a.resize(a_n);
		for (int i = 0; i < a_n; i++)
			scanf("%lld", &a[i].first);
		for (int i = 0; i < a_n; i++)
			scanf("%lld", &a[i].second);

		sort(a.begin(), a.end());

		s64 neg = a[0].first;
		for (int i = 0; i < a_n; i++)
			a[i].first -= neg;

		vector<s64> s;
		while (a.size() > 1 || a[0].second > 1)
			s.push_back(calc(a));

		int n = (int)s.size();
		sort(s.begin(), s.end());
		static set<s64> f[MaxN + 1];
		for (int i = 0; i <= n; i++)
			f[i].clear();
		f[0].insert(0);
		for (int i = 0; i < n; i++)
			for (set<s64>::iterator it = f[i].begin(); it != f[i].end(); it++)
				f[i + 1].insert(*it + s[i]), f[i + 1].insert(*it);

		s64 sum = -neg;
		for (int i = n - 1; i >= 0; i--)
			if (f[i].count(sum - s[i]))
				sum -= s[i], s[i] = -s[i];
		sort(s.begin(), s.end());

		assert(sum == 0);

		printf("Case #%d:", nt);
		for (int i = 0; i < (int)s.size(); i++)
			printf(" %lld", s[i]);
		printf("\n");
	}

	return 0;
}
