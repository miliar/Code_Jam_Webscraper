#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<string>
#include<iomanip>
#include<vector>
#include<set>
#include<map>
#include<queue>

using namespace std;
typedef long long LL;
typedef unsigned long long ULL;

#define rep(i,k,n) for(int i=(k);i<=(n);i++)
#define rep0(i,n) for(int i=0;i<(n);i++)
#define red(i,k,n) for(int i=(k);i>=(n);i--)
#define sqr(x) ((x)*(x))
#define clr(x,y) memset((x),(y),sizeof(x))
#define pb push_back
#define mod 1000000007

char s[10000];
LL po[12][35];
int ans[600];
LL aa[600][12];

LL check(LL x)
{
	for(LL i=2;i*i<=x;i++)
	{
		if(x%i==0)return i;
	}
	return -1;
}

int main()
{
	rep(i,2,10)
	{
		po[i][0]=1;
		rep(j,1,16)po[i][j]=po[i][j-1]*i;
	}
	int T,m,n;
	scanf("%d",&T);
	rep(ii,1,T)
	{
		scanf("%d%d",&n,&m);
		int tot=1<<n;
		LL tmp;
		for(int i=(1<<n-1)+1,cnt=1;cnt<=m && i<tot;i+=2)
		{
			int p=check(i);
			if(p==-1)continue;
			bool ok=1;
			aa[cnt][2]=p;
			for(int j=3;j<=10;j++)
			{
				tmp=0;
				for(int k=0;k<n;k++)if(i&(1<<k))tmp+=po[j][k];
				aa[cnt][j]=check(tmp);
				if(aa[cnt][j]==-1)
				{
					ok=0;
					break;
				}
			}
			if(ok)ans[cnt++]=i;
		}
		printf("Case #%d:\n",ii);
		rep(i,1,m)
		{
			for(int j=n-1;j>=0;j--)if(ans[i]&(1<<j))putchar('1');else putchar('0');
			for(int j=2;j<=10;j++)printf(" %I64d",aa[i][j]);
			puts("");
		}
	}
	
	return 0;
}
