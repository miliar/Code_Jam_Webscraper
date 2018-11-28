#include <bits/stdc++.h>
using namespace std;
long long triv(long long x)
{
	for(long long i = 2; i*i<= x; i++)
	{
		if(x%i == 0)
		{
			return i;
		}
	}
	return -1ll;
}
long long xp(int b, int i)
{
	if(i == 0) return 1ll;
	if(i == 1) return (long long) b;
	long long x = xp(b, i/2);
	x *= x;
	if(i&1)
	{
		x *= (long long) b;
	}
	return x;
}
int main()
{
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int n, k;
	scanf("%*d %d %d", &n, &k);
	printf("Case #1:\n");
	for(long long i = (1<<(n-1)); i< (1<<n) && k; i++)
	{
		if(!(i&1)) continue;
		bool ok = 1;
		long long d[15];
		long long num;
		for(int b = 2; b<= 10; b++)
		{
			num = 0;
			for(int j= 0; j< n; j++)
			{
				if(i & (1<<j) )
				{
					num += xp(b, j);
				}
			}
			//printf("Base %d: %lld\n", b, num);
			long long t = triv(num);
			if(t == -1)
			{
				ok = 0;
				break;
			}
			d[b] = t;
		}
		if(ok)
		{
			for(int j = n-1; j>= 0; j--)
			{
				printf("%d", (bool)((i&(1<<j))));
			}
			printf(" ");
			for(int j = 2; j<= 10; j++)
			{
				printf("%lld ", d[j]);
			}
			printf("\n");
			k--;
			//system("pause");
		}
	}
}