#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
bool yorn(bool chk[])
{
	for (int i = 0; i < 10; i++)
	{
		if (!chk[i])
		{
			return false;
		}
	}
	return true;
}
int main()
{
	freopen("large.in", "r", stdin);
	FILE *f;
	f = fopen("out.txt", "w");
	int cas, k = 1;
	scanf("%d", &cas);
	while (cas--)
	{
		long long num;
		bool chk[10];
		for (int i = 0; i < 10; i++)
		{
			chk[i] = false;
		}
		scanf("%lld", &num);
		for (long long i = 1; i<100000000; i++)
		{
			char str[200] = { 0, };
			_itoa(i*num, str, 10);
			for (int j = 0; j < strlen(str); j++)
			{
				if (!chk[str[j] - '0'])
				{
					chk[str[j] - '0'] = true;
				}
			}
			if (yorn(chk))
			{
				fprintf(f, "Case #%d: %lld\n", k, i*num);
				break;
			}
		}
		if (!yorn(chk))
		{
			fprintf(f, "Case #%d: INSOMNIA\n", k);
		}
		k++;
	}
}
