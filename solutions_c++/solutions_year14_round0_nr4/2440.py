#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#include<iostream>
#include<queue>
using namespace std;
#define ll long long
#define inf 0x3f3f3f3f

double a[1010],b[1010];
int main()
{
	int t;
	scanf("%d",&t);
	int he=0;
	while(t--)
	{
		he++;
		int n,i,j,k;
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%lf",&a[i]);
		for(i=0;i<n;i++)
			scanf("%lf",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		int ans=0;
		i=0;j=0;
		while(i<n && j<n)
		{
			if(b[j]>a[i])
				ans++,i++,j++;
			else
				j++;
		}
		int sum=0;
		i=n-1,j=n-1;
		while(i>=sum && j>=0)
		{
			if(a[i]>b[j])
				i--,j--;
			else
				sum++,j--;
		}
		printf("Case #%d: ",he);
		printf("%d %d\n",n-sum,n-ans);
	}
}