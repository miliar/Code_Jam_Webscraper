#include <set>
#include <cmath>
#include <stack>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <numeric>
#include <vector>
#include <ctime>
#include <queue>
#include <list>
#include <map>
#define pi acos(-1.0)
#define INF 0x3f3f3f3f
#define clr(x)  memset(x,0,sizeof(x));
#define clrto(x,siz,y)  for(int xx=0;xx<=siz;xx++)  x[xx]=y;
#define clrset(x,siz)  for(int xx=0;xx<=siz;xx++)  x[xx]=xx;
#define clr_1(x) memset(x,-1,sizeof(x));
#define clrmax(x) memset(x,0x3f,sizeof(x));
#define clrvec(x,siz) for(int xx=0;xx<=siz;xx++)  x[xx].clear();
#define fop2   freopen(".in","r",stdin); //freopen(".out","w",stdout);
#define fop   freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
#define myprogram By_135678942570
#define clrcpy(x,siz,y)  for(int xx=0;xx<siz;xx++)  x[xx]=y[xx];
#define pb push_back
using namespace std;
long long num[1001111];
long long sum[1001111];
int main()
{
	fop;
	int T,cas=0;
	scanf("%d",&T);
	while(T--)
	{
		clr(sum);
		long long N,p,q,r,s;
		scanf("%lld%lld%lld%lld%lld",&N,&p,&q,&r,&s);
		for(int i=1;i<=N;i++)
		{
			num[i]=((i-1)*p+q)%r+s;
			sum[i]=sum[i-1]+num[i];
			// printf("%lld ",num[i]);
		}
		// puts("");
		long long res=0x3f3f3f3f3f3f3f3fll;
		for(int i=1;i<=N;i++)
		{
			long long sum1=sum[i-1];
			int l=i+1,r=N+1;
			while(l<r-1)
			{
				int m=l+r>>1;
				if(sum[m-1]-sum1<=sum[N]-sum[m-1])
					l=m;
				else r=m;
			}
			long long sum2=sum[l-1]-sum1;
			long long sum3=sum[N]-sum[l-1];
			res=min(res,max(sum1,max(sum2,sum3)));
			sum2=sum[l]-sum1;
			sum3=sum[N]-sum[l];
			res=min(res,max(sum1,max(sum2,sum3)));
		}
		printf("Case #%d: %.10f\n",++cas,(sum[N]-res+0.0)/sum[N]);
	}
}