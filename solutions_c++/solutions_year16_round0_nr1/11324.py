#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define vi vector<int>
int main()
{
    ios::sync_with_stdio(false);
    int t,l=1;
	cin>>t;
	ll n;
	while(t--)
	{
		cin>>n;
		if(n==0)
		cout<<"Case #"<<l<<": INSOMNIA"<<endl;
		else
		{
		int flag=0;
		ll temp1=0;
		vi v;
		int vis[11];
		memset(vis,0,sizeof(vis));
		while(1)
		{
			temp1+=n;
			ll temp=temp1;
			while(temp>0)
			{
				int d=temp%10;
				if(vis[d]==0)
				{v.pb(d);vis[d]=1;}
				if(v.size()==10)
				{flag=1;break;}
				temp/=10;
			}
			if(flag==1)
			break;
		}
		cout<<"Case #"<<l<<": "<<temp1<<endl;
		}
		l++;

	}
return 0;
}
