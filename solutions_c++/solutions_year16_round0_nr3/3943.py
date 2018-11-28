#include<stdio.h>

int main()
{
	long long t, i;
	long long n, j;
	long long k, l, m, min, max, value[11], base[11], root, count;
	freopen("inputC.txt", "r", stdin);
	freopen("outputC.txt", "w", stdout);
	scanf("%lld", &t);
	for (i = 0; i < t; i++)
	{
		scanf("%lld %lld", &n, &j);
		printf("case #%lld:\n", i + 1);

		min = 1;
		for (k = 1; k < n; k++)
			min *= 2;
		min += 1;
		max = min * 2 - 2;
		for (k = min; k < max; k+=2) //이진수 범위
		{
			count = 0;
			for (l = 0; l < 11; l++)
			{
				value[l] = 0;
				base[l] = 0;
			}

			root = 1;
			for (l = 1; l <= n; l++)//진법별 값 구하기
			{
				for (m = 2; m < 11; m++)
				{
					value[m] *= m;
					value[m] += ((k >> (n - l)) % 2);
				}
				if (l < n / 2+1)
					root *= 10;
			}

			for (l = 2; l < root; l++)
			{
				for (m = 2; m < 11; m++)
					if (value[m] % l == 0 && base[m]==0 && value[m]>l)
					{
						base[m] = l;
						count++;
					}
				if (count == 9)
					break;
			}

			if (count == 9)
			{
				for (l = 1; l <= n; l++)//진법별 값 구하기
				{
					printf("%d",((k >> (n - l)) % 2));
				}
				printf(" ");

				for (l = 2; l < 11; l++)
				{
					printf("%lld ", base[l]);
				}
				j--;
				printf("\n");
			}

			if (j == 0)
				break;
		}
	}
	return 0;
}