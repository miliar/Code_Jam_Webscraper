#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#define rep(i,a,b) for (int i=a;i<=b;i++)
#define drep(i,a,b) for (int i=a;i>=b;i--)
#define INF int(1e8)
#define LL long long
#define D double
#define LD long double
#define pb push_back
#define mp make_pair
#define Pi M_PI
using namespace std;
template<class T> inline T min(T &a,T &b) {return a<b?a:b;}
template<class T> inline T max(T &a,T &b) {return a>b?a:b;}
int n,a[3000],b[3000];
void work(int ti)
{
	int ans=(int)1e9;
	scanf("%d",&n);
	rep(i,1,n) scanf("%d",&b[i]);
	rep(i,1,2000)
	{
		int cnt=0;
		rep(j,1,n) a[j]=b[j];
		rep(j,1,n)
			while (a[j]>i) cnt++,a[j]-=i;
		ans=min(ans,cnt+i);
	}
	printf("Case #%d: %d\n",ti,ans);
}
int main()
{
	freopen("large.in","r",stdin);
	freopen("me.out","w",stdout);
	int cs,ti=0;
	scanf("%d",&cs);
	while (cs--) work(++ti);
}
