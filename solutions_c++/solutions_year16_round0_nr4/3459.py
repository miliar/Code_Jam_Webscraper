#include <stdio.h>
#include <stdlib.h>
#include <math.h>

FILE *fin, *fout;


void solve(int K, int C, int S)
{
	int i;
	long long site;

	for(i=0; i<S; i++)
	{
		site = (long long)1 + (long long)pow((double)K, C-1)*(long long)i;
		fprintf(fout, "%lld ", site);
	}

	fprintf(fout, "\n");
}


int main()
{
	int i, totalCaseNum;
	int K, C, S;

	fin = fopen("D-small-attempt0.in", "r");
	fout = fopen("D-small-attempt0.out", "w");

	fscanf(fin, "%d", &totalCaseNum);

	for(i=0; i<totalCaseNum; i++)
	{
		fscanf(fin, "%d %d %d", &K, &C, &S);
		fprintf(fout, "Case #%d: ", i+1);
		solve(K, C, S);
	}

	fcloseall();

	return 0;
}