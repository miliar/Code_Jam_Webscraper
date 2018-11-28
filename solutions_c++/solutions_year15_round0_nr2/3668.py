#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t,k=1;
	scanf("%d",&t);
	while(t--)
	{
		int i,j,d,max=0,min=999999;
		int step,cost=0;
		scanf("%d",&d);
		int a[d+1];
		for(i=0;i<d;i++)
		{
			scanf("%d",&a[i]);
			if(a[i] > max)
				max=a[i];
		}
	
		for(i=1;i<=max;i++)
		{
			for(j=0;j<d;j++)
			{
				if(a[j] % i== 0)
				{
					step = (a[j]/i)-1;
					cost +=step;
				}
				else
				{
					step = (a[j]/i);
					cost +=step;
				}
				
			}
			cost +=i;
				if(cost <= min )
					min=cost;
			cost=0;
		}
		printf("Case #%d: %d\n",k,min);
		k++;
	}
	return 0;
}
