#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <ctime>
#include <sstream>
#include <fstream>

using namespace std;

typedef long long int64;

#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define ROF(i,a,b) for(int i=(a);i>=(b);--i)
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define sz(a) ((int)(a).size())
#define ms(a,x)

const int N=5005;

int a[N],b[N],u[N],v[N],pre[N],f[N],g[N],use[N],path[N];
int hehe[N],fuck[N];

int main()
{
	#ifdef LOCAL_TEST
		freopen("a.in","r",stdin);
		freopen("a.out","w",stdout);
	#endif

	int task;
	cin>>task;
	for (int tt=1;tt<=task;++tt)
	{
		cout<<"Case #"<<tt<<": ";
		int n,m,p;
		cin>>n>>m>>p;
		for (int i=1;i<=m;++i)
		{
			use[i]=0;
			hehe[i]=0;
			cin>>a[i]>>b[i]>>u[i]>>v[i];
		}
		int cost=0;
		for (int i=0;i<p;++i)
		{
			cin>>path[i];
			use[path[i]]=1;
			cost+=u[path[i]];
		}
		for (int i=1;i<=n;++i) f[i]=1000000001;
		f[1]=0;
		for (int k=1;k<=n;++k)
		{
			for (int i=1;i<=m;++i)
			{
				int x=a[i],y=b[i],z;
				if (use[i]) z=u[i];
				else z=v[i];
				if (f[x]+z<f[y]) f[y]=f[x]+z;
			}
		}
		if (cost==f[2])
		{
			cout<<"Looks Good To Me"<<endl;
			continue;
		}
		cost=0;

		for (int i=0;i<p;++i)
		{
			cost+=u[path[i]];
			hehe[path[i]]=1;
			int cc=cost;
			int j=b[path[i]];


		for (int i=1;i<=n;++i) g[i]=1000000001;
		g[2]=0;
		for (int k=1;k<=n;++k)
		{
			bool ok=1;
			for (int i=1;i<=m;++i)
			{
				int x=b[i],y=a[i],z=u[i];
				if (use[i] && !hehe[i]) z=v[i];
				if (g[x]+z<g[y])
				{
					ok=0;
					g[y]=g[x]+z;
					pre[y]=i;
				}
			}
			if (ok) break;
		}



			for (int k=1;k<=m;++k) fuck[k]=0;
			for (int k=0;k<=i;++k) fuck[path[k]]=1;

			while (j!=2)
			{
				cc+=u[pre[j]];
				fuck[pre[j]]=1;
				j=b[pre[j]];
			}

			for (int i=1;i<=n;++i) f[i]=1000000001;
			f[1]=0;
			for (int k=1;k<=n;++k)
			{
				bool ok=1;
				for (int i=1;i<=m;++i)
				{
					int x=a[i],y=b[i],z;
					if (fuck[i]) z=u[i];
					else z=v[i];
					if (f[x]+z<f[y])
					{
						ok=0;
						f[y]=f[x]+z;
					}
				}
				if (ok) break;
			}
			if (cc!=f[2])
			{
				cout<<path[i]<<endl;
				break;
			}
		}
	}
	return 0;
}
