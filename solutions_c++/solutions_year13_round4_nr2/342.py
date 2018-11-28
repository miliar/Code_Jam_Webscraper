#include<set>
#include<map>
#include<cmath>
#include<queue>
#include<string>
#include<cstdio>
#include<vector>
#include<cassert>
#include<cstring>
#include<cstdlib>
#include<utility>
#include<iostream>
#include<algorithm>
#include<functional>
#define REP(x,y,z) for(int x=y;x<=z;x++)
#define FORD(x,y,z) for(int x=y;x>=z;x--)
#define MSET(x,y) memset(x,y,sizeof(x))
#define FOR(x,y) for(__typeof(y.begin()) x=y.begin();x!=y.end();x++)
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define SZ size()
#define M 
using namespace std;
typedef long long LL;
int t,n;
LL m,p;
bool must(LL x)
{
	int round=0;
	LL l=1, r=m;
	LL cnt = x;

	while(cnt && round<n)
	{
		l = (l+r)/2 + 1;
		cnt = min(r-l, (cnt-1)/2);
		round++;
		//printf("%I64d %I64d\n",l,r);
	}
	while(round < n)
	{
		r = (l+r)/2;
		round++;
		//printf("%I64d %I64d\n",l,r);
	}
	return l<=p;
}
bool possible(LL x)
{
	int round=0;
	LL l=1, r=m;
	LL cnt = m-1-x;

	while(cnt && round<n)
	{
		r = (l+r)/2;
		cnt = min(r-l, (cnt-1)/2);
		round++;
		//printf("%I64d %I64d\n",l,r);
	}
	while(round < n)
	{
		l = (l+r)/2 + 1;
		round++;
		//printf("%I64d %I64d\n",l,r);
	}
	return l<=p;
}
int main()
{
	LL l,r,mid;
	
	scanf("%d",&t);
	REP(tt,1,t)
	{
		scanf("%d %I64d",&n,&p);
		m=1ll<<n;
	
		//printf("%d\n",must(1));while(1);
		
		printf("Case #%d: ",tt);
		l=0, r=m-1;
		while(l<r-1)
		{
			mid=(l+r)/2;
			if(must(mid))l=mid;
			else r=mid-1;
		}
		if(l==r-1 && must(r))l++;
		printf("%I64d ",l);
		

		l=0, r=m-1;
		while(l<r-1)
		{
			mid=(l+r)/2;
			if(possible(mid))l=mid;
			else r=mid-1;
		}
		if(l==r-1 && possible(r))l++;
		printf("%I64d\n",l);
	}
	return 0;
}

