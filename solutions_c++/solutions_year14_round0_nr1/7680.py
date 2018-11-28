#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<set>
using namespace std;

int main()
{
	int T,i,first,second,j,k,matrixA[8][8],matrixB[8][8],ans,card;
	set<int> magic;
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		memset(matrixA,0,sizeof(matrixA));
		memset(matrixB,0,sizeof(matrixB));
		ans=0;
		magic.clear();
		scanf("%d",&first);
		for(j=1;j<=4;j++)
		{
			for(k=1;k<=4;k++)
			{
				scanf("%d",&matrixA[j][k]);
				if(j==first)
					magic.insert(matrixA[j][k]);
			}
		}
		scanf("%d",&second);
		for(j=1;j<=4;j++)
		{
			for(k=1;k<=4;k++)
			{
				scanf("%d",&matrixB[j][k]);
				if(j==second && magic.find(matrixB[j][k])!=magic.end())
				{
					ans++;
					card=matrixB[j][k];
				}
			}
		}
		printf("Case #%d: ",i);
		if(ans==1)
			printf("%d\n",card);
		else if(ans>1)
			printf("Bad magician!\n");
		else
			printf("Volunteer cheated!\n");
		
	}
	return 0;
}