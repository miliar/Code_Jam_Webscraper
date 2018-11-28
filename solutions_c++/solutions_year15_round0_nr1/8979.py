#include<iostream>
using namespace::std;

#define ll long long int


int main()
{
	ll i,j,k,t,s;

	cin>>t;

	char a[10000];

	for(j=1;j<=t;j++)
	{
		cin>>s;

		cin.ignore();

		cin>>a;

		ll count=0;
		ll sum=int(a[0]-48);
		for(i=1;i<=s;i++)
		{
			if(i-sum> 0)
			{	count = count + i-sum;
				sum=int(a[i]-48)+i;
			}
			else
			{
				sum=sum+int(a[i]-48);
			}

		}
		

		cout<<"Case #"<<j<<": "<<count<<"\n";

	}
}