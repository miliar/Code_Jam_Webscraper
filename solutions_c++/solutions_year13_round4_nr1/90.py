#include <cstdio>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <sstream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#define pb push_back
#define mp make_pair
#define ST begin()
#define ED end()
#define XX first
#define YY second
#define elif else if 
#define foreach(i,x) for (__typeof((x).ST) i=(x).ST;i!=(x).ED;++i) 
using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vci;
typedef vector<string> vcs;
typedef pair<int,int> PII;

const int N = 2005;
const int mo = 1000002013;

int n, m;
int a[N], b[N], c[N];
map<int, ll> f;
pair<int, ll> q[N];

ll cal(int x)
{
	return 1LL*(n+n-x+1)*x/2%mo;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	int task;
	scanf("%d", &task);
	for (int _i=1;_i<=task;++_i)
	{
		scanf("%d%d", &n, &m);
		f.clear();
		ll aa=0;
		for (int i=1;i<=m;++i)
		{
			scanf("%d%d%d", &a[i], &b[i], &c[i]);
			aa+=cal(b[i]-a[i])*c[i]%mo;
			f[a[i]]=(f[a[i]]+c[i])%mo;
			f[b[i]]=(f[b[i]]-c[i])%mo;
		}
		ll ans=0;
		int ed=0;
		foreach(it,f)
		{
			int i=it->XX;
			ll w=it->YY;
			if (w>0)
			{
				q[++ed]=mp(i,w);
			}
			if (w<0)
			{
				ll x=-w;
				while (x>0)
				{
					ll y=min(x,q[ed].YY);
					ans=(cal(i-q[ed].XX)*y+ans)%mo;
					x-=y;
					q[ed].YY-=y;
					if (!q[ed].YY)
						--ed;
				}
			}
		}
		//printf("%I64d %I64d\n", aa, ans);
		aa=((aa-ans)%mo+mo)%mo;
		cout<<"Case #"<<_i<<": "<<aa<<endl;
	}

	return 0;
}
