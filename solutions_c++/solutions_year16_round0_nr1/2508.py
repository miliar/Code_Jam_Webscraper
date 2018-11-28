#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int a[10];

bool gg(ll x)
{
    ll y = x;
	bool f = 1;

	a[x%10]=1;
	while (x)
	{
		a[x%10]=1;
		x/=10;
	}

	for (int i=0; i<10; i++)
		f = f && a[i];

	if (f) cout<<y;
	return f;
}

int main()
{
	int t;
	cin>>t;
	for (int tt=1; tt<=t; tt++)
	{
		cout<<"Case #"<<tt<<": ";
		ll n;
		cin>>n;

		for (int j=0; j<10; j++)
			a[j] = 0;

		bool f=0;
		for (int i=1; !f && i<=1e7; i++)
			f |= gg(1ll*n*i);

		if (!f) cout<<"INSOMNIA";
		cout<<'\n';
	}
    return 0;
}

