#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int T,a,i,n,j,b;
	cin>>T;
	for(a=1;a<=T;a++)
	{
		int q[3001];
		for(i=0;i<=3000;i++)
		{
			q[i]=0;
		}
		cin>>n;
		for(i=0;i<(2*n-1);i++)
		{
			for(j=0;j<n;j++)
			{
				cin>>b;
				q[b]++;
			}
		}
		cout<<"Case #"<<a<<": ";
		for(i=0;i<=3000;i++)
		{
			if(q[i]%2==1)
			{
				cout<<i<<" ";
			}
		
		}
		cout<<"\n";
	}
	
}