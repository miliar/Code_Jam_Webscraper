#include<stdio.h>
int a[10][10];
int b[10][10];
int main()
{
	int T;
	int count=0;
	int fi,se;
	int ans;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		scanf("%d",&fi);
		count=0;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&a[i][j]);
		scanf("%d",&se);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d",&b[i][j]);
			}
		}
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(a[fi-1][i]==b[se-1][j])
				{
					count++;
					ans=a[fi-1][i];
				}
			}
		}
		printf("Case #%d: ",t);
		if(count==1)
			printf("%d",ans);
		else if(count>1)
			printf("Bad magician!");
		else if(count==0)
			printf("Volunteer cheated!");
		printf("\n");
	}	
}
