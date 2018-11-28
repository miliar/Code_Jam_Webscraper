#include<cstdio>
using namespace std;

int main()
{
	int tc;
	int row;
	int arr[4][4];
	int ans1[4];
	int ans;
	int count;
	
	scanf("%d",&tc);
	for(int t=1;t<=tc;t++)
	{
		count=0;
		scanf("%d",&row);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				scanf("%d",&arr[i][j]);
				if(i==row-1)
					ans1[j]=arr[i][j];
			}
		
		scanf("%d",&row);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				scanf("%d",&arr[i][j]);
				if(i==row-1)
				{
					for(int k=0;k<4;k++)
					{
						if(arr[i][j]==ans1[k])
						{
							count++;
							ans=arr[i][j];
						}
					}
				}
			}
		printf("Case #%d: ",t);
		if(count==0)
			printf("Volunteer cheated!\n");
		else if(count==1)
			printf("%d\n",ans);
		else
			printf("Bad magician!\n");
		
	
	
	}
	


}