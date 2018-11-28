#include <iostream>
using namespace std;
typedef long long int ll;

int main() {
	ll tc;cin>>tc;
	
	for(ll ii=0;ii<tc;ii++)
		{
		ll n;
		cin>>n;
		cout<<"Case #"<<(ii+1)<<": ";
		if(n==0)
			cout<<"INSOMNIA\n";
		else
		{
			ll a[10]={0},count=0,cnt=1;
			
			while(count<10)		
			{
				ll m=n*cnt;
				while(m!=0)
				{
					if(a[m%10]==0)
					{a[m%10]=1;count+=1;}
					m/=10;
				}
				cnt+=1;
			}
			
			cout<<n*(cnt-1)<<"\n";
		}
	}
	return 0;
}