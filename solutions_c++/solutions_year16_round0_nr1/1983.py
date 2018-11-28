#include <bits/stdc++.h>
using namespace std;
bool u[10];
bool check(int v)
{
	while(v>0)
	{
		u[v%10]=1;
		v/=10;
	}
	for(int i=0;i<10;i++) if(!u[i]) return 0;
	return 1;
}
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	int T,no=0;
	cin>>T;
	while(T--)
	{
		int n;
		cin>>n;
		//int mx=1;
		//while(mx<=n) mx*=10;
		memset(u,0,sizeof u);
		int ans=-1;
		if(n!=0)
			for(int i=1;/*i<=mx*/;i++)
				if(check(i*n))
					{ans=i;break;}
		cout<<"Case #"<<++no<<": ";
		if(ans==-1) cout<<"INSOMNIA\n";
		else cout<<ans*n<<'\n';
	}
}