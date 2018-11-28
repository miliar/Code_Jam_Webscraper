#include "stdio.h"
#include "string.h"
#include "math.h"
#include "memory.h"

FILE * pFile1,*pFile2;

const int max = 15;

int num[100];

int ans = 50;

int left = 16384;

long long convert(int base)
{
	long long res = 0;
	long long x = 1;
	int i,j;
	for (i=max;i>=0;i--)
	{
		res += num[i]*x;
		x *= base;
	}
	return res;
}

int prime(long long x)
{
	long long testmax = (long long)sqrt(x)+1;
	long long i;
	for (i=2;i<=testmax;i++)
	{
		if (x % i == 0)
		{
			return i;
		}
	}
	return 0;
}

void verify()
{
	int i,j,k;
	int ok = 1;
	long long res[12];
	memset(res,0,sizeof(res));
	for (i=2;i<=10;i++)
	{
		long long x = convert(i);
		res[i] = prime(x);
		if (res[i] == 0) return;
	}
	ans --;
	printf("Found a new number! Only %d/50 left!",ans);
	for (i=0;i<=max;i++)
	{
		fprintf(pFile2,"%d",num[i]);
	}
	for (i=2;i<=10;i++)
	{
		fprintf(pFile2," %lld",res[i]);
	}
	fprintf(pFile2,"\n");
}

void dfs(int d)
{
	if (d == max)
	{
		printf("%d/16384 left...\n",left);
		verify();
		left--;
		return;
	}
	dfs(d+1);
	if (ans <= 0) return;
	num[d] = 1;
	dfs(d+1);
	num[d] = 0;
}

int main()
{
	int n;
	pFile2 = fopen("output.txt","w");
	fprintf(pFile2,"Case #1:\n");
	num[0] = 1;
	num[max] = 1;
	dfs(1);
	fclose(pFile2);
	return 0;
}

