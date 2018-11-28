#include "stdio.h"
#include "string.h"
#include "math.h"
#include "memory.h"

const int neg = '+' + '-';

int arr[1000];

int main()
{
	int n;
	char buf[255];
	FILE * pFile1,*pFile2;
	pFile1 = fopen("input.in","r");
	pFile2 = fopen("output.txt","w");
	fscanf(pFile1,"%d",&n);
	int i,j,k;
	for (i=1;i<=n;i++)
	{
		int ans=0;
		fscanf(pFile1,"%s",buf);
		while (strlen(buf) == 0) fscanf(pFile1,"%d",buf);
		j = strlen(buf);
		j--;
		while (j>=0)
		{
			if (buf[j] == '+') {j--; continue;}
			if (buf[0] == '+') ans ++;
			k = 0;
			while (buf[k] == '+')
			{
				buf[k] = '-';
				k++;
			}
			for (k=0;k<=j/2;k++)
			{
				int x;
				if (k != j-k)
				{
					x = buf[k];
					buf[k] = neg-buf[j-k];
					buf[j-k] = neg-x;
				}
				else
				{
					buf[k] = neg-buf[k];
				}
			}
			ans ++;
			j--;
		}
		fprintf(pFile2,"Case #%d: %d\n",i,ans);
	}
	fclose(pFile1);
	fclose(pFile2);
	return 0;
}

