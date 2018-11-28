#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>

const int MAX=3000;

int main()
{
	FILE* inf=fopen("A-small-attempt3.in", "r");
	FILE* outf=fopen("A-small-attempt3.out", "w");
	int T, n;
	char s[MAX];
	int A[MAX];
	int sum[MAX];
	memset(A, 0, sizeof(A));
	memset(sum, 0, sizeof(sum));
	fscanf(inf, "%d", &T);

	for(int i=1; i<=T; i++)
	{
		memset(A, 0, sizeof(A));
		memset(sum, 0, sizeof(sum));
		fscanf(inf, "%d", &n);
		fscanf(inf, "%s", s);
		for(int j=0; j<=n; j++)
		{
			A[j]=int(s[j]-'0');
			if(j==0) sum[j]=A[j];
			else sum[j]=sum[j-1]+A[j];
		}

		int count=0;
		for(int j=1; j<=n; j++)
			if(A[j]>0)
			if(sum[j-1]+count<j) count+=j-sum[j-1]-count;

		fprintf(outf, "Case #%d: %d\n", i, count);
	}

	fclose(inf);
	fclose(outf);
	return 0;
}

