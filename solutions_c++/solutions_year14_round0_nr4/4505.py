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
#define EPS 1e-8
#define PI acos(-1)
#define lowbit(x) ((x) & (-(x)))
#define IDX(l,r) ((l)+(r) | (l)!=(r))
#define ABS(x) ((x)>0?(x):-(x))
#define SET(a,b) memset(a,b,sizeof(a))
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
#define N 1010
double a[N],b[N];
int n;
bool cmp(const double &a,const double &b)
{
	return b-a>EPS;
}
int main()
{
	int tt=fastget();
	int ttt=0;
	while (tt--)
	{
		n=fastget();
		for(int i=0;i<n;++i)
			scanf("%lf",&a[i]);
		for(int i=0;i<n;++i)
			scanf("%lf",&b[i]);
		sort(a,a+n,cmp);
		sort(b,b+n,cmp);
		/*
		for(int i=0;i<n;++i)
			printf("%.3lf ",a[i]);
		printf("\n");
		for(int i=0;i<n;++i)
			printf("%.3lf ",b[i]);
		printf("\n");
		*/
		printf("Case #%d: ",++ttt);
		int ans=0;
		for(int i=0,j=0,k=n-1;i<n && j<=k;++i)
		{
			if(a[i]-b[j]<EPS) --k;
			else ++j,++ans;
		}
		printf("%d ",ans);
		ans=n;
		for(int i=0,j=0;i<n && j<n;++i,++j)
		{
			if(a[i]-b[j]<EPS) --ans;
			else
			{
				while(j<n && b[j]-a[i]<EPS) ++j;
				if(j<n) --ans;
			}
		}
		printf("%d\n",ans);
	}
	return 0;
}
