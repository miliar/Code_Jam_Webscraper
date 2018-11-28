#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

bool val(long long a)
{
	vector <int> b;
	while (a)
	{
		b.push_back(a % 10);
		a /= 10;
	}
	bool res = true;
	if (b.size() & 1)
	{
		int m = b.size() / 2;
		for (int i = 0; i < m; i++)
		{
			if (b[i] != b[b.size() - i - 1])
			{
				res = false;
				break;
			}
		}
	}
	else
	{
		for (int i = 0; i < (b.size() - i - 1); i++)
		{
			if (b[i] != b[b.size() - i - 1])
			{
				res = false;
				break;
			}
		}
	}

	return res;
}

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	long long N = 100000000000000;
	long long enn = sqrt((double)N) + 1;
	long long mass[100] = {0};
	int sz = 0;
	for (long long i = 1; i <= enn; i++)
	{
		if (!val(i))
			continue;
		long long a = i * i;
		if (!val(a))
			continue;
		if ((a) <= N)
		{
			mass[sz] = a;
			sz++;
			//printf("%lld\n", a);
		}
	}


	int t;
	scanf("%d ", &t);

	for (int k = 0; k < t; k++)
	{
		long long a,b;
		scanf("%lld %lld ", &a, &b);
		int res = 0;
		for (int i = 0; i < sz; i++)
		{
			if ((mass[i] >= a) && (mass[i] <= b))
				res++;
			if (mass[i] > b)
				break;
		}
		printf("Case #%d: %d\n", k + 1, res);
	}
	return 0;
}