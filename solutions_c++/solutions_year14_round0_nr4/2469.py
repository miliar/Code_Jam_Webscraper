#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int tc;int c=1;
	scanf("%d",&tc);
	while(tc--)
	{
		int n;
		scanf("%d",&n);
		double arr[n],crr[n],arr1[n],crr1[n];
		for(int i=0;i<n;i++)
			scanf("%lf",&arr[i]);
		for(int j=0;j<n;j++)
			scanf("%lf",&crr[j]);
		sort(arr,arr+n);
		sort(crr,crr+n);
		for(int i=0;i<n;i++)
			arr1[i]=arr[i];
		for(int j=0;j<n;j++)
			crr1[j]=crr[j];
		int x=0;
		for(int i=n-1;i>=0;i--)
		{
			sort(crr,crr+n);int j=0;bool flag=0;
			for(;j<n;j++)
			{
				if(crr[j]!=-1&&crr[j]>arr[i])
				{
					flag=1;
					crr[j]=-1;
					break;
				}
			}
			if(!flag)
			{
				for(j=0;j<n;j++)
				{
					if(crr[j]!=-1)
					{
						crr[j]=-1;x++;
						break;
					}
				}
			}
		}
		int y=0;
		for(int i=0;i<n;i++)
		{
			sort(crr1,crr1+n);
			for(int j=0;j<n;j++)
			{
				if(arr1[i]>crr1[j]&&crr1[j]!=-1)
				{
					y++;
					crr1[j]=-1;
					break;
				}
				else if(crr1[j]!=-1)
				{
					crr1[n-1]=-1;
					break;
				}
			}
		}
		printf("Case #%d: %d %d\n",c,y,x);
		c++;
	}
}
