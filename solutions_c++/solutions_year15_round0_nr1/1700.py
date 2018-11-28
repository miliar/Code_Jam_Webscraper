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
char s[10000];
int n;
void work(int ti)
{
	scanf("%d%s",&n,s);
	int ans=0,cur=0;
	rep(i,0,n)
		if (cur>=i) cur+=s[i]-'0';
		else ans+=i-cur,cur=i+s[i]-'0';
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
