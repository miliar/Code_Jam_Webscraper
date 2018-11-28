#include <stdio.h>
#include <math.h>

int digits[20];
int cnt = 0;

bool pal(long long n)
{
	cnt = 0;
	while (n > 0)
	{
		digits[cnt++] = n % 10;
		n/=10;
	}
	for (int i = 0; i < cnt / 2; i++)
	{
		if (digits[i] != digits[cnt - i - 1])
		{
			return false;
		}
	}
	return true;
}

long long f(long long n)
{
	long long res = 0;
	long long bord = sqrt(n * 1.0) + 3;
	for (long long i = 1; i <= bord; i++)
	{
		if (pal(i))
		{
			if (i * i <= n && pal(i*i))
			{
				res++;
			}
		}
	}
	return res;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for (int i = 1 ; i <= t; i++)
	{
		long long a,b;
		scanf("%lld%lld",&a,&b);
		printf("Case #%d: %lld\n",i, f(b) - f(a - 1));
	}
	return 0;
}