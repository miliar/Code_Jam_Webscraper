#include <stdio.h>


int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int nCases,fChoice,sChoice;
	int fVector[16],sVector[16];
	int cnt=16,nSame=0,s;
	scanf("%d",&nCases);
	int i,j,k;
	for(i=0;i<nCases;i++)
	{
		scanf("%d",&fChoice);
		for(j=0;j<16;j++)
		{
			scanf("%d",&fVector[j]);
		}
		scanf("%d",&sChoice);
		for(j=0;j<16;j++)
		{
			scanf("%d",&sVector[j]);
		}
		nSame=0;
		for(j=(fChoice-1)*4;j<fChoice*4 && j<16;j++)
		{
			for(k=(sChoice-1)*4;k<sChoice*4 && k<16;k++)
			{
				if(fVector[j]==sVector[k])
				{
					s=fVector[j];
					nSame++;
				}
			}
		}
		printf("Case #%d: ",i+1);
		if(nSame==1)
		{
			printf("%d\n",s);
		}
		else if(nSame>1)
		{
			printf("Bad magician!\n");
		}
		else
		{
			printf("Volunteer cheated!\n");
		}
	}
	return 0;
}