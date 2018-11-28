#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define vi vector<ll>
#define pi 3.14159265359
#define pb(n) push_back(n)
#define fir first
#define sec second
#define mp make_pair
#define sf scanf
#define pf printf
#define sz size()
#define foa(i,n) for(ll i=0;i<n;i++)
#define fod(i,n) for(ll i=n-1;i>=0;i--)
int main()
{
	int t;
	cin>>t;
	for (int i = 0; i < t; ++i)
	{
		ll n;
		cout<<"Case #"<<i+1<<": ";
		cin>>n;
		int a[10];
		ll sum=n,f,flag=0;
		memset(a,0,sizeof a);

		if(n==0)
		{
			cout<<"INSOMNIA\n";
			continue;
		}
		for(ll i=1;1;i++)
		{
			f=0;
			sum=n*i;
			ll temp = sum;
			while(temp)
			{
				a[temp%10]++;
				temp/=10;
			}
			for (int i = 0; i < 10; ++i)
			{
				if(a[i]==0)
					f=1;
			}
			if(f)
				continue;
			else
			{
				flag=1;
				cout<<sum<<endl;
				break;
			}

		}	
		if(flag==0)
		{
			cout<<"INSOMNIA\n";	
		}
	}
}