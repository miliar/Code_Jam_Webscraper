#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	for(int z=1;z<=t;z++)
	{
		int p[1010];
		int n,i,j,max1,min1,sum;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d",&p[i]);
			max1=max(max1,p[i]);
			}
		min1=max1;
		for(i=1;i<=max1;i++)
		{
			sum=i;
			for(j=0;j<n;j++)
			{
				if(p[j]>i)
				{
					if(p[j]%i == 0)
					sum += (p[j] / i-1);
					else
					sum+=(p[j]/i);
					}
				}
			min1=min(min1,sum);
			}
		printf("Case #%d: %d\n",z,min1);
		}
	return 0;
	}
