#include<stdio.h>
#include<iostream>
#include<limits.h>
using namespace std;
int  main()
{
	int a[10001],i,j,test_cases;
	cin>>test_cases;
	for(j=1;j<=test_cases;j++)
	{
		int n;
		cin>>n;
		for(i=0;i<n;i++)
		{
			cin>>a[i];
		}
		int s=0,temp,d=INT_MIN;
		int index=0;
		for(i=1;i<n;i++)
		{
			if((a[i-1]-a[i])>d)
			{
				d=a[i-1]-a[i];
			//	index=i;
			}
		}
		for(i=0;i<n-1;i++)
		{
			if(a[i]<=d)
			{
				s=s+a[i];
			}
			else
			{
				s=s+d;
			}
		}
//		printf("%d\n",s+max);
		int sum=0;
		for(i=1;i<n;i++)
		{
			if((a[i-1]-a[i])>0)
			{
				sum=sum+a[i-1]-a[i];
			}
		}
		printf("Case #%d: %d %d\n",j,sum,s);
	}
	return 0;
}
