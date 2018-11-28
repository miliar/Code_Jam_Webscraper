#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	int T,i,ar[17],m,n,x,count,ans,flag=0,y=1;
	scanf("%d",&T);
	while(T--)
	{
		flag=0;
		count=0;
		for(i=1;i<=16;i++)
			ar[i]=0;
		scanf("%d",&m);
		for(i=1;i<=16;i++)
		{
			scanf("%d",&x);
			n=4*(m-1);
			if(i>n && i<=n+4)
			{
				ar[x]++;
			}
		}
		scanf("%d",&m);
		for(i=1;i<=16;i++)
		{
			scanf("%d",&x);
			n=4*(m-1);
			if(i>n && i<=n+4)
			{
				ar[x]++;
			}
		}
		for(i=1;i<=16;i++)
		{
			if(ar[i]==2)
			{
				count++;
				if(count>=2)
					break;
				else
					ans=i;
			}
		}
		if(count==1)
			printf("Case #%d: %d\n",y,ans);
		else if(count==0)
			printf("Case #%d: Volunteer cheated!\n",y);
		else
			printf("Case #%d: Bad magician!\n",y);
			
			y++;
	}
	
	
	
	return 0;
}
