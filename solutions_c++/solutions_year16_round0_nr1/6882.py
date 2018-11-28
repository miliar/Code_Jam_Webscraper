#include<bits/stdc++.h>
#define ll long long int

using namespace std;
int main()
{
	
	freopen("A-large.in","r",stdin);
	freopen("out2.out","w",stdout);
	int t;
	cin>>t;
	int count=0;
	while(t--)
	{
		count++;
		ll n;
		cin>>n;
		if(n==0)
			cout<<"Case #"<<count<<": INSOMNIA\n";
		else
		{
			int visit[10];
			memset(visit,0,sizeof(visit));
			ll xx;
			for(ll i=1;;i++)
			{
				ll x=n*i;xx=n*i;
				int d;
				while(x!=0)
				{
					d=x%10;
					x=x/10;
					visit[d]=1;
				}
				int flag=1;
				for(int j=0;j<10;j++)
				{
					if(visit[j]==0)
					{
						flag=0;
						break;
					}
				}
					if(flag==1)
						break;
			}
				cout<<"Case #"<<count<<": "<<xx<<endl;
		}
	}
	return 0;
}
