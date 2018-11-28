#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	FILE *fout = fopen("out.out", "w");

	int t;
	scanf("%d", &t);

	for (int ca = 1; ca <= t; ca++)
	{
		int ans = 0;
		int a, b, k;
		int m[1000];
		memset(m, 0, sizeof(m));

		scanf("%d %d %d", &a, &b, &k);
		for (int i = 0; i < a; i++)
			for (int j = 0; j < b; j++)
				if ((i & j) < k)
				{
					ans++;
				}

		fprintf(fout, "Case #%d: %d\n", ca, ans);
	}

	fclose(fout);

	return 0;
}