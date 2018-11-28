#include<iostream>
#include<stdio.h>
using namespace std;
int a1[100][100],a2[100][100];
int main()
{
	int i,j,t1,t2,k,tp,tt,ii;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("000.txt","w",stdout);
	scanf("%d",&tt);
	for(ii=1;ii<=tt;ii++)
	{
		scanf("%d",&t1);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				scanf("%d",&a1[i][j]);
		scanf("%d",&t2);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				scanf("%d",&a2[i][j]);
		k=0;
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				if (a1[t1][i]==a2[t2][j])  {k++;tp=a1[t1][i];}
		if (k==0)
		{
			printf("Case #%d: Volunteer cheated!\n",ii);
		}
		if (k==1)
		{
			printf("Case #%d: %d\n",ii,tp);
		}
		if (k>1)
		{
			printf("Case #%d: Bad magician!\n",ii);
		}


	}
}