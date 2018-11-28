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
		int maz[102]={0};
		int n;
		scanf("%d",&n);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				int d;
				scanf("%d",&d);
				if(i==n-1)
					maz[d]++;
			}
		scanf("%d",&n);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				int d;
				scanf("%d",&d);
				if(i==n-1)
					maz[d]++;
			}
		int flag=-1;
		for(int i=0;i<=100;i++)
		{
			if(maz[i]==2)
			{
				if(flag==-1)
					flag=i;
				else flag=-2;
			}
		}
		printf("Case #%d: ",++cas);
		if(flag==-1)
			puts("Volunteer cheated!");
		else if(flag==-2)
			puts("Bad magician!");
		else printf("%d\n",flag);
	}
}