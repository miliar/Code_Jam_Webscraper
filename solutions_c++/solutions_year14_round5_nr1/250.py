#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<queue>
#include<stack>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<string>
#include<cstring>
#include<cstdio>
#include<ctime>
#include<climits>
#include<complex>
#include<cassert>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define sz(x) (int)((x).size())
#define all(x) x.begin(),x.end()
#define clr(x) memset((x),0,sizeof(x))
#define cdp(x) memset((x),-1,sizeof(x))
#define rep(i,n) for (i=0;i<n;i++)
#define Rep(i,a,b) for (i=a;i<=b;i++)
#define ff(i,x) for (i=start[x];i!=-1;i=a[i].next)
#define foreach(e,x) for(__typeof(x.begin()) e=x.begin();e!=x.end();++e)
using namespace std;
const double eps=1e-8;
const double pi=acos(-1.0);
int dblcmp(double d){if (fabs(d)<eps)return 0;return d>eps?1:-1;}
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector<pii> vpi;
int n,p,q,r,s;
int a[1111111];
ll sum[1111111];
int main()
{
	freopen("C://competition//R3//A-large (2).in","r",stdin);
	freopen("C://competition//R3//A.out","w",stdout);
	int i,j,k,cas,cc=0;
	scanf("%d",&cas);
	while (cas--)
	{
		scanf("%d%d%d%d%d",&n,&p,&q,&r,&s);
		for (i=0;i<n;i++)
		{
			ll o=i;
			o*=p;
			o+=q;
			o%=r;
			a[i+1]= ((int)o + s) ;
		}
		clr(sum);
		for (i=1;i<=n;i++)sum[i]=sum[i-1]+a[i];
		ll low=0,high=sum[n],ans,mid;
		while (low<=high)
		{
			mid=(low+high)>>1;
			int p1=-1,p2=-1,p3;
			for (i=1;i<=n;i++)if (sum[i]>mid)break;
			p1=i-1;
			if (p1==0)
			{
				low=mid+1;
				continue;
			}
			//[1,p1] first part
			for (i=p1+1;i<=n;i++)if (sum[i]-sum[p1]>mid)break;
			p2=i-1;
			//[p1+1,p2] first part
			if (p2==-1)
			{
				low=mid+1;
				continue;
			}
			if (sum[n]-sum[p2]>mid)
			{
				low=mid+1;
				continue;
			}
			high=mid-1;
			ans=mid;
		}
		/*
		ll c=0;
		for (i=1;i<=n;i++)
		{
			for (j=i;j<=n;j++)
			{
				ll x=sum[j]-sum[i-1];
				ll y=sum[i-1];
				ll z=sum[n]-sum[j];
				ll t=min(sum[n]-x,sum[n]-y);
				t=min(t,sum[n]-z);
				c=max(c,t);
			}
		}
		*/
		ans=sum[n]-ans;
		printf("Case #%d: %.10lf\n",++cc,ans*1.0/sum[n]);
	}
	return 0;
}