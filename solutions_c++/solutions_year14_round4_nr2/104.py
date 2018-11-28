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
	vector<int> e;
	int n; scanf("%d",&n);
	rep(i,1,n)
	{
		int x; scanf("%d",&x);
		e.push_back(x);
	}
	
	int sum=0;
	rep(i,1,n)
	{
		int minv=2000000000, minvi=0;
		rep(k,0,n-i) if (e[k]<minv) minv=e[k], minvi=k;
		sum+=min(minvi,n-i-minvi);
		e.erase(e.begin()+minvi);
	}
	printf("%d\n",sum);
}

int main()
{
	ios::sync_with_stdio(true);
	#ifndef ONLINE_JUDGE
		freopen("B.in","r",stdin);
	#endif
	int tcase; scanf("%d",&tcase);
	rep(nowcase,1,tcase) 
	{
		printf("Case #%d: ",nowcase);
		lemon();
	}
	return 0;
}

