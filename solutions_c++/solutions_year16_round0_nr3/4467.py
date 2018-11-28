#include <bits/stdc++.h>
#define ll long long int

using namespace std;

ll po(ll a, int b)
{
	ll re=1;
	while(b)
	{
		if(b%2)
			re=(ll)re*a;
		a=(ll)a*a;
		b/=2;
	}
	return re;
}

vector<ll> v[510];
int j;

int prime(ll x)
{
	ll sq=sqrt(x);
	for(ll i=2;i<=sq;i++)
		if(x%i == 0)
		{
			v[j].push_back(i);
			return 0;
		}
	v[j].clear();
	return 1;
}

string ans[510];

int main()
{
	ios_base::sync_with_stdio(false);
	int t,n,nj,count,len;
	ll p,var,temp;
	string s,b;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>n>>j;
		nj=j;
		p=po(2LL,n-2);
		if(n-2 == 0)
			p=0;
		cout<<"Case #"<<i<<":\n";
		if(!j)
			continue;
		for(ll k=0;k<p;k++)
		{
			for(ll l=2;l<=10;l++)
			{
				var=po(l,n-1)+1;
				temp=k;
				count=1;
				while(temp)
				{
					if(temp%2)
						var+=po(l,count);
					temp/=2;
					count++;
				}
				if(prime(var))
					break;
			}
			if(v[j].size())
			{
				s="1";
				b="";
				temp=k;
				len=n-2;
				while(len--)
				{
					if(temp%2)
						b+="1";
					else
						b+="0";
					temp/=2;
				}
				for(int l=n-3;l>=0;l--)
					s+=b[l];
				s+="1";
				ans[j]=s;
				j--;
			}
			if(!j)
				break;
		}
		for(int k=nj;k>=1;k--)
		{
			cout<<ans[k]<<" ";
			for(int l=0;l<9;l++)
				cout<<v[k][l]<<" ";
			cout<<"\n";
		}
	}
	return 0;
}