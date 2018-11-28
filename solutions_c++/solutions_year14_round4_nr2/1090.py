#include<cstdio>
#include<algorithm>
#include<iostream>
using namespace std;
int n,m;
int d[10010];

int solve_()
{
	int ans=0;
	int ma=0;
	for(int i=1;i<n;i++)
		if (d[i]>d[ma])
			ma=i;
	//	ans=
	return ans;
}

int best;
bool v[1010];
int id[1010];
int ma;

bool check()
{
	//printf("%d %d %d\n",d[0],d[1],d[2]);
	for(int i=0;i<n;i++)
		if (id[i]==ma||i==n-1)
			break;
		else
			if (d[id[i]]>d[id[i+1]])
				return false;
	for(int i=n-1;i>=0;i--)
		if (id[i]==ma||i==0)
			break;
		else
			if (d[id[i-1]]<d[id[i]])
				return false;
	return true;
}

void dfs(int x,int cur)
{
	if (x==n){
		if (check())
			if (cur<best)best=cur;
	}
	else
		for(int i=0;i<n;i++)
			if (!v[i])
				{
					v[i]=true;
					id[x]=i;
					int s=0;
					for(int j=0;j<x;j++)
						s+=(id[j]>i);
					dfs(x+1,cur+s);
					v[i]=false;
				}
}

int solve()
{
	best=n*n;
	memset(v,0,sizeof(v));
	ma=0;
	for(int i=1;i<n;i++)
		if (d[i]>d[ma])
			ma=i;
	dfs(0,0);
	return best;
	
}



int main()
{
	freopen("bs.in","r",stdin);
	int tt;
	scanf("%d",&tt);
	for(int ii=1;ii<=tt;ii++)
		{
			scanf("%d",&n);
			for(int i=0;i<n;i++)
				scanf("%d",d+i);
			int ans=solve();
			printf("Case #%d: %d\n",ii,ans);
		}
	return 0;
}


