#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int t;
	cin>>t;
	for(long long int t1=0;t1<t;t1++)
	{
		long long int smax;
		cin>>smax;
		string s;
		cin>>s;
		long long int a[smax+1];
		for(long long int i=0;i<=smax;i++)
		{
			a[i]=s[i]-'0';
		}
		long long int b[smax+1];
		for(long long int i=0;i<=smax;i++)
		{
			b[i]=0;
		}
		for(long long int i=1;i<=smax;i++)
		{
			b[i]+=(b[i-1]+a[i-1]);
		}
		long long int count=0;
		for(long long int i=1;i<=smax;i++)
		{
			if(i>(b[i]+count))
			{
				count+=(i-b[i]-count);
			}
		}
		cout<<"Case #"<<t1+1<<": "<<count<<endl;
	}
}
