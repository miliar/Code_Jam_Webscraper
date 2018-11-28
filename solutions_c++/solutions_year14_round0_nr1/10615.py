#include<stdio.h>
#include<stdlib.h>
main()
{
	int T,z;
	int ans1,ans2,Q1[5][5],Q2[5][5],flag1[17],flag2[17],FLAG=0,j,k,perm,i;
	scanf("%d",&T);
	for(z=0;z<T;z++)
	{
		FLAG=0;
		scanf("%d",&ans1);
		for(k=1;k<=4;k++)
		for(j=1;j<=4;j++)
		scanf("%d",&Q1[k][j]);
		scanf("%d",&ans2);
		for(k=1;k<=4;k++)
		for(j=1;j<=4;j++)
		scanf("%d",&Q2[k][j]);
		ans1;
		ans2;
		for(k=1;k<=16;k++)
		{
			flag1[k]=0;
			flag2[k]=0;
		}
		for(k=1;k<=4;k++)
		{
			i=Q1[ans1][k];
			//printf("Flag1 i=%d\n",i);
			flag1[i]=1;
			i=Q2[ans2][k];
			//printf("Flag2 i=%d\n",i);
			flag2[i]=1;
		}
		/*for(k=0;k<15;k++)
		{
			if(flag1[k]==1)
			printf("flag1=%d\n",k+1);
			if(flag2[k]==1)
			printf("flag2=%d\n",k+1);
		}*/
		for(k=1;k<=16;k++)
		{
			if(flag1[k]==1&&flag2[k]==1&&FLAG==0)
			{
				FLAG=1;
				perm=k;
			}
			else if(flag1[k]==1&&flag2[k]==1&&FLAG==1)
			FLAG=-1;
		}
		printf("Case #%d: ",z+1);
		if(FLAG==0)
		{
			printf("Volunteer cheated!\n");
			continue;
		}
		else if(FLAG==-1)
		printf("Bad magician!\n");
		else if(FLAG==1)
		printf("%d\n",perm);
	}
}
