#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
//	freopen("in.txt","r",stdin);
//	freopen("out.txt","w",stdout);
	
	int test;
	cin>>test;
	for(int t=1;t<=test;t++)
	{
		ll n;
		cin>>n;
		if(n)
		{
			bool flag[10]={false};
			ll count=0;
			ll r=0;
		
			while(count!=10)
			{
				r=r+n;
				ll m=r;
				while(m)
				{
					if(!flag[m%10])
					{
						count++;flag[m%10]=true;
					}
					m=m/10;
				}
			}
			
			cout<<"Case #"<<t<<": "<<r<<endl;
		}
		else
		cout<<"Case #"<<t<<": "<<"INSOMNIA"<<endl;
	}
	return 0;
}
