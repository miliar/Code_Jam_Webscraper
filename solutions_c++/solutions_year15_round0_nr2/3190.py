#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

bool check(int ti, std::vector<int>& p)
{
	int extra;
	for (int i = 1; i <= ti; i++)
	{
		extra = 0;
		for (int j = 0; j < p.size(); j++)
		{
			if (p[j] <= i) continue;
			if (p[j] % i == 0)
				extra += (p[j] - i) / i;
			else 
				extra += (p[j] - i) / i + 1;
		}
		if (extra + i <= ti) return true;
	}
	return false;
}

int solve()
{
	int d;
	std::vector<int> p;
	int pmax = 0;
	scanf("%d", &d);
	for (int i = 0; i < d; i++)
	{
		int temp;
		scanf("%d", &temp);
		p.push_back(temp);
		if (temp > pmax) pmax = temp;
	}
	int l = 0;
	int r = pmax + 1;
	while (l < r)
	{
		int mid = (l + r) / 2;
		if (check(mid, p)) 
			r = mid;
		else 
			l = mid + 1;
	}
	return l;
}

int main()
{
	//freopen("B-large.in", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		printf("Case #%d: %d\n", i + 1, solve());
	}
}