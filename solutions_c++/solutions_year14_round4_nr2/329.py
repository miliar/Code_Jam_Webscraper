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
int num[1011];
map<int,int>pos;
int main()
{
	int T,cas=0;
	fop;
	scanf("%d",&T);
	while(T--)
	{
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%d",&num[i]);
			pos[num[i]]=i;
		}
		int num2[1011];
		for(int i=0;i<n;i++)
			num2[i]=num[i];
		sort(num2,num2+n);
		int siz=n;
		int res=0;
		for(int i=0;i<n;i++)
		{
			int now=num2[i];
			int nowpos;
			for(int j=0;j<siz;j++)
				if(num[j]==now)
				{
					nowpos=j;
					break;
				}
			int l=nowpos;
			int r=siz-nowpos-1;
			res+=min(l,r);
			for(int i=nowpos;i<siz-1;i++)
				swap(num[i],num[i+1]);
			siz--;
		}
		printf("Case #%d: %d\n",++cas,res);
	}
}