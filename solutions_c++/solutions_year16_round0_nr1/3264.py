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

bool vis[11];

void gao(int x)
{
	while(x)
	{
		vis[x%10]=1;
		x/=10;
	}
	vis[10]=1;
	rep(i,0,9)if(!vis[i]){vis[10]=0;break;}
}

int main()
{
	int T,n;
	scanf("%d",&T);
	rep(ii,1,T)
	{
		scanf("%d",&n);
		printf("Case #%d: ",ii);
		if(n==0)puts("INSOMNIA");
		else
		{
			clr(vis,0);
			int m=n;
			gao(m);
			while(!vis[10])gao(m+=n);
			printf("%d\n",m);
		}
	}
	
	return 0;
}
