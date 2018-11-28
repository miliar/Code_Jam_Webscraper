#include<cstdio>

const int INF = 1e6;
int seen;

void check(long long n)
{
	while(n != 0)
	{
		seen |= (1<<(n%10));
		n /= 10;
	}
}

int main()
{
	int tcc;
	scanf("%d", &tcc);
	for(int i = 1; i <= tcc; i++)
	{
		long long n;
		scanf("%lld", &n);
		if(n == 0)
		{
			printf("Case #%d: INSOMNIA\n", i);
			continue;
		}
		seen = 0;
		long long plus = n;
		while(1)
		{
			check(n);
			if(seen == (1<<10)-1)	break;
			n += plus;
		}

		if(seen == (1<<10)-1)
			printf("Case #%d: %lld\n", i, n);
	}
}
