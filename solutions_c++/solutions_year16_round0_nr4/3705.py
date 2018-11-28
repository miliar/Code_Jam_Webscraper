#include <bits/stdc++.h>
using namespace std;
#define ll long long
ll power(ll a,ll n)
{
	if(a==1 || n==0)return 1;
	if(n==1)return a;
	ll t=power(a,n/2);
	return t*t*(n%2==0?1:a);
}
int main() 
{
	int test=1,test0;
	cin>>test0;
	while(test0--)
	{
		int k,c,s;
		cin>>k>>c>>s;
		if(k==1){cout<<"Case #"<<test++<<": "<<1<<endl;continue;}
		if(c==1 && s<k){cout<<"Case #"<<test++<<": IMPOSSIBLE"<<endl;continue;}
		if(c==1 && s>=k)
		{
			cout<<"Case #"<<test++<<": ";
			for(int i=1;i<=k;i++)cout<<i<<" ";cout<<endl;continue;
		}
		if(k==2){cout<<"Case #"<<test++<<": "<<2<<endl;continue;}
		if(k==3){cout<<"Case #"<<test++<<": 2 3"<<endl;continue;}
		cout<<"Case #"<<test++<<": ";
		for(int i=2;i<=k-2;i++)cout<<i<<" ";
		cout<<power(k,c)-k<<endl;
	}
	return 0;
}