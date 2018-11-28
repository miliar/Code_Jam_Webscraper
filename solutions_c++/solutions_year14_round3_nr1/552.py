#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <fstream>
using namespace std;
long long gcd(long long a, long long b)
{
	if (b == 0)
		return a;
	return gcd(b, a % b);
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	long long t, i, p, q, g;
	scanf("%lld", &t);
	for (i = 1; i <= t; i++)
	{
		scanf("%lld/%lld", &p, &q);
		if (p > q)
			printf("Case #%lld: impossible\n", i);
		else
		{
			g = gcd(p, q);
			p /= g;
			q /= g;
			long long temp = q;
			while (q != 1)
			{
				if (q % 2 != 0)
				{
					printf("Case #%lld: impossible\n", i);
					break;
				}
				q /= 2;
			}
			if (q == 1)
			{
				long long c = 0;
				while (p < temp)
				{
					p *= 2;
					c++;
				}
				printf("Case #%lld: %lld\n", i, c);
			}
		}
	}
	return 0;
}