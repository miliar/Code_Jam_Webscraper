
#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define f first
#define s second
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
	ll n,i,t,j,counter=1;
	cin>>t;
	while(t--)
	{
		cout<<"Case #"<<counter++<<": ";
		cin>>n;
		pair<ll,char> a[100];
		for(i=0;i<n;++i)
		{
			cin>>a[i].f;
			a[i].s=i+65;
		}
		sort(a,a+n);
		//for(i=0;i<n;++i)
		//	cout<<a[i].s<<" ";
		ll d=a[n-1].f-a[n-2].f;
		ll t1=d/2;
		ll r=d%2;
		for(j=0;j<t1;++j)
			cout<<((a[n-1].s))<<((a[n-1].s))<<" ";
		if(r==1)
			cout<<((a[n-1].s))<<" ";
		a[n-1].f=a[n-2].f;
		for(i=0;i<n-2;++i)
		{
			d=a[i].f/2;
			r=a[i].f%2;
			for(j=0;j<d;++j)
				cout<<((a[i].s))<<((a[i].s))<<" ";
			if(r==1)
				cout<<((a[i].s))<<" ";
		}
		for(i=0;i<a[n-2].f;++i)
			cout<<((a[n-2].s))<<((a[n-1].s))<<" ";
		cout<<endl;
	}
	return 0;
}
