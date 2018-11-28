#include "stdio.h"
#include "stdlib.h"
#include "string.h"




int isPalindrom(unsigned long res)
{
	char buf[256];
	int i, j, strLen;
	if (res < 10)
	{
		return 1;
	}
	ultoa(res,buf,10);
	strLen = strlen(buf);

	for (i=0, j=strLen-1; i<j; i++, j--)
	{
		if(buf[i] != buf[j])
		{
			return 0;
		}
	}

	return 1;
}

int main()
{
	int T = 0;
	int fnsShort[] = {1,4,9,121,484};
	int t, i, j, possible, cnt, N,M;
	unsigned long fns [10000];
	unsigned long li, lj;
	FILE* fIn = fopen("C-small-attempt1 (1).in", "r");
	FILE* fOut = fopen("solutionC.out", "w");
	fscanf(fIn, "%d\n", &T);
	
	//cnt = 0;
	//for (li =0; li < 0xffffffff; li++)
	//{
	//	lj = li*li;
	//	if(isPalindrom(lj))
	//	{
	//		fns[cnt++] = lj;
	//	}

	//}

	for (t=1; t<=T; t++)
	{
		fscanf(fIn, "%d %d\n", &N, &M);
		for(i=0; i< 5; i++)
		{
			if(N <= fnsShort[i])
			{
				break;
			}
		}
		j=i;
		for(; j< 5; j++)
		{
			if(M < fnsShort[j])
			{
				break;
			}
		}

		fprintf(fOut, "Case #%d: %d\n", t, (j-i));
	}
}
