#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int t;

void solve();

int main()
{
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
}

void solve()
{
	int n;
	cin >> n;
	vector<double> naomi;
	vector<double> ken;
	for (int i = 0; i < n; ++i)
	{
		double p;
		cin >> p;
		naomi.push_back(p);
	}
	for (int i = 0; i < n; ++i)
	{
		double p;
		cin >> p;
		ken.push_back(p);
	}
	sort(naomi.begin(), naomi.end());
	sort(ken.begin(), ken.end());
	int p = 0;
	int ans1 = 0;
	for (int i = 0; i < n; ++i)
	{
		while ((naomi[p] < ken[i]) && (p < n))
		{
			++p;
		}
		if (p == n) break;
		else ++ans1;
		++p;
	}
	int ans2 = 0;
	p = 0;
	for (int i = 0; i < n; ++i)
	{
		while ((ken[p] < naomi[i]) && (p < n))
		{
			++p;	
		}
		if (p == n)
		{
			ans2 += n - i;
			break;
		}
		++p;
	}
	printf("%d %d\n", ans1, ans2);
	return;
}
