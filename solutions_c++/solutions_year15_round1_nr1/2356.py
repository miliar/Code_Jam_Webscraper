#include <iostream>
#include <stdio.h>
#include <algorithm>
#include<limits.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);

	for(int i=0;i<t;i++)
	{
		int n;
		cin>>n;

		int a[10001];
		int d=INT_MIN;
		int s=0;

		cin>>a[0];

		for(int j=1;j<n;j++)
		{
			cin>>a[j];
			if(a[j-1]-a[j]>0)
				s=s+a[j-1]-a[j];

		}

		for(int j=1;j<n;j++)
		{
			if(d<a[j-1]-a[j])
				d=a[j-1]-a[j];
		}

		int x=0;

		for(int j=0;j<n-1;j++)
		{
			if(a[j]<=d)
				x=x+a[j];
			else
				x=x+d;
		}

		printf("Case #%d: %d %d\n",i+1,s,x);
	}

	return 0;

}
				

		

		


