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
const char*iip="C:\\Users\\daizhy\\Downloads\\B-large (8).in"; 
const char*oop="C:\\2013¸öÈËÈü\\gcj\\r2\\bout.txt";
int n;
ll p;
bool c1(ll x,ll lessthan,ll now,int v)//worst
{
	if (v==n)
	{
		return now<=p;
	}
	if (!lessthan)
	{
		return c1(x,lessthan,now*2LL+0,v+1);
	}
	return c1(x,(lessthan-1)/2,now*2LL+1,v+1);
}
bool c2(ll x,ll lessthan,ll now,int v)//best
{
	if (v==n)
	{
		//if (x==6)cout<<"now="<<now<<endl;
		return now<=p;
	}
	if (!lessthan)
	{
		return c2(x,lessthan,now*2LL+0,v+1);
	}
	ll l=lessthan;
	ll b=(1LL<<(n-v))-1-l;
	if (!b)return c2(x,l/2,now*2LL+1,v+1);
	b--;
	return c2(x,(l+1)/2,now*2LL+0,v+1);
}
int main()
{
	freopen(iip,"r",stdin);
	freopen(oop,"w",stdout);
	int i,j,k,cas,cc=0;
	cin>>cas;
	while (cas--)
	{
		cin>>n>>p;
		p--;
		ll low=0,high=(1LL<<n)-1,ans=-1,mid;
		//for (ll i=low;i<=high;i++)cout<<c1(i,i,0,0)<<endl;
		while (low<=high)
		{
			mid=(low+high)/2LL;
			//cout<<mid<<" "<<c1(mid,mid,0,0)<<endl;
			if (c1(mid,mid,0LL,0))
			{
				low=mid+1;
				ans=mid;
			}
			else 
			{
				high=mid-1;
			}
		}
		cout<<"Case #"<<++cc<<": "<<ans;
		low=0;high=(1LL<<n)-1;ans=-1;
		while (low<=high)
		{
			mid=(low+high)/2LL;
			//cout<<mid<<" "<<c1(mid,mid,0,0)<<endl;
			if (c2(mid,mid,0LL,0))
			{
				low=mid+1;
				ans=mid;
			}
			else 
			{
				high=mid-1;
			}
		}
		cout<<" "<<ans<<endl;
	}
	return 0;
}
