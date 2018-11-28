#include <iostream>
#include <stdio.h>
#include <math.h>
#include <cmath>

using namespace std;

#define maxn 10000+10
char s[maxn];
short vis[maxn],a[maxn],b[maxn];
int T[4][4]={ 1, 2, 3, 4
			 ,2,-1, 4,-3
			 ,3,-4,-1, 2
			 ,4, 3,-2,-1};

int idx(char c)
{
	if (c=='i') return 2;
	if (c=='j') return 3;
	if (c=='k') return 4;
}

int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);
	int t,cas=0,n,x;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&n,&x);
		scanf("%s",s+1);
		for (int i=1;i<=n;i++)
		{
			for (int j=1;j<x;j++) s[j*n+i]=s[i];
		}
		for (int i=1;i<=n*x;i++) a[i]=idx(s[i]);
		s[n*x+1]=0;
		vis[1]=a[1];
		//printf("%d ",vis[i]);
		for (int i=2;i<=n*x;i++)
		{
			int x=(vis[i-1]);
			int y=(a[i]);
			int u=abs(x);
			int v=abs(y);
			vis[i]=T[u-1][v-1];
			if ((x<0 && y>0)||(x>0 && y<0)) vis[i]=0-vis[i];
		}
		if (vis[n*x]!=-1)
		{
			printf("Case #%d: NO\n",++cas);
			continue;
		}
		bool cut=0,flag=0;
		b[n*x]=a[n*x];
		for (int i=n*x-1;i>=1;--i)
		{
			int y=(b[i+1]);
			int x=(a[i]);
			int u=abs(x);
			int v=abs(y);
			b[i]=T[u-1][v-1];
			if ((x<0 && y>0)||(x>0 && y<0)) b[i]=0-b[i];
		}
		for (int i=1;i<n*x;i++)
		{
			if (cut && b[i+1]==4){
				flag=1; break;
			}
			if (vis[i]==2) cut=1;
		}

		if (flag) printf("Case #%d: YES\n",++cas);
		else printf("Case #%d: NO\n",++cas);
	}
	return 0;
}
