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
typedef __int64 ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector<pii> vpi;
string itos(ll x)
{
	string s="";
	if (x==0)return "0";
	if (x<0){s+="-";x=-x;}
	while (x){s+='0'+x%10;x/=10;}
	if (s[0]=='-'){reverse(s.begin()+1,s.end());}
	else reverse(all(s));
	return s;
}
bool ispar(ll x)
{
	string s1=itos(x);
	string s2=s1;
	reverse(all(s2));
	return s1==s2;
}
vl p;
int smalleq(ll x)
{
	int c=upper_bound(all(p),x)-p.begin();
	//if (p[c]>x)c--;
	return c+1;
}
	
int main()
{
	freopen("C:\\Users\\daizhy\\Downloads\\C-large-1.in","r",stdin);
	freopen("C:\\2013������\\gcj\\oc.txt","w",stdout);
	int i,j,k,cas,cc=0;	
	for (i=1;i<=10000000;i++)if (ispar(i))
	{
		ll u=i;
		u*=u;
		if (ispar(u))p.pb(u);
	}
	scanf("%d",&cas);
	while (cas--)
	{
		ll l,r;
		scanf("%I64d%I64d",&l,&r);
		printf("Case #%d: %d\n",++cc,smalleq(r)-smalleq(l-1));
	}
	return 0;
}

