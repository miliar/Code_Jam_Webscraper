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
#define LD long double
#define pb push_back
#define mp make_pair
#define Pi M_PI
#define clr(a) memset(a,0,sizeof(a));
using namespace std;
template<class T> inline T min(T &a,T &b) {return a<b?a:b;}
template<class T> inline T max(T &a,T &b) {return a>b?a:b;}
const int u[4]={0,0,1,-1};
const int v[4]={1,-1,0,0};
vector<int> all;
int n,m,K;
void work(int ti)
{
	scanf("%d%d%d",&n,&m,&K);
	int cnt=0,ans=0,sum=0;
	rep(i,1,n) rep(j,1,m)
	{
		if ((i+j)%2==0) cnt++;
	}
	all.clear();
	rep(i,1,n) rep(j,1,m)
		if ((i+j)%2==1)
	{
		int num=0;
		rep(k,0,3)
			if (i+u[k]>=1 && i+u[k]<=n && j+v[k]>=1 && j+v[k]<=m)
				num++;
		all.pb(num);
	}
	sort(all.begin(),all.end());
	for (int i=0;i<all.size();i++)
		if (cnt<K) cnt++,sum+=all[i];
	ans=sum;
	sum=0;cnt=0;
	rep(i,1,n) rep(j,1,m)
	{
		if ((i+j)%2==1) cnt++;
	}
	all.clear();
	rep(i,1,n) rep(j,1,m)
		if ((i+j)%2==0)
	{
		int num=0;
		rep(k,0,3)
			if (i+u[k]>=1 && i+u[k]<=n && j+v[k]>=1 && j+v[k]<=m)
				num++;
		all.pb(num);
	}
	sort(all.begin(),all.end());
	for (int i=0;i<all.size();i++)
		if (cnt<K) cnt++,sum+=all[i];
	ans=min(ans,sum);
	printf("Case #%d: %d\n",ti,ans);
}
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("me.out","w",stdout);
	int cs;
	scanf("%d",&cs);
	rep(_,1,cs) work(_);
}
