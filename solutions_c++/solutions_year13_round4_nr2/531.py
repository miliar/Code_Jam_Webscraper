#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
typedef long long ll;
ll n,p,l,r,mid;

bool alligator(ll x)
{
	ll i,lose=0,rank=0;
	for(i=x;i;i>>=1) i--,lose++;
	for(i=1;i<=lose;i++) rank|=1ll<<n-i;
	return rank<p;
}

bool crocodile(ll x)
{
	ll i,win=0,rank=(1ll<<n)-1;
	for(i=(1ll<<n)-x-1;i;i>>=1) i--,win++;
	for(i=1;i<=win;i++) rank^=1ll<<n-i;
	return rank<p;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t,T;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		cin>>n>>p;
		l=0,r=(1ll<<n)-1;
		while(l<r)
		{
			mid=(l+r+1)>>1;
			if(alligator(mid)) l=mid; else r=mid-1;
		}
		cout<<"Case #"<<t<<": "<<l<<" ";
		l=0,r=(1ll<<n)-1;
		while(l<r)
		{
			mid=(l+r+1)>>1;
			if(crocodile(mid)) l=mid; else r=mid-1;
		}
		cout<<r<<endl;
	}
}
