#pragma warning(disable : 4996)
#include <stdio.h>
#include <iostream>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

long long convert(long long mask, long long base)
{
	long long res = 0;
	long long m = 1;
	while (mask > 0)
	{
		res += m * (mask % 2);
		mask /= 2;
		m *= base;
	}
	return res;
}

long long divisor(long long a)
{
	for (long long i = 2; i * i <= a; i++)
		if (a % i == 0)
			return i;
	return -1;
}

void process(int t)
{
	printf("Case #%d:\n", t + 1);
	int N, J;
	scanf("%d%d", &N, &J);
	long long NN = (1LL << min(N - 2, 19));
	for (long long i = 0; i < NN; i++)
	{
		long long mask = 1LL + (1LL << (N - 1)) + i * 2;
		bool ok = true;
		vector<long long> v;
		for (int j = 2; j <= 10; j++)
		{
			long long a = convert(mask, j);
			a = divisor(a);
			if (a == -1)
			{
				ok = false;
				break;
			}
			else
				v.push_back(a);
		}
		if (ok)
		{
			J--;
			long long a = convert(mask, 10);
			printf("%lld", a);
			for (int j = 2; j <= 10; j++)
			{
				printf(" %lld", v[j - 2]);
			}
			printf("\n");
		}
		if (J == 0)
			break;
	}
	
}

int main()
{
	freopen("d:\\acm\\CodeJam\\2016\\CodeJamQual\\C\\C.in", "r", stdin);
	freopen("d:\\acm\\CodeJam\\2016\\CodeJamQual\\C\\C.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		process(t);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}