#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<cstring>
using namespace std;
int main()
{
		freopen("A-small-attempt0.in","r",stdin);
		freopen("output.txt","w",stdout);
	int t,t1=0,i,j,x,y,a[5][5],b[5][5],count,ans;
	scanf("%d",&t);
	while(t--)
	{
		t1++;
		scanf("%d",&x);
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				scanf("%d",&a[i][j]);
			}
		}
		scanf("%d",&y);
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				scanf("%d",&b[i][j]);
			}
		}
		count=0;
		for(i=1;i<=4;i++)
		{
		
		for(j=1;j<=4;j++)
		{
			if(a[x][i] == b[y][j])
			{
				count++;
				ans=a[x][i];
			}
		}
		
		}
		if(count == 1)
		{
			printf("Case #%d: %d\n",t1,ans);
		}
		else if(count > 1)
		{
			printf("Case #%d: Bad magician!\n",t1);

		}
		else if(count == 0 )
		{
			printf("Case #%d: Volunteer cheated!\n",t1);
		}
	
	
	}
	return 0;
}
