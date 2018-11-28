#include<bits/stdc++.h>
#define ll long long
using namespace std;
ll arr[11];

ll ipow(ll base,ll power)
{
	if(power==0)
	return 1;
	ll temp=ipow(base,power/2);
	if(power&1)
	return base*temp*temp;
	return temp*temp;
}

ll isprime(ll n)
{
	ll temp=4;
	for(ll i=2;temp<=n;i++)
	{
		if((n%i)==0)
		return i;
		temp=(i+1)*(i+1);
	}
	return 0;
}

int main()
{
//	freopen("in.txt","r",stdin);
//	freopen("out.txt","w",stdout);
	
	ll test;
	cin>>test;
	for(ll t=1;t<=test;t++)
	{
		ll n,j;
		cin>>n>>j;
		cout<<"Case #"<<t<<": "<<endl;
		
		ll count=pow(2,n-1)+pow(2,0);
		ll loop=pow(2,n-2);
		
	//	cout<<count<<" "<<loop<<endl;
		
		ll ans=0;
		for(ll i=0;i<loop;i++)
		{
			bool flag=true;
			for(ll j=2;j<=10;j++)
			{
				ll z=count|(i*2);
			//	cout<<z<<endl;
				ll ind=0;
				ll sum=0;
				while(z)
				{
					if(z&1)
					sum=sum+ipow(j,ind);
					ind++;
					z>>=1;
				}
			//	cout<<sum<<endl;
				arr[j]=isprime(sum);
				if(!arr[j])
				{
					flag=false;
					break;
				}
			}
			if(flag)
			{
				ans++;
				ll z=count|(i*2);
				for(ll j=15;j>=0;j--)
				{
					if((z&(1<<j)))
					cout<<1;
					else
					cout<<0;
				}
				cout<<" ";
				
				for(ll j=2;j<=10;j++)
				cout<<arr[j]<<" ";
				cout<<endl;
			}
			if(ans==50)
			break;
		}
	}

	return 0;
}
