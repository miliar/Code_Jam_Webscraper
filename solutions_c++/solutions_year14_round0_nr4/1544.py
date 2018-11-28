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
#define fop   freopen("in.txt","r",stdin);//freopen("out.txt","w",stdout);
#define myprogram By_135678942570
#define clrcpy(x,siz,y)  for(int xx=0;xx<siz;xx++)  x[xx]=y[xx];
#define pb push_back
using namespace std;
double A[1111];
double B[1111];
int main()
{
	fop;
	int T,cas=0;
	scanf("%d",&T);
	while(T--)
	{
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%lf",&A[i]);
		for(int i=0;i<n;i++)
			scanf("%lf",&B[i]);
		sort(A,A+n);
		sort(B,B+n);
		for(int i=-1;i<n;i++)
		{
			int flag=1;
			for(int j=i+1;j<n;j++)
				if(A[j]<B[j-i-1])
				{
					flag=0;
					break;
				}
			if(flag)
			{ 
				printf("Case #%d: %d ",++cas,n-i-1);
				break;
			}
		}
		int r=0;
		for(int i=0;i<n;i++)
		{
			while(r<n&&B[r]<A[i])
				r++;
			if(r==n)
			{
				printf("%d\n",n-i);
				goto loop;
			}
			r++;
		}
		puts("0");
		loop:;
	}
}