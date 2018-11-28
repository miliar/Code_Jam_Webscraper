#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t,n,x;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>n;
		int a[4];
		for(int j=1;j<=4;j++)
		{
			for(int k=1;k<=4;k++)
			{
				cin>>x;
				if(j==n)
				{
					a[k-1]=x;
				}
			}
		}
		cin>>n;
		int b[4];
		for(int j=1;j<=4;j++)
		{
			for(int k=1;k<=4;k++)
			{
				cin>>x;
				if(j==n)
				{
					b[k-1]=x;	
				}
			}
		}
		int cnt=0,val;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				if(a[j]==b[k])
				{
					cnt++;
					val=a[j];
				}
			}
		}
		if(cnt==1)
		{
			cout<<"Case #"<<i+1<<": "<<val<<endl;
		}
		else if(cnt==0)
		{
			cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
		}
		else
		{
			cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
		}
	}
}