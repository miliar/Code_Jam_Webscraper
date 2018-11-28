#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int n,j;

int c = 0;

void check(ll x)
{
	vector<ll> v;
	for (int i=2; i<=10; i++)
	{
		int mm = 3;
		
		if (i%2) mm=2;
		else if (i==2) mm=3;
		else if (i==4) mm=5; 
		else if (i==6) mm=7;
		else if (i==10) mm=11;
		
		ll y = 0;
		ll tt = x;
		ll t = 1;
		while (tt)
		{
			y+=(tt%2)*t;
			tt/=2;
			t*=i;			
			t%=mm;
		}
		
		if (y%mm) return; 
		
		v.push_back(mm);		
	}
	
	cerr<<"Case #"<<c<<' ' <<x<<" DONE\n";
	c++;
	vector<int> a;
	while (x)
		a.push_back(x%2),x/=2;
	reverse(a.begin(),a.end());
	
	for (int i:a) cout<<i;
	
	for (ll i:v) cout<<' '<<i;
	
	cout<<'\n';
}

int main()
{
	int t;
	cin>>t;
	for (int tt=1; tt<=t; tt++)
	{
		cout<<"Case #"<<tt<<":\n";
		cin>>n>>j;
		c = 0 ;
		
		for (ll i=(1ll<<(n-1))+1; c<j && i<(1ll<<n); i+=2)
			check(i);
	}
    return 0;
}

