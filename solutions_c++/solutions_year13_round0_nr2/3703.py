#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
using namespace std;

const int M = 102;
int grass[M][M], n, m;

bool judge(int x,int y)
{
	int cot = 0;
	for(int i=0;i<m;i++)
		if(grass[x][i] > grass[x][y])
		{
			cot ++;
			break;
		}
	for(int j=0;j<n;j++)
		if(grass[j][y] > grass[x][y])
		{
			cot ++;
			break;
		}
	if(cot < 2)
		return true;
	return false;
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int cas=1;cas<=T;cas++)
	{
		scanf("%d %d", &n, &m);
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				scanf("%d", &grass[i][j]);

		bool flag = false;
		for(int i=0;i<n;i++)
		{
			if(flag)
				break;
			for(int j=0;j<m;j++)
				if(!judge(i, j))
				{
					flag = true;
					break;
				}
		}
		
		if(!flag)
			printf("Case #%d: YES\n",cas);
		else
			printf("Case #%d: NO\n",cas);
	}
	return 0;
}
