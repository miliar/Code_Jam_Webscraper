#include<stdio.h>
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("siku1.txt","w",stdout);
	int t,test=0,cnt=0;
	scanf("%d",&t);
	while(t--)
	{
		cnt=0;
		test++;
		int in[4][4],in1[4][4];
		int s[4];
		int index,i,j,k;
		scanf("%d",&index);
		index=index-1;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%d",&in[i][j]);
				if(i==index)
				s[j]=in[i][j];
			}
		}
		int index1,ans=0;
		scanf("%d",&index1);
		index1=index1-1;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%d",&in1[i][j]);
				if(i==index1)
				{
					for(k=0;k<4;k++)
					{
						if(s[k]==in1[i][j])
						{
						cnt=cnt+1;
						ans=s[k];
						}
					}	
				}
			}
		}
		if(cnt==0)
		printf("Case #%d: Volunteer cheated!\n",test);
		else if (cnt==1)
		printf("Case #%d: %d\n",test,ans);
		else if(cnt>1)
		printf("Case #%d: Bad magician!\n",test);
		
		
	}
	return 0;
}
