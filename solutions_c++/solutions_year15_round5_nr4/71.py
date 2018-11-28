#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstring>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

#define SIZE(x) (int((x).size()))
#define rep(i,l,r) for (int i=(l); i<=(r); i++)
#define repd(i,r,l) for (int i=(r); i>=(l); i--)
#define rept(i,c) for (typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)

#ifndef ONLINE_JUDGE
#define debug(x) { cerr<<#x<<" = "<<(x)<<endl; }
#else
#define debug(x) {}
#endif

map<int,int> s;
int ans[30];
int lis[1100000], v[1000000], t[1000000];

void lemon()
{
	int n, x=0; scanf("%d",&n);
	rep(i,1,n) scanf("%d",&v[i]);
	rep(i,1,n) scanf("%d",&t[i]), x+=t[i];
	s.clear();
	rep(i,1,n) s[v[i]]+=t[i];
	s[0]--;
	int m=0;
	while (x!=1) x/=2, m++;
	lis[1]=0;
	rep(i,1,m)
	{
		while (s.begin()->second==0) s.erase(s.begin());
		int val=s.begin()->first;
		ans[i]=val;
		rep(k,1,(1<<(i-1))) 
		{
			lis[k+(1<<(i-1))]=lis[k]+val;
			s[lis[k]+val]--;
		}
	}
	rep(i,1,m) 
	{
		printf("%d",ans[i]);
		if (i!=m) printf(" "); else printf("\n");
	}
}

int main()
{
	ios::sync_with_stdio(true);
	#ifndef ONLINE_JUDGE
		freopen("D.in","r",stdin);
	#endif
	int tcase; scanf("%d",&tcase);
	rep(nowcase,1,tcase)
	{
		printf("Case #%d: ",nowcase);
		lemon();
	}
	return 0;
}

