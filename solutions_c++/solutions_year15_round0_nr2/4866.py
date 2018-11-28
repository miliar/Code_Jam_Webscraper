#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	for(int tt=1;tt<=t;tt++)
	{
		int d;
		scanf("%d",&d);
		int p[d];
		int temp=0;
		scanf("%d",&p[0]);
		temp=p[0];
		for(int i=1;i<d;i++)
		{
			scanf("%d",&p[i]);
			temp=max(temp,p[i]);
		}

		int i=0,j;
		int count=99999;

		for(i=1;i<=temp;i++)
		{
			int sum=0;
			for(j=0;j<d;j++)
			{
				sum+=ceil((float)(p[j]-i)/(float)i);
			}
			sum+=i;
			//cout<<sum<<endl;
			count=min(count,sum);
		}
		printf("Case #%d: %d\n",tt,count);
		
	}
	return 0;
}