#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<string.h>
#include<math.h>
#include<queue>
#include<vector>
#include<stack>
#include<set>
#include<cstring>
#include<cassert>

using namespace std;
int main()
{
	long long  t,i=0;
	scanf("%lld",&t);
	while(t--)
	{	
		i++;
		printf("Case #%lld: ",i);
		int x,y, matrixA[4][4], matrixB[4][4];
		vector<int> result;
		result.clear();
		scanf("%d",&x);
		for(int i=0;i<4;++i)
			for(int j=0;j<4;++j)
				scanf("%d",&matrixA[i][j]);
		scanf("%d",&y);
		for(int i=0;i<4;++i)
			for(int j=0;j<4;++j)
				scanf("%d",&matrixB[i][j]);
		x--; y--;
		for(int i=0;i<4;++i)
		{
			for(int j=0;j<4;++j)
				if(matrixA[x][i]==matrixB[y][j]) result.push_back(matrixA[x][i]);
		}
		if(result.size()==1) printf("%d\n",result[0]);
		else if(result.size() == 0) printf("Volunteer cheated!\n");
		else printf("Bad magician!\n");
	}
	return 0;
}
