#include<stdio.h>

int ans,x[5][5],y[5][5],check[20];

int main()
{
	int i,j,k,q,s,e,chk=0;
	scanf("%d",&q);
	for(i=1;i<=q;i++)
	{
		chk=0;
		for(j=0;j<20;j++)
			check[j]=0;
		scanf("%d",&s);
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				scanf("%d",&x[j][k]);
				if(j==s-1)
					check[x[j][k]]++;
			}
		}
		scanf("%d",&e);
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				scanf("%d",&y[j][k]);
				if(j==e-1)
					check[y[j][k]]++;
			}
		}
		for(j=1;j<=16;j++)
		{
			if(check[j]==2)
			{
				ans=j;
				chk++;
			}
		}
		printf("Case #%d: ",i);
		if(chk==0)
		{
			printf("Volunteer cheated!\n");
		}
		else if(chk==1)
		{
			printf("%d\n",ans);
		}
		else
		{
			printf("Bad magician!\n");
		}
	}
	return 0;
}
