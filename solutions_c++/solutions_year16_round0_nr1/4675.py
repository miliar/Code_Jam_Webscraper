#include<stdio.h>
int main()
{
	long long t, i;
	long long n, k, j, m[10], ten;
	freopen("inputA.txt", "r",stdin);
	freopen("outputA.txt", "w",stdout);
	scanf("%lld", &t);
	for (i = 0; i < t; i++)
	{
		scanf("%lld", &n);
		ten = 0;
		for (j = 0;j<10; j++)
			m[j] = 0;
		if (n == 0)
		{
			printf("case #%lld: INSOMNIA\n", i + 1);
			continue;
		}
		for (j = 1;; j++)
		{
			k = n*j;
			while (k)
			{
				if (m[k % 10] == 0)
				{
					m[k % 10] = 1;
					ten++;
				}
				k /= 10;
			}
			if (ten == 10)
				break;
		}
		printf("case #%lld: %lld\n", i + 1, j*n);
	}
	return 0;
}