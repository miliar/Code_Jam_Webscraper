#include<stdio.h>
#include<iostream>

int main()
{
	int t,T,n,m,mat1[4][4],mat2[4][4],count,ans;
	scanf("%d",&t);
	T=t;
	while(t--)
	{
		count=ans=0;
		scanf("%d",&n);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
				scanf("%d",&mat1[i][j]);
		}
		scanf("%d",&m);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
				scanf("%d",&mat2[i][j]);
		}
		n--;
		m--;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(mat1[n][i]==mat2[m][j])
				{
					count++;
					ans=mat1[n][i];
				}
				if(count>1)
					break;
			}
			if(count>1)
				break;
		}
		printf("Case #%d: ",T-t);
		if(count==1)
			printf("%d\n",ans);
		else if(count==0)
			printf("Volunteer cheated!\n");
		else if(count>1)
			printf("Bad magician!\n");
	}
	return 0;
}
