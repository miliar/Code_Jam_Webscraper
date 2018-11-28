#include <iostream>
#include <algorithm>
#include <math.h>
#include <stdio.h>
#include <string.h>

using namespace std;

int nump[30];
int order[30];
int N;
int sum;

bool cmp(int a, int b)
{
	if(nump[a]>nump[b])
		return true;
	else
		return false;
}

void plan()
{
	sort(order, order+N, cmp);
	/*for(int i=0;i<N;i++)
		printf("%d ", order[i]);
	printf("\n");*/
	int a1=order[0], a2=order[1];
	if(nump[a1]==nump[a2])
	{
		if(2<N && nump[a2]==nump[order[2]])
		{
			printf(" %c", 'A'+a1);
			nump[a1]--;
			sum--;
		}
		else
		{
			printf(" %c%c", 'A'+a1, 'A'+a2);
			nump[a1]--;
			nump[a2]--;
			sum=sum-2;
		}
	}
	else
	{
		printf(" %c", 'A'+a1);
		nump[a1]--;
		sum=sum-1;
	}
	if(sum>0)
		plan();
}

int main()
{
	int test_case;
	scanf("%d", &test_case);
	
	for (int i = 0; i < test_case; i++)
	{
		scanf("%d", &N);
		sum=0;
		for(int i=0;i<N;i++)
		{
			scanf("%d", &nump[i]);
			order[i]=i;
			sum+=nump[i];
		}
		printf("Case #%d:", i+1);
		plan();
		printf("\n");
	}
	
	return 0;
}
