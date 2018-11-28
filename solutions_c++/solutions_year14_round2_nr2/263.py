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
long long dp[44][2][2][2];
int A[44]={0};
int B[44]={0};
int K[44]={0};
long long solve(int pos,int up1,int up2,int upk)
{
	long long res=0;
	if(pos==-1)
		return 1;
	if(dp[pos][up1][up2][upk]!=-1)
		return dp[pos][up1][up2][upk];
	int uppA=0;
	if(up1==0||(up1==1&&A[pos]==1))
		uppA=1;
	int uppB=0;
	if(up2==0||(up2==1&&B[pos]==1))
		uppB=1;
	for(int i=0;i<=uppA;i++)
		for(int j=0;j<=uppB;j++)
		{
			if(i==1&&j==1&&upk==1&&K[pos]==0)
				continue;
			int newup1=(up1&&A[pos]==i);
			int newup2=(up2&&B[pos]==j);
			int newupk=(upk&&K[pos]==(i&j));
			long long tmp=solve(pos-1,newup1,newup2,newupk);
			res+=tmp;
		}
	return dp[pos][up1][up2][upk]=res;
}
int main()
{
	fop;
	int T,cas=0;
	scanf("%d",&T);
	while(T--)
	{
		clr(A);
		clr(B);
		clr(K);
		clr_1(dp);
		long long a,b,k;
		scanf("%lld%lld%lld",&a,&b,&k);
		a--,b--,k--;
		for(int i=0;i<40;i++)
			A[i]=a%2,a>>=1;
		for(int i=0;i<40;i++)
			B[i]=b%2,b>>=1;
		for(int i=0;i<40;i++)
			K[i]=k%2,k>>=1;
		printf("Case #%d: %lld\n",++cas,solve(40,1,1,1));
		// printf("%lld\n",solve(1,0,1,1));
	}
}