#define _CRT_SECURE_NO_DEPRECATE

#pragma comment(linker,"/STACK:267386880")

#include <iostream>
#include <functional>
#include <ctime>
#include <cstdio>
#include <memory>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <utility>
#include <iterator>
#include <bitset>
#include <sstream>
#include <numeric>
#include <complex>

#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define pdd pair<double,double>
#define LL long long
#define ULL unsigned LL
#define VI vector<int>
#define X first
#define Y second
#define sz(_v) ((int)_v.size())
#define all(_v) (_v).begin(),(_v).end()
#define FOR(i,a,b) for (int i(a); i<=(b); ++i)
#define rep(i,a) FOR(i,1,a)
#define rept(i,a) FOR(i,0,(int)(a)-1)
#define x1 X1
#define y1 Y1
#define sqr(a) ((a)*(a))
#define C(a) memset((a),0,sizeof (a))
#define MS(a,x) memset((a),(x),sizeof (a))
#define INF 1000000000
#define PI 3.141592653589
#define eps 0.00000000001
#define MOD 1000002013
#define PRIME 1000003

using namespace std;

int n,m;
LL d[10005];

set<int> SET;
map<int,int> MAP;
map<int,int> revMAP;
vector<pair<pii, int> > IN;

void solve()
{
	scanf("%d%d",&n,&m);
	C(d);
	LL mb=0;
	SET.clear();
	MAP.clear();
	revMAP.clear();
	IN.clear();
	IN.reserve(m);
	rept(i,m)
	{
		int a,b,k;
		scanf("%d%d%d",&a,&b,&k);
		IN.pb(mp(mp(a,b),k));
		SET.insert(a-1);
		SET.insert(b-2);
		SET.insert(b-1);
		LL toAdd=0;
		if ((b-a)%2==0)
			toAdd=(b-a)/2*1ll*(2ll*n-b+a+1);
		else
			toAdd=(2ll*n-b+a+1)/2*1ll*(b-a);
		toAdd%=MOD;
		mb=(mb+(1ll*k*toAdd)%MOD)%MOD;
	}
	int count=0;
	for (set<int>::iterator it=SET.begin(); it!=SET.end(); ++it,++count)
	{
		MAP[*it]=count;
		revMAP[count]=*it;
	}
	rept(i,sz(IN))
	{
		int a,b,k;
		a=IN[i].X.X;
		b=IN[i].X.Y;
		k=IN[i].Y;
		int start=a-1;
		int end=b-2;
		start=MAP[start];
		end=MAP[end];
		FOR(i,start,end)
			d[i]+=k;
	}
	--n;
	LL ans=0;
	while (1)
	{
		int start(0);
		while (d[start]==0 && start<count)
			++start;
		int end=start;
		while (d[end]!=0 && end<count)
			++end;
		--end;
		if (start>end)
			break;
		if (start>revMAP.size())
		{
			int b=0;
		}
		int realStart=revMAP[start];
		int realEnd=revMAP[end];
		LL mn=INF*1ll*INF;
		FOR(i,start,end)
			mn=min(d[i],mn);
		FOR(i,start,end)
			d[i]-=mn;

		LL toAdd=0;
		if ((realEnd-realStart+1)%2==0)
			toAdd=(realEnd-realStart+1)/2*1ll*(2ll*(n+1)-realEnd+realStart);
		else
			toAdd=(2ll*(n+1)-realEnd+realStart)/2*1ll*(realEnd-realStart+1);
		toAdd%=MOD;
		ans=(ans+((1ll*mn)%MOD*toAdd)%MOD)%MOD;
	}
	mb=(mb-ans+MOD)%MOD;
	printf("%lld\n",mb);
}

int main()
{
#ifndef ONLINE_JUDGE
	{
		freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
	}
#endif
	int t;
	scanf("%d",&t);
	rept(tst,t)
	{
		printf("Case #%d: ",tst+1);
		solve();
	}
	return 0;
}