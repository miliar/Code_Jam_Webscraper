#include <iostream>
#include <set>
using namespace std;
#define ll long long
int main(int argc, char const *argv[])
{
	ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		ll n;
		cin>>n;
		if(n==0)
			cout<<"Case #"<<i<<": INSOMNIA\n";
		else
		{
			set<int> s;
			ll ans=0;
			while(s.size()<10)
			{
				ans+=n;
				ll temp=ans;
				while(temp)
				{
					s.insert(temp%10);
					temp/=10;
				}
			}
			cout<<"Case #"<<i<<": "<<ans<<"\n";
		}
	}
	return 0;
}