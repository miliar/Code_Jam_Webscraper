#include "bits/stdc++.h"
using namespace std;

int main()
{
	std::ios::sync_with_stdio(false);
	#ifndef ONLINE_JUDGE
		freopen("D-small-attempt0.in","r",stdin);
		freopen("D.txt","w",stdout);
	#endif
	int t;
	cin>>t;
	unsigned long long int k,c,s,ans,add;
	for(int te=1;te<=t;te++)
	{
		cin>>k>>c>>s;
		ans=1;
		for(int mul=1;mul<c;mul++)
			ans*=k;
		add=ans;
		cout<<"Case #"<<te<<": ";
		for(int i=1;i<=k;i++)
		{
			cout<<ans<<" ";
			ans+=add;
		}
		cout<<endl;
	}	
}