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

struct ar
{
	ar(){}
	long long x,y;
};

const int N=10005;
const int64 mo=1000002013;

ar a[N],b[N];
int64 x[N],y[N],z[N];

bool cmp(ar a,ar b)
{
	if (a.x!=b.x) return a.x<b.x;
	return a.y>b.y;
}

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
		int64 n,m;
		cin>>n>>m;
		int64 ans=0;
		for (int i=0;i<m;++i)
		{
			cin>>x[i]>>y[i]>>z[i];
			int64 l=y[i]-x[i]-1;
			int64 tmp=(n+n-l)*(l+1)/2;
			tmp%=mo;
			(tmp*=z[i])%=mo;
			(ans+=tmp)%=mo;
			a[i*2].x=x[i];
			a[i*2].y=z[i];
			a[i*2+1].x=y[i];
			a[i*2+1].y=-z[i];
		}
		sort(a,a+m*2,cmp);
		for (int64 i=0,k=0,ed=0;i<m*2;++i)
		{
			int64 l=a[i].x-k-1;
			for (int j=0;j<ed;++j)
			{
				int64 tmp=(b[j].x+b[j].x-l)*(l+1)/2;
				tmp%=mo;
				(tmp*=b[j].y)%=mo;
				(ans-=tmp)%=mo;
				b[j].x-=l+1;
			}
			k=a[i].x;
			if (a[i].y>0)
			{
				b[ed].x=n;
				b[ed].y=a[i].y;
				++ed;
			}
			if (a[i].y<0)
			{
				int64 t=-a[i].y;
				sort(b,b+ed,cmp);
				while (t>0)
				{
					long long tt=min(t,b[ed-1].y);
					b[ed-1].y-=tt;
					t-=tt;
					if (b[ed-1].y==0) --ed;
				}
			}
		}
		(ans+=mo)%=mo;
		cout<<ans<<endl;
	}
	return 0;
}
