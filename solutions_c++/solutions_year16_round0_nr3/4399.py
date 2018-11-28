#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll t,ans,n,jj,m,c=0;
vector<ll> vec;

ll isprime(ll x)
{
	for(ll i=2;i*i<=x;i++)
	{
		if(x%i==0)
			return i;
	}
	return 0;
}

ll change(ll a,ll b)
{
	ll q=1,rem,ret=0;
	while(a)
	{
		rem=a%10;
		ret+=(rem*q);
		a/=10;
		q*=b;
	}
	return ret;
}

ll chn(ll a)
{
	ll ans=0,rem,q=1;
	while(a)
	{
		rem=a%2;
		ans+=(rem*q);
		q*=10;
		a/=2;
	}
	return ans;
}

int main()
{
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	cin>>t;
	while(t--)
	{
		c++;
		ans=0;
		cin>>n>>jj;	
		n--;
		m=(1<<(n+1));
		cout<<"Case #"<<c<<": "<<endl;
		for(ll i=(1<<n)+1;i<m;i+=2)
		{
			ll num=chn(i);
			vec.clear();
			ll flg=1;
			
			for(ll j=2;j<=10;j++)
			{
				vec.push_back(isprime(change(num,j)));
				if(vec.back()==0)
				{
					flg=0;
					break;
				}
			}
			
			if(flg)
			{
				ans++;
				cout<<num<<" ";
				
				for(ll j=0;j<vec.size();j++)
					cout<<vec[j]<<" ";
				cout<<endl;
			}
			
			if(ans>=jj)
				break;
		}
	}
	return 0;
}
