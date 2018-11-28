#include<bits/stdc++.h>
#define ll long long

using namespace std;

int solve(int c, int w)
{
	if (c!=w){
		 if (c%w == 0)return ( c/w + w -1 );
		 else return c/w + w;
	}
	return w;
}

int main()
{
	int t;
	int r,c,w;
	cin>>t;
	int ans;
	for(int i=1;i<=t;++i)
	{
		cin>>r>>c>>w;
		ans = solve(c,w);
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}
