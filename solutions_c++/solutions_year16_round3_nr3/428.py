#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;

#define MAXCOMBINE 1333

int cas,T;
int J,P,S,K,numcombine,combine[MAXCOMBINE],cntK[MAXCOMBINE];
bool b_combine[MAXCOMBINE], maxcombine[MAXCOMBINE];

void backtrace(int now, int num, int outputnum)
{
	if (num == numcombine)
	{
		memset(cntK, 0, sizeof(cntK));
/*	
		for (int i = 0; i < numcombine; ++i)
		{
			if (b_combine[i] == true)
			{
				printf("%d ", i);
			}
		}
		printf("\n");
*/		
		for (int i = 0; i < numcombine; ++i)
		{
			int tmp = combine[i];
			if (b_combine[i] == true)
			{
//				printf("%d %d %d %d %d\n", i, tmp, tmp-tmp%11, tmp-tmp%121+tmp%11, tmp%121);
				++cntK[tmp];
				if (cntK[tmp] == 2)
				{
					return;
				}
				++cntK[tmp-tmp%11];
				if (cntK[tmp-tmp%11] > K)
				{
					return;
				}
				++cntK[tmp-tmp%121+tmp%11];
				if (cntK[tmp-tmp%121+tmp%11] > K)
				{
					return;
				}
				++cntK[tmp%121];
				if (cntK[tmp%121] > K)
				{
					return;
				}
			}
		}
		
		combine[MAXCOMBINE-1] = 0;
		for (int i = 0; i < numcombine; ++i)
		{
			if (b_combine[i] == true)
			{
				++combine[MAXCOMBINE-1];
			}
		}
		if (combine[MAXCOMBINE-1] > combine[MAXCOMBINE-2])
		{
			for (int i = 0; i < numcombine; ++i)
			{
				if (b_combine[i] == true)
				{
					maxcombine[i] = true;
				}
				else
				{
					maxcombine[i] = false;
				}
			}
			combine[MAXCOMBINE-2] = combine[MAXCOMBINE-1];
		}
		return;
	}
	b_combine[now] = true;
	if (combine[MAXCOMBINE-2] < outputnum+1+numcombine-(now+1))
	{
		backtrace(now+1, num+1, outputnum+1);
	}
//	printf("\n");
	b_combine[now] = false;
	if (combine[MAXCOMBINE-2] < outputnum+1+numcombine-(now+1))
	{
		backtrace(now+1, num+1, outputnum);
	}
//	printf("\n");
}

int main()
{
	freopen ("C-small-attempt1.in","r",stdin);
    freopen ("C-small-attempt1.out","w",stdout);
	
	scanf("%d", &T);
	for (cas = 1; cas <= T; ++cas)
	{
		scanf("%d%d%d%d", &J, &P, &S, &K);
		numcombine = 0;
		memset(b_combine, false, sizeof(b_combine));
		memset(combine, 0, sizeof(combine));
		memset(maxcombine, 0, sizeof(maxcombine));
		for (int i = 1; i <= J; ++i)
		{
			for (int j = 1; j <= P; ++j)
			{
				for (int k = 1; k <= S; ++k)
				{
					combine[numcombine++] = 121*i + 11*j + k;
				}
			}
		}
		backtrace(0,0,0);

		printf("Case #%d: %d", cas, combine[MAXCOMBINE-2]);
		printf("\n");
		for (int i = 0; i < numcombine; ++i)
		{
			if (maxcombine[i] == true)
			{
				int tmp = combine[i];
				printf("%d %d %d\n", tmp/121, (tmp%121-tmp%11)/11, tmp%11);
			}
		}
	}
	
	return 0;
}