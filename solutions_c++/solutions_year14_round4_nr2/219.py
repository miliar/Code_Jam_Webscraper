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
int n,a[11111],m;
inline int gao(vi x)
{
	int i,j,k=0;
	int n=sz(x);
	for (i=0;i<n;i++)
	{
		for (j=0;j<n-1;j++)
		{
			if (x[j]>x[j+1])
			{
				k++;
				swap(x[j],x[j+1]);
			}
		}
	}
	return k;
}
inline int gao1(vi x)
{
	int i,j,k=0;
	int n=sz(x);
	for (i=0;i<n;i++)
	{
		for (j=0;j<n-1;j++)
		{
			if (x[j]<x[j+1])
			{
				k++;
				swap(x[j],x[j+1]);
			}
		}
	}
	return k;
}
int b[11111];
int main()
{
	freopen("C://competition//R2//B-large (2).in","r",stdin);
	freopen("C://competition//R2//B.out","w",stdout);
	int i,j,k,cas,cc=0;
	scanf("%d",&cas);
	while (cas--)
	{
		scanf("%d",&n);
		for (i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
			b[i]=a[i];
		}
		sort(a,a+n);
		int ans=0;
		int x=0,y=n-1;
		for (i=0;i<n;i++)
		{
			int p;
			for (j=0;j<n;j++)if (a[i]==b[j])
			{
				p=j;break;
			}
			int l=abs(p-x),r=abs(p-y);
			if (l<=r)
			{
				if (p>=x)
				{
					for (j=p;j>x;j--)swap(b[j],b[j-1]);
				}
				else 
				{
					for (j=p;j<x;j++)swap(b[j],b[j+1]);
				}
				x++;
				ans+=l;
			}
			else 
			{
				if (p>=y)
				{
					for (j=p;j>y;j--)swap(b[j],b[j-1]);
				}
				else 
				{
					for (j=p;j<y;j++)swap(b[j],b[j+1]);
				}
				y--;
				ans+=r;
			}
		}
			
			
		printf("Case #%d: %d\n",++cc,ans);
	}
	return 0;
}
				
			