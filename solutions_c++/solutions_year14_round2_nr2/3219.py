// Libraries that I'm using and are available in the internet (they are standard ones)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int cases(int a, int b, int k)
{
	int res = 0;

	for(int i = 0; i < a; i++)
	{
		for(int j = 0; j < b; ++j)
		{
			int c = i & j;

			if(c >= k) continue;

			res++;
		}
	}

	return res;
}

int main(void)
{
	int t;
	size_t v[100];
	FILE* arq, *saida;

	arq = fopen("B-small-attempt0.in","rt");
	saida = fopen("B-small-attempt0.out","wt");
	if(!arq || !saida)
	{
		printf("Problem happened");
		exit(-1);
	}
	
	fscanf(arq, "%d", &t);

	for(int j = 0; j < t; ++j)
	{
		size_t a, b, k;

		fscanf(arq,"%d %d %d", &a, &b, &k);

		v[j] = cases(a, b, k);
	}
	fclose(arq);

	for(int i = 0; i < t; ++i) fprintf(saida,"Case #%d: %d\n", i+1, v[i]);
	fclose(saida);

	return 0;
}