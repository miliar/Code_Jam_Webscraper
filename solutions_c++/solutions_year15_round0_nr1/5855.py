#include "stdio.h"
#include "iostream"


int main£¨)
{
	FILE * finp;
	FILE * foutp;

	int t;
	int an;
	int n;
	char in[1001];
	int num;
	if ((finp = fopen("1.in", "r")) == NULL)
	{
		printf("error");
		exit(0);
	}
	if ((foutp = fopen("1.out", "w")) == NULL)
	{
		printf("error");
		exit(0);
	}

	fscanf(finp, "%d", &t);

	for (int i = 0; i<t; i++)
	{
		an = 0; num = 0;
		fscanf(finp, "%d", &n);
		fscanf(finp, "%s", in);
		for (int j = 0; j <= n; j++)
		{	
			if (num < j)
			{
				an += j - num;
				num =j;
			}
			num += in[j]-'0';
		}
		fprintf(foutp, "Case #%d: %d\n", i + 1, an);
	}

	fclose(finp);
	fclose(foutp);

	return 0;
}
