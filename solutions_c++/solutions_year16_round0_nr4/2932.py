#include "stdio.h"
#include "memory.h"

int main()
{
	int n;
	FILE * pFile1,*pFile2;
	pFile1 = fopen("input.in","r");
	pFile2 = fopen("output.txt","w");
	fscanf(pFile1,"%d",&n);
	int k,c,s;
	int i,j;
	for (i=1;i<=n;i++)
	{
		fscanf(pFile1,"%d %d %d",&k,&c,&s);
		fprintf(pFile2,"Case #%d: 1",i);
		for (j=2;j<=s;j++)
		{
			fprintf(pFile2," %d",j);
		}
		fprintf(pFile2,"\n");
	}
	fclose(pFile1);
	fclose(pFile2);
	return 0;
}

