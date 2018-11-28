#include <iostream>
#include<stdio.h>
using namespace std;
#include<algorithm>

int main() 
{
	long long t,n,k=0,i,ans1,ans2,count1,count2,j;
	cin>>t;
	while(t--)
	{
		cin>>n;
		long double arr[n],brr[n];
		for(i=0;i<n;i++)
		cin>>arr[i];
		
		for(i=0;i<n;i++)
		cin>>brr[i];
		
		sort(arr,arr+n);
		sort(brr,brr+n);
		
	/*	for(i=0;i<n;i++)
		cout<<arr[i]<<" ";
		
		cout<<endl;
		
		for(i=0;i<n;i++)
		cout<<brr[i]<<" ";*/
		
		count2=0;
		for(i=0,j=0;i<n && j<n;)
		{
			if(arr[i]<brr[j])
			{
				count2++;
				i++;
				j++;
			}
			else
			j++;
		
		}
		ans2=n-count2;
		
		count1=0;
		for(i=0,j=0;i<n && j<n;)
		{
			if(arr[i]>brr[j])
			{
				//cout<<"A"<<arr[i]<<" "<<brr[j];
				count1++;
				i++;
				j++;
			}
			else
			i++;
		}
		ans1=count1;
		k++;
		printf("Case #%lld: %lld %lld\n",k,ans1,ans2);
	}
	
	
	return 0;
}