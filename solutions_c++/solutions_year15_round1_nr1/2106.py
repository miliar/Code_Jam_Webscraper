#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

int main()
{	freopen("input.txt", "r", stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		ll n,y=0,z=0,ans=0;
		cin>>n;
		ll a[n];
		for(ll j=0;j<n;j++)
		{
		 cin>>a[j];
		 if(j>0)
		 {
		 	if(a[j]<a[j-1])
		 	{
			 y+=a[j-1]-a[j];
			 if(z<a[j-1]-a[j])
			 z=a[j-1]-a[j];
			}
		 }
		}
		for(ll j=0;j<n-1;j++)
		{
			ans+=min(z,a[j]);
		}
		cout<<"Case #"<<i<<": "<<y<<" "<<ans<<endl;
	}
	return 0;
}
