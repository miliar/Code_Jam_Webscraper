#include <cstdio>

int main()
{
	int n_casos, ind = 0;	scanf("%d", &n_casos);
	FILE *arq = fopen("a.out", "w");
	while(n_casos--)
	{
		int smax;
		char buf[1005];
		scanf("%d %s", &smax, buf);

		int inv = 0, acu = buf[0] - '0';
		for(int i = 1; i <= smax; i++)
		{
			inv += i - acu > 0 ? i - acu : 0;
			acu += buf[i] - '0' + (i - acu > 0 ? i - acu : 0);
		}

		fprintf(arq, "Case #%d: %d\n", ++ind, inv);
	}

	return 0;
}
