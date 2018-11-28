#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
freopen("in.in","r",stdin);
freopen("out.out","w",stdout);
long long t;
long long n;
cin>>t;
for(long long i=1;i<=t;i++)
	{
	set<long long> num;
	cin>>n;
	if(n==0)
		{
		cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		continue;
		}
long long temp;
long long itt=1;	
long long ans;
	while(num.size()!=10)
	{
		temp=n*itt;
		ans=temp;
		while(temp!=0)
		{
		num.insert(temp%10);
		temp=temp/10;
		}
itt++;
	}
	cout<<"Case #"<<i<<": "<<ans<<endl;
	}
return 0;
}
