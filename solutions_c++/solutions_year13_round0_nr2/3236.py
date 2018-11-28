#include <stdio.h>
#include <memory.h>
#include <limits.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <list>
#include <map>

using namespace std;

int T;
int N,M;
int input[110][110];
int test[110][110];

int main()
{
	scanf("%d",&T);
	for(int i = 0; i<  T;i++)
	{
		bool result = true;
		scanf("%d %d",&N,&M);
		for(int j = 0; j < N;j++)
			for(int k = 0; k < M;k++)
			{
				scanf("%d",&input[j][k]);
				test[j][k] = 100;
			}
		int maxX[110];
		int maxY[110];
		memset(maxX,0,sizeof maxX);
		memset(maxY,0,sizeof maxY);
		for(int j = 0; j < N;j++)
		{
			for(int k = 0; k < M;k++)
			{
				maxX[j] = max(maxX[j],input[j][k]);
				maxY[k] = max(maxY[k],input[j][k]);
			}
		}
		for(int j = 0; j < N;j++)
		{
			for(int k = 0; k < M;k++)
			{
				test[j][k] = maxX[j];
				test[j][k] = min(test[j][k],maxY[k]);
				if(test[j][k] != input[j][k])
					result = false;
			}
		}
		
		if(result)
			printf("Case #%d: YES\n",i+1);
		else
			printf("Case #%d: NO\n",i+1);
	}
	return 0;
}

