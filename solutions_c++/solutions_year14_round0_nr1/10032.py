#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,a[100][20],i,j,k,n,ans,c[100],count1=1;
	//freopen("abc.txt","r",stdin);
	//freopen("rohit1.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		int count=0;
		for(j=1;j<=16;j++)
		c[j]=0;
		scanf("%d",&n);
		for(j=1;j<=4;j++)
		{
			for(k=1;k<=4;k++)
			{
				if(j==n)
				{
				scanf("%d",&a[i][j]);
				c[a[i][j]]++;
				}
				else
				scanf("%d",&a[i][j]);
			}
		}
		scanf("%d",&n);
		for(j=1;j<=4;j++)
		{
			for(k=1;k<=4;k++)
			{
				if(j==n)
				{
				scanf("%d",&a[i][j]);
				c[a[i][j]]++;
				}
				else
				scanf("%d",&a[i][j]);
			}
		}
		for(j=1;j<=16;j++)
		{
			if(c[j]==2)
			{
				count++,ans=j;
			}
		}
		if(count==1)
		printf("Case #%d: %d\n",count1++,ans);
		else if(count>1)
		printf("Case #%d: Bad magician!\n",count1++);
		else if(count==0)
		printf("Case #%d: Volunteer cheated!\n",count1++);
	}
	return 0;
}
