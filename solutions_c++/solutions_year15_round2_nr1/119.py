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
LL po[100],po2[100],n,t[100];
int tl;
LL solve(LL n)
{
	//printf("%lld\n",n);
	if (n<=10) return n;
	if (n%10==0) return solve(n-1)+1;
	LL _n=n;
	tl=0;
	while (_n) t[++tl]=_n%10,_n/=10;
	LL res=0;
	int flag=0;
	rep(i,1,tl)
		if (i==1 || i==tl)
		{
			if (i==tl && t[i]>1) flag=1;
			res+=min(po[i-1],po[tl-i])*(t[i]-1);
		}
		else
		{
			if (po[i-1]>po[tl-i] && t[i]>0) flag=1;
			res+=min(po[i-1],po[tl-i])*t[i];
		}
	return res+solve(po2[tl-1])+2+flag;
}
void work(int ti)
{
	scanf("%lld",&n);
	po[0]=1;
	rep(i,1,16) po[i]=po[i-1]*10;
	po2[0]=0;
	rep(i,1,16) po2[i]=po2[i-1]*10+9;
	printf("Case #%d: %lld\n",ti,solve(n));
}
int main()
{
	int cs,ti=0;
	scanf("%d",&cs);
	while (cs--) work(++ti);
}
