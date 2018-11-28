#include<stdio.h>
int t,a1,a2,i,j,c1[4][4],c2[4][4],flag,c,ans;
int main()
{
	scanf("%d",&t);
	c=0;
	while(t--)
	{
		scanf("%d",&a1);
		for(i=0;i<4;++i)
		{
			for(j=0;j<4;++j)
			{
				scanf("%d",&c1[i][j]);
			}
		}
		scanf("%d",&a2);
		for(i=0;i<4;++i)
		{
			for(j=0;j<4;++j)
			{
				scanf("%d",&c2[i][j]);
			}
		}
		flag=0;
		for(i=0;i<4;++i)
		{
			for(j=0;j<4;++j)
			{
				if(c1[a1-1][i]==c2[a2-1][j] && flag==0)
				{
					ans=c1[a1-1][i];
					flag=1;
				}
				else if(c1[a1-1][i]==c2[a2-1][j] && flag==1)
				{
					flag=-1;
					break;
				}
			}
		}
		++c;
		if(flag==0)
		{
			printf("Case #%d: Volunteer cheated!\n",c);
		}
		else if(flag==-1)
		{
			printf("Case #%d: Bad magician!\n",c);
		}
		else
		{
			printf("Case #%d: %d\n",c,ans);
		}
	}
	return 0;
}
