#include <stdio.h>
#include <stdlib.h>
#include <string.h>

FILE *fin, *fout;


int solve(char *str)
{
	int i, cnt = 0;
	int len = strlen(str);
	char ch = '+';

	for(i=len-1; i>=0; i--)
	{
		if(str[i] == '-') break;
	}

	for(;i>=0; i--)
	{
		if(str[i] != ch)
		{
			ch = str[i];
			cnt++;
		}
	}

	return cnt;
}


int main()
{
	int i, totalCaseNum;
	char str[110];

	fin = fopen("B-large.in", "r");
	fout = fopen("B-large.out", "w");

	fscanf(fin, "%d", &totalCaseNum);

	for(i=0; i<totalCaseNum; i++)
	{
		fscanf(fin, "%s", str);
		fprintf(fout, "Case #%d: %d\n", i+1, solve(str));
	}

	fcloseall();

	return 0;
}