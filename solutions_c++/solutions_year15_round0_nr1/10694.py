#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	long long int t;
	cin>>t;
	char str[100005];
	long long int n;
	for(long long int j=1;j<=t;j++)
	{
		cin>>n>>str;
		long long int ans=0;
		long long int sum=(int)str[0]-48;
		for(long long int i=1;i<=n;i++)
		{
			if(sum<i)
			{
				//cout<<i<<"here1"<<endl;
				ans=ans+(i-sum);
				sum=sum+((int)str[i]-48+i-sum);
				//cout<<ans<<endl;
			}
			else
			{
				//cout<<i<<"here2"<<endl;
				sum=sum+(int)str[i]-48;
				//cout<<sum<<endl;
			}
		}
		cout<<"Case #"<<j<<": "<<ans<<endl;
	}
	return 0;
}