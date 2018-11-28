#include <iostream>
#include<stdio.h>

#include<algorithm>
using namespace std;

int main() 
{
	long long t,n,k=0,i,ans1,ans2,countw,countdw,j;
	cin>>t;
	while(t--)
	{
		cin>>n;
		long double a[n],b[n];
		for(i=0;i<n;i++)
		cin>>a[i];
		
		for(i=0;i<n;i++)
		cin>>b[i];
		
		sort(a,a+n);
		sort(b,b+n);
		
	
		
		countdw=0;
		for(i=0,j=0;i<n && j<n;)
		{
			if(a[i]<b[j])
			{
				countdw++;
				i++;
				j++;
			}
			else
			j++;
		
		}
		countdw=n-countdw;
		
		countw=0;
		for(i=0,j=0;i<n && j<n;)
		{
			if(a[i]>b[j])
			{
				
				countw++;
				i++;
				j++;
			}
			else
			i++;
		}
		
		k++;
		printf("Case #%lld: %lld %lld\n",k,countw,countdw);
	}
	
	
	return 0;
}