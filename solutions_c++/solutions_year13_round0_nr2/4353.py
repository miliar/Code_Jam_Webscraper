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
#include <sstream>

using namespace std;

struct ar
{
	int x,y,z;
	ar (){}
	ar(int a,int b,int c)
	{
		x=a;y=b;z=c;
	}
	bool operator<(const ar &p) const
	{
		return z<p.z;
	}
};

vector<ar> a;
int f[1005],g[1005];

int main()
{
	#ifdef LOCAL_TEST
		freopen("d.in","r",stdin);
		freopen("d.out","w",stdout);
	#endif
	int task;
	scanf("%d ",&task);
	for (int tt=1;tt<=task;++tt)
	{
		printf("Case #%d: ",tt);
		a.clear();
		int n,m;
		scanf("%d%d",&n,&m);
		for (int i=0;i<n;++i) f[i]=1;
		for (int i=0;i<m;++i) g[i]=1;
		for (int i=0;i<n;++i)
			for (int j=0;j<m;++j)
			{
				int k;
				scanf("%d",&k);
				a.push_back(ar(i,j,k));
			}
		bool ok=1;
		sort(a.begin(),a.end());
		for (int h=100,ed=a.size()-1;h>0;--h)
		{
			int op=ed;
			while (op>=0 && a[op].z==h)
			{
				int x=a[op].x,y=a[op].y;
				if (f[x]==0 && g[y]==0) ok=0;
				--op;
			}
			for (int i=op+1;i<=ed;++i)
			{
				int x=a[i].x,y=a[i].y;
				f[x]=g[y]=0;
			}
			ed=op;
		}
		if (ok) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}
