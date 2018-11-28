#include <bits/stdc++.h>
using namespace std;
#define ll long long 
ll pow (ll x,ll y)
{
	if(y<=1)return x;
	
	ll c=pow(x,y/2);
	if(y&1)
	return c*x;
	else return c;
}
int main ()
{
	int t,p=1;
	cin>>t;
	while(t--)
	{
		int k,c,s;
		cin>>k>>c>>s;
		cout<<"Case #"<<p<<": ";
		ll u=pow(k,c-1);
		ll z=1;
		for(int i=0;i<s;i++)
		{
			cout<<z<<" ";
			z+=u;
		}
		p++;
		cout<<"\n";
	}
}
