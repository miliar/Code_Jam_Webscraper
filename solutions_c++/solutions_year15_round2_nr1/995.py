#include <stdio.h>
long long n, t, dp[20], i, j, ans, cnt, a,b, tmp,c,d,cc;
int ccnt(long long n)
{
	int j = 1, re = 1;
	while (n / (j*10))
	{
		j *= 10;
		re++;
	}
	return re;
}

long long rev(long long a)
{
	long long re = 0, i;
	i = 1;
	
	while (a / i)
	{
		re = re * 10 + (a / i) % 10;
		i *= 10;
	}
	return re;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A2.out", "w", stdout);
	scanf("%lld", &t);
	j = 9;
	dp[2] = 10;
	for (i = 2; i <= 15; i++)
	{
		
		if (i % 2) dp[i] = j + j + 1 + dp[i - 1];
		else dp[i] = j + (j / 10) + 1 + dp[i - 1];
		if (i%2)
			j = j * 10 + 9;
	}
	
	for (i = 0; i < t; i++)
	{
		ans = 0;
		scanf("%lld", &n);
		if (n <= 20)
			ans = n;
		else
		{
			cnt = 1;
			j = 1;
			tmp = 0;
			c = 0;
			while (n/(j*10))
			{
				cnt++;
				j *= 10;
			}
			cc = j;

			while (tmp < cnt / 2)
			{
				
				c = c*10 + (n / j) % 10;
				j /= 10;
				tmp++;
			}
			j *= 10;
			d = n % j;

			if (d == 0)
			{
				ans += 1;
				n--;
				j = 1;
				cnt = 1;
				tmp = 0;
				while (n / (j * 10))
				{
					j *= 10;
					cnt++;
				}
				cc = j;
				c = 0;
				while (tmp < cnt / 2)
				{

					c = c * 10 + (n / j) % 10;
					j /= 10;
					tmp++;
				}
				j *= 10;
				d = n % j;


			}

			c = rev(c);

			
			ans += d;
			if (n-d != cc)
			{
				ans += c;
			}
			ans += dp[cnt];

			
		}
		
		printf("Case #%lld: %lld\n", i + 1, ans);
	}
	
}