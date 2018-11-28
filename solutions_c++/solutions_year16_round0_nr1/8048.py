#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	ll t;
	cin>>t;
	ll count=0;
	while(t--)
	{	
		count++;
		ll n;
		cin>>n;
		if(n==0)
			cout<<"Case #"<<count<<": INSOMNIA\n";
		else 
		{
			ll i=1;
			set<ll> s;
			while(n!=0 && s.size()<10){
				ll temp=i*n;
				while(temp!=0)
				{
					s.insert(temp%10);
					temp=temp/10;
				}
				i++;
			}
			cout<<"Case #"<<count<<": "<<(i-1)*n<<endl;
		}
	}
}
