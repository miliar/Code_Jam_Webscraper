#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int t,x,i,n,j,a;
	cin>>t;
	for(x=1;x<=t;x++)
	{
		int ar[3001];
		for(i=0;i<=3000;i++)
		{
			ar[i]=0;
		}
		cin>>n;
		for(i=0;i<(2*n-1);i++)
		{
			for(j=0;j<n;j++)
			{
				cin>>a;
				ar[a]++;
			}
		}
		cout<<"Case #"<<x<<": ";
		for(i=0;i<=3000;i++)
		{
			if(ar[i]%2==1)
			{
				cout<<i<<" ";
			}
		
		}
		cout<<endl;
	}
	
}