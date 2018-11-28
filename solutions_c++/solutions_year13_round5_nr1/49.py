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

int64 a[1005];

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
		int64 m;
		cin>>m;
		int n;
		cin>>n;
		for (int i=0;i<37;++i) a[i]=0;
		for (int i=0;i<n;++i)	cin>>a[i];
		sort(a,a+37);
		double ans=0;
		for (int end=1;end<=37;++end)
		{
			int64 l=0,r=(int64)1e16;
			while (l<r)
			{
				int64 mid=(l+r+1)/2;
				int64 use=0;
				for (int i=0;i<end;++i)
					use+=mid-a[i];
				for (int i=end;i<37;++i)
					if (a[i]<=mid)
						use+=mid-a[i]+1;
				if (use<=m) l=mid;
				else r=mid-1;
			}
			if (l<a[end-1]) continue;
			double t=0;
			for (int i=end;i<37;++i)
				if (a[i]<=l)
					t-=l-a[i]+1;
			for (int i=0;i<end;++i)
			{
				int64 dif=l-a[i];
				t+=1.*dif*36/end;
				t-=dif;
			}
		//	cerr<<end<<' '<<t<<' '<<l<<endl;
			if (t>ans) ans=t;
		}
		printf("%.10f\n",ans);
	}
	return 0;
}
