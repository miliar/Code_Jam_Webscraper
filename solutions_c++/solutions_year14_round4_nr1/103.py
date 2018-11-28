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

void lemon()
{
	int n,s; scanf("%d%d",&n,&s);
	multiset<int> ss;
	rep(i,1,n) 
	{
		int x; scanf("%d",&x);
		ss.insert(x);
	}
	
	int all=0;
	while (!ss.empty())
	{
		all++;
		int z=*(--ss.end()); ss.erase(--ss.end());
		multiset<int>::iterator it=ss.upper_bound(s-z);
		if (it==ss.begin()) continue;
		it--; ss.erase(it);
	}
	printf("%d\n",all);
}

int main()
{
	ios::sync_with_stdio(true);
	#ifndef ONLINE_JUDGE
		freopen("A.in","r",stdin);
	#endif
	int tcase; scanf("%d",&tcase);
	rep(nowcase,1,tcase) 
	{
		printf("Case #%d: ",nowcase);
		lemon();
	}
	return 0;
}

