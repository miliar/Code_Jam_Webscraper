#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<string>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<ctime>
#include<vector>
#include<utility>
using namespace std;
#define INF (1<<30)
#define EPS 1e-6
#define PI acos(-1)
#define lowbit(x) ((x) & (-(x)))
#define IDX(l,r) ((l)+(r) | (l)!=(r))
#define ABS(x) ((x)>0?(x):-(x))
#define SET(a,b) memset(a,b,sizeof(a))
#define N 18
int fastget()
{
	char c; int ans=0; c=getchar();
	int sign=1;
	while (! (c>='0' && c<='9' || c=='-')) c=getchar();
	if(c=='-') sign=-1,c=getchar();
	while (c>='0' && c<='9')
	{
		ans=(ans<<3)+(ans<<1)+c-'0';
		c=getchar();
	}
	return ans*sign;
}
void fastput(int x)
{
	char s[12]; int a=0;
	if(x==0) puts("0");
	else
	{
		if(x<0) putchar('-'),x=-x;
		while (x) { s[a++]=x%10+'0'; x/=10; }
		for(a--;a>=0;a--) putchar(s[a]);
		putchar('\n');
	}
}
int vis[N];
int main()
{
	int tt=fastget();
	int ttt=0;
	while (tt--)
	{
		int r=fastget();
		SET(vis,0);
		for(int i=1;i<=4;++i)
		for(int j=1;j<=4;++j)
		{
			int x=fastget();
			if(i==r) vis[x]=1;
		}
		r=fastget();
		for(int i=1;i<=4;++i)
		for(int j=1;j<=4;++j)
		{
			int x=fastget();
			if(i==r && vis[x]==1) vis[x]=2;
		}
		int ans=0;
		for(int i=1;i<=16;++i)
			if(vis[i]==2)
			if(ans==0) ans=i;
			else ans=-1;
		printf("Case #%d: ",++ttt);
		if(ans>0) printf("%d\n",ans);
		else if(ans==0) printf("Volunteer cheated!\n");
		else printf("Bad magician!\n");
	}
	return 0;
}
