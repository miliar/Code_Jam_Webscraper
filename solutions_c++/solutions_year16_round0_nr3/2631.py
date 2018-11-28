/*input
1
16 50
*/
#include <bits/stdc++.h>
#include<stdio.h>
using namespace std;
#define pii pair<long long,long long>
#define F(i,a,b) for(ll i = (ll)(a); i <= (ll)(b); i++)
#define RF(i,a,b) for(ll i = (ll)(a); i >= (ll)(b); i--)
#define PI 3.14159265
#define ll long long
#define ff first
#define ss second
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define INF 1000000009
#define mod 1000000007
vector <string> v;
string convert(ll x)
{
	//cout<<x<<endl;
	string s;
	vector <char> v1;
	while(x>0)
	{
		ll d = x%2;
		//cout<<d<<endl;
		x = x/2;
		char c = (char)(d+48);
		v1.push_back(c);
		//cout<<c<<endl;
	}
	ll sz = v1.size();
	RF(i,sz-1,0)
	{
		s = s+v1[i];
	}
	return s;
}
bool isprime(ll num)
{
	for(ll i=3;i<=sqrt(num);i=i+2)
	{
		if(num%i==0)
			return 0;
	}
	return 1;
}
bool convertbase(string s,ll base)
{
	ll sz = s.length();
	ll t=0;
	ll num = 0;
	RF(i,sz-1,0)
	{
		if(s[i]=='1')
			num = num + ceil(pow(base,t));
		t++;
	}
	if(isprime(num))
		return 0;
	else
		return 1;	
}
void divisors(string s,ll base)
{
	ll sz = s.length();
	ll t=0;
	ll num = 0;
	RF(i,sz-1,0)
	{
		if(s[i]=='1')
			num = num + ceil(pow(base,t));
		t++;
	}
	//cout<<num<<endl;
	F(j,2,sqrt(num))
	{
		if(num%j==0)
		{
			cout<<j<<" ";
			break;
		}
	}
}
int main() 
{
	std::ios::sync_with_stdio(false);
	ll tc;
	cin>>tc;
	F(t,1,tc)
	{
		cout<<"Case #"<<t<<": "<<endl;
		ll n,j;
		cin>>n>>j;
		ll s = ceil(pow(2,n-1))+1;
		ll e = ceil(pow(2,n))-1;
		F(i,s,e)
		{
			ll num = i; // this is decimal representation of number
			if(num%2==0)
				continue;
			string s = convert(num);
			//cout<<s<<endl;
			bool f = 0;
			F(j,2,10)
			{
				if(!convertbase(s,j))
				{
					f = 1;
					break;
				}
			}
			if(!f)
				v.push_back(s);
		}
		ll sz = v.size();
		F(i,0,j-1)
		{
			string s = v[i];
			cout<<s<<" ";
			F(j,2,10)
				divisors(s,j);
			cout<<endl;
		}
	}
	return 0;
}