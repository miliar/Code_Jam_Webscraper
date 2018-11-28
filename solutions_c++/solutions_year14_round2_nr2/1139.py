#include<stdio.h>

int main(void)
{
	int T;
	FILE *in = fopen("B-small-attempt0.in","r");
	FILE *out = fopen("output.txt","w");

	fscanf(in,"%d",&T);

	for(int t = 1; t <= T; t++)
	{
		int A,B,K;
		fscanf(in,"%d %d %d",&A, &B, &K);
		int cnt = 0;
		for(int i = 0; i < A; i++)
		{
			for(int j = 0; j < B; j++)
			{
				if( (i & j) < K) cnt++;
			}
		}
		fprintf(out,"Case #%d: %d\n",t,cnt);
	}
	fclose(in);
	fclose(out);
}