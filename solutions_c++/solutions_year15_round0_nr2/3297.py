#include<iostream>
#include<cstdio>
#include<cmath>
#include<climits>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	for(int l=1;l<=t;l++)
	{
		int n;
		scanf("%d",&n);
		int arr[n];
		int temp=0;
		scanf("%d",&arr[0]);
		temp=arr[0];
		for(int i=1;i<n;i++)
		{
			scanf("%d",&arr[i]);
			temp=max(temp,arr[i]);
		}

		int i=0,j;
		int count=INT_MAX;

		for(i=1;i<=temp;i++)
		{
			int total=0;
			for(j=0;j<n;j++)
			{
				total+=ceil((float)(arr[j]-i)/(float)i);
			}
			total+=i;
			//cout<<total<<endl;
			count=min(count,total);
		}
		printf("Case #%d: %d\n",l,count);
		
	}
	return 0;
}