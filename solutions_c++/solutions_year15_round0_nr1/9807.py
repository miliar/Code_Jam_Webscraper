#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,n;
	cin>>t;
	for(int j=0;j<t;j++)
	{
		cin>>n;
		int cnt=0,req=0;
		char arr[1000];
		cin>>arr;
		for(int i=0;i<=n;i++)
		{
			if(arr[i]=='0')
				continue;		
			if(cnt>=i)
			{
				cnt+=(arr[i]-48);
			}
			else
			{
				req+=i-cnt;
				cnt=cnt+req+(arr[i]-48);
			}
		}
		cout<<"Case #"<<j+1<<": "<<req<<endl;
		
	}
}
