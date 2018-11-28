#include<bits/stdc++.h>
using namespace std;
#define ll long 
#define lim 100005
#define mk make_pair
#define pll pair<ll,ll>
#define pb push_back
#define X first
#define Y second
#define MOD 1000000007
#define ios ios_base::sync_with_stdio(0)

string s;

int main(void)
{
	ios;
	ll a,len,tem,ct,n,b,m,c,d,e,t,f;
	freopen("input2.txt","r",stdin);
	freopen("output2.txt","w",stdout);
	cin>>t;	
	
	for(d=1;d<=t;d++)
	{
		cin>>s;
		len=s.size();
		tem=-1;
		ct=0;
		tem=-1;
		for(a=0;a<len;a++)
			if(s[a]=='-')
			tem=a;
		ct=1;
		if(tem==-1)
		cout<<"Case #"<<d<<": "<<"0\n";
		else
		{
			for(a=0;a<tem;a++)
			{
				if(s[a]!=s[a+1])
				ct++;
			}
			cout<<"Case #"<<d<<": "<<ct<<"\n";
		}
	}
	return 0;
}
