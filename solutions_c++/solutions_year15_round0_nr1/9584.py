#include <bits/stdc++.h>

using namespace std;

#define ll long long int


int main()
{
	ll t;
	cin>>t;
	ll count=0;
	while(t--)
	{
		count++;
		ll max;
		string inp;
		cin>>max>>inp;
		ll ar[max+1];
		for(ll i=0;i<=max;i++)
		{
			ar[i] = inp[i]-'0';
		}
		ll sumTillNow = 0;
		ll ans=0;
		for(ll i=0;i<=max;i++)
		{
			if(sumTillNow<i)
			{
				ans = ans + (i-sumTillNow);
				sumTillNow = i;
			}
			// cout<<ans<<endl;
			sumTillNow = sumTillNow + ar[i];
		}
		cout<<"Case #"<<count<<": "<<ans<<endl;
	}
}