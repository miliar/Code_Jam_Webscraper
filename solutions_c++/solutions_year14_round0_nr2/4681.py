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
double c,f,x;
int main()
{
	int tt=fastget();
	int ttt=0;
	while (tt--)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		double ans=x/2.0;
		printf("Case #%d: ",++ttt);
		if(x-c<EPS)
		{
			printf("%.7lf\n",ans);
			continue;
		}
		double v=2;
		double sum=0;
		for(int i=1;;++i)
		{
			double tim=c/v;
			sum+=tim;
			v+=f;
			if(ans-sum-x/v>EPS) ans=sum+x/v;
			else break;
		}
		printf("%.7lf\n",ans);
	}
	return 0;
}
