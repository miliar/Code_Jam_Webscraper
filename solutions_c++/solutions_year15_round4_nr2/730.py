#include<iostream>
#include<fstream>
#include<iomanip>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iomanip>
#include<algorithm>
#include<list>
#include<map>
#include<set>
#include<queue>
#include<deque>
#include<vector>
#include<functional>
#include<string>

#define INF 1000000007
#define pb push_back
#define mp make_pair
#define ll long long
#define rep(i,k) for(int i=G.start[k];i!=INF;i=G.next[i])

using namespace std;

double r[105],c[105];

int main()
{
freopen("t.in","r",stdin);
freopen("t.out","w",stdout);
	ios::sync_with_stdio(false);
	
	int T;
    cin>>T;
	for(int cas=1;cas<=T;cas++)
	{
		bool fg=0;
		int n;
		double V,X,ans;
		cin>>n>>V>>X;
		for(int i=0;i<n;i++)
			cin>>r[i]>>c[i];
		if(n==1)
		{
			if(c[0]!=X)fg=1;
			else ans=V/r[0];
		}
		if(n==2)
		{
			if(c[0]<X&&c[1]<X)fg=1;
			else if(c[0]>X&&c[1]>X)fg=1;
			else
			{
				if(c[0]==c[1])
				{
					double r0=r[0]+r[1];
					if(c[0]!=X)fg=1;
					else ans=V/r0;
				}
				else
				{
					double t1=V*(X-c[1])/(c[0]-c[1])/r[0];
					double t2=V*(X-c[0])/(c[1]-c[0])/r[1];
					ans=max(t1,t2);
				}
			}
		}
		
		cout<<setiosflags(ios::fixed)<<setprecision(9);
		if(!fg)cout<<"Case #"<<cas<<": "<<ans<<endl;
		else cout<<"Case #"<<cas<<": "<<"IMPOSSIBLE"<<endl;
	}
	
	return 0;
}
