#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int n, m;

void print(int x)
{
	for (int i = n-1; i >= 0; --i)
		if ((1 << i) & x)
			printf("1");
		else
			printf("0");
}

long long trans(int x, int base)
{
	long long a = 1;
	long long res = 0;
	for (int i = 0; i < n; ++i)
	{
		if ((1 << i) & x)
			res += a;
		a *= base;
	}
	return res;
}
bool check(int x, vector<long long>& divs)
{
	for (int base = 2; base <= 10; ++base)
	{
		long long num = trans(x, base);
		long long top = sqrt(num);
		int flag = 0;
		for (long long i = 2; i <= top; ++i)
			if (num % i == 0)
			{
				divs.push_back(i);
				flag = 1;
				break;
			}
			// else
			// 	printf("not %d %d\n", num, i);
		if (flag == 0)
		{
			// printf("x%d base%d num%d\n", x, base, num);
			return false;
		}
	}
	return true;
}

int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("dataCCC.out","w",stdout);
	int T, ys = 0;
	scanf("%d", &T);
	while (T--)
	{
		printf("Case #%d:\n", ++ys);
		scanf("%d%d", &n, &m);

		int high = (1 << (n - 1));
		for (int i = 0; i < (1 << (n - 2)); ++i)
		{
			int x = (i << 1) + high + 1;
			vector<long long> divs;
			if (check(x, divs))
			{
				print(x);
				// printf(" x=%d ", x);
				for (int i = 0; i < divs.size(); ++i)
					printf(" %lld", divs[i]);
				printf("\n");
				if (--m == 0) break;
			}
		}
	}

	return 0;
}