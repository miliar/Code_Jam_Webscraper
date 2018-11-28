#include <stdio.h>

#define RING(r) (r)*(r)

void main()
{
	FILE *in = fopen("A-small-attempt0 (1).in","r");
	FILE *out = fopen("A-small-attempt0.out","w");

	int T, t, r;
	int n, i, j, cnt, base, rest;

	fscanf(in,"%d",&T);

	for(n=1; n<=T; n++)
	{
		fscanf(in, "%d %d",&r, &t);

		rest = t;
		cnt = 0;
		
		while( rest >= RING(r+1) - RING(r) )
		{
			rest -= (RING(r+1) - RING(r));
			r+=2;
			cnt++;
		}

		fprintf(out, "Case #%d: %d\n",n,cnt);
	}

	fclose(in);
	fclose(out);
}