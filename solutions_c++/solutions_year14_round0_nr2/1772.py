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
int main()
{
	fop;
	int T,cas=0;
	scanf("%d",&T);
	while(T--)
	{
		double c,f,x;
		scanf("%lf%lf%lf",&c,&f,&x);
		double nowres=10000000000000.0;
		double nowtime=0;
		for(int i=0;;i++)
		{
			double nowcps=2+i*f;
			nowtime+=x/nowcps;
			if(nowtime>nowres)
				break;
			nowres=nowtime;
			nowtime-=x/nowcps;
			nowtime+=c/(2+(i)*f);
		}
		printf("Case #%d: %.7f\n",++cas,nowres);
	}
}