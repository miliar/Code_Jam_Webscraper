#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int caseNum, totalCaseNum;
FILE *fin, *fout;

char S[1001], str[2001];

void solve()
{
	int i, len;
	int begin = 1000, end = 1000;
	len = strlen(S);
	
	str[begin] = S[0];
	for(i=1; i<len; i++)
	{
		if(S[i] >= str[begin]) str[--begin] = S[i];
		else str[++end] = S[i];
	}

	fprintf(fout, "Case #%d: ", caseNum+1);
	for(i=begin; i<=end; i++) fprintf(fout, "%c", str[i]);
	fprintf(fout, "\n");
}

int main()
{
	fin = fopen("sample_input.in", "r");
	fout = fopen("sample_output.out", "w");

	fscanf(fin, "%d", &totalCaseNum);

	for(caseNum=0; caseNum<totalCaseNum; caseNum++)
	{
		fscanf(fin, "%s", S);
		solve();
	}

	fcloseall();

	return 0;
}