#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;


int main() {
	
	ll tc;cin>>tc;
	
	for(ll t=1;t<=tc;t++)
	{
		
		
		ll n;cin>>n;
		
ll cnt[26]={0};
		pair<ll,char>pp[n];	
		
		for(ll i=0;i<n;i++)
			{
				cin>>pp[i].first;
				pp[i].second = char('A'+i);
				
			}
		
		cout<<"Case #"<<t<<": ";
		sort(pp,pp+n);
		
		while(pp[n-1].first>pp[n-2].first)
		{
			cout<<pp[n-1].second<<" ";
			pp[n-1].first-=1;
		}
		
		for(ll i=0;i<n-2;i++)
		{
			while(pp[i].first>0)
			{
				cout<<pp[i].second<<" ";
				pp[i].first-=1;
			}
		}
		
		while(pp[n-1].first>0)
		{
			cout<<pp[n-2].second<<pp[n-1].second<<" ";
			pp[n-1].first-=1;
		}
		cout<<"\n";
			
	}
	
	
	return 0;
	
}