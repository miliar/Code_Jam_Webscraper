#include<stdio.h>
#include<iostream>
using namespace std;

int main()
{
	freopen("test1.in","rt",stdin);
    freopen("output1.out","wt",stdout);
	int t,i,j,n,arr[1500];
	long int case1=0,case2=0,maxdiff=0;
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		case1=0;case2=0;maxdiff=0;
		scanf("%d",&n);
		for(j=0;j<n;j++)
			scanf("%d",&arr[j]);
		for(j=0;j<n-1;j++)
		{
			if(arr[j]>arr[j+1])
				case1+=(arr[j]-arr[j+1]);
		}
		for(j=0;j<n-1;j++)
		{
			if(arr[j]>arr[j+1])
			{
				if((arr[j]-arr[j+1])>maxdiff)
					maxdiff=(arr[j]-arr[j+1]);
			}			
		}
		for(j=0;j<n-1;j++)
		{
			if(arr[j]<maxdiff)
				case2+=arr[j];
			else if(arr[j]>=maxdiff)
				case2+=maxdiff;
		}
		printf("Case #%d: %ld  %ld\n",i+1,case1,case2);
	}
}
