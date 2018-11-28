#include<bits/stdc++.h>
using namespace std;

int ans = 1000;


void solve(int sum,int m,int size,int arr[])
{
	int arr1[10000];
	//cout<<"hello "<<sum<<" "<<m<<" "<<size<<endl;
	int maxi=-1,sum1,index,i;
	sum1 = sum;
	
	for(i=0;i<10000;i++)
	arr1[i] = arr[i];
	
	if(sum<=0)
	{
		ans = min(ans,m);
		return;
	}
	
	for(i=0;i<size;i++)
	{
		if(maxi<=arr[i])
		{
			maxi = arr[i];
			index = i;
		}
	}
	
	for(i=0;i<size;i++)
	{
		if(arr[i]>0)
		{
		arr[i]--;
		sum1--;
		}
	}
	
	solve(sum1,m+1,size,arr);
	
	for(i=0;i<100;i++)
	arr[i] = arr1[i];
	

	if(maxi==9)
	{
		arr[index] = 6;
		arr[size++]=3;
		solve(sum,m+1,size,arr);
	}
	else if(maxi>1)
	{
		int x = maxi/2;
		arr[index] = x;
		arr[size++] = maxi - x;
		
		solve(sum,m+1,size,arr);
	}
	
	
	
}

int main()
{
	int t,k=1;
	cin>>t;
	
	while(t--)
	{
	ans = 1000;	
	int arr[10000];
	
	int size,i,sum=0,m=0;
	
	for(i=0;i<size;i++)
	arr[i]=0;

	cin>>size;
	
	for(i=0;i<size;i++)
	{
		cin>>arr[i];
		sum+=arr[i];
	}
	
//	cout<<"sum "<<sum<<endl;
	solve(sum,m,size,arr);
	
	cout<<"Case #"<<k<<": "<<ans<<endl;
	k++;
	}
}
