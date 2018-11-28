#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

const int MAXN = 2001;
const int MAXM = 2000011;
const int MAXK = 201;
const int INF = 1000000001;
const double eps = 1e-5;

int sum[MAXN];
int val[MAXN];
int len[MAXN];
int a[MAXN];
int g[MAXN][MAXN];
char ch[MAXN][MAXK];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,cas,m,n,i,j,k,t,u,ans,total,temp,res;
	scanf("%d",&T);
	for(cas=1;cas<=T;cas++)
	{
		scanf("%d%d",&m,&n);
		for(i=0;i<m;i++)
			scanf("%s",ch[i]);
		for(i=0;i<m;i++)
			len[i]=strlen(ch[i]);
		for(i=0;i<m;i++)
			for(j=0;j<m;j++)
			{
				for(k=0;k<len[i]&&k<len[j]&&ch[i][k]==ch[j][k];k++);
				g[i][j]=k;
			}
		for(t=1,i=0;i<m;i++)
			t=t*n;
		ans=-1; total=0;
		for(i=0;i<t;i++)
		{
			temp=i;
			for(j=0;j<m;j++)
			{
				a[j]=temp%n;
				temp=temp/n;
			}
			for(k=0;k<n;k++)
				sum[k]=0;
			for(j=0;j<m;j++)
				sum[a[j]]++;
			for(k=0;k<n;k++)
				if(sum[k]==0)
					break;
			if(k<n) continue;
			res=0;
			for(k=0;k<n;k++)
			{
				for(j=0;j<m;j++)
					val[j]=len[j];
				for(j=0;j<m;j++)
					if(a[j]==k)
					{
						res=res+val[j];
						for(u=j+1;u<m;u++)
							val[u]=min(val[u],len[u]-g[j][u]);
					}
				res++;
			}
			if(res>ans)
			{
				ans=res;
				total=1;
			}
			else
			if(res==ans)
			{
				total++;
			}
		}
		printf("Case #%d: %d %d\n",cas,ans,total);
	}
	return 0;
}