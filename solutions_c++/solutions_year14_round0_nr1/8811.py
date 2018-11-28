#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	for(int tt=1;tt<=t;tt++)
	{
		int ar[20] = {0};
		int ans1,ans2,temp;
		scanf("%d",&ans1);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d",&temp);
				if (ans1 == i+1)
				{
					ar[temp]++;
				}
			}
		}
		int sum = 0;
		int ans ;
		scanf("%d",&ans2);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d",&temp);
				if (ans2 == i+1)
				{
					if(ar[temp]) {sum++;ans = temp;}
					else ar[temp]++;
				}
			}
		}
		if(sum == 0)
		{
			printf("Case #%d: Volunteer cheated!\n",tt);
		}
		else if(sum == 1)
		{
			printf("Case #%d: %d\n",tt,ans);
		}
		else
		{
			printf("Case #%d: Bad magician!\n",tt);
		}
	}
}