
#include<bits/stdc++.h>
typedef long long ll;
using namespace std;


int main()
{
	
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	ll t;
	cin>>t;
	for(ll i=0;i<t;i++)
	{
		ll n;
		cin>>n;
		ll nc=n;
		ll a[10];
		for(int i=0;i<10;i++)
		a[i]=0;
		
		if(n==0)
		{
			cout<<"Case #"<<(i+1)<<": INSOMNIA"<<endl;
			continue;
		}
		
		
		
		int trcount=0;
		ll k=1;
		int flag=0;
		
		while(trcount==0)
		{
			
			
			while((nc!=0))
			{
				a[(nc%10)]++;
				nc/=10;
				
				
			}
			
			k++;
			nc= k*n;
			
			for(int i=0;i<10;i++)
			{ 
				flag=0;
				if(a[i]==0)
				{
					trcount=0;
					flag=1;
					break;
				}
				
			}
			
			if(flag==0)
			{
				trcount=1;
			}
			
			
		}
		
		
		ll ans= (k-1)*n;
		
		cout<<"Case #"<<(i+1)<<": "<<ans<<endl;
		
	}
	
	return 0;
}
	

