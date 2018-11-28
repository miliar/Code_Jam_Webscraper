#include<stdio.h>
#include<algorithm>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<stdlib.h>
#include<string.h>
#include<time.h>
using namespace std;
//wahaha wahahaha

int n, m;
char a[10][12];
int b[2000];
int d[256];
int go(int x)
{
	int i, j, k;
	int res = 1;
	string c[10];
	j=0;
	for(i=0;i<n;i++)
	{
		if(x&(1<<i))
		{
			c[j] = a[i];
			j++;
		}
	}
	sort(c,c+j);
	if(j>0)
	{
		res += c[0].length();
		for(i=1;i<j;i++)
		{
			for(k=0;k<c[i-1].length() && k<c[i].length(); k++)
			{
				if(c[i-1][k] != c[i][k])
					break;
			}
			res += (c[i].length() - k);
		}
	}
	return res;
}
int mark;
void dfs(int dep, int si, int x,int s)
{
	if(dep == m)
	{
		if(mark == (1<<n)-1)
			b[s]++;
	}
	else if(si == n)
	{
		if(x==0)return;
		dfs(dep+1,0,0,s + d[x]);
	}
	else
	{
		dfs(dep,si+1,x,s);
		if((mark & (1<<si)) == 0)
		{
			mark |= (1<<si);
			dfs(dep,si+1,x|(1<<si),s);
			mark -= (1<<si);
		}
	}
}
int main()
{
	freopen("D-small-attempt1.in","rt",stdin);
	freopen("D-small-attempt1.out","wt",stdout);
	int t;
	int tv;
	scanf("%d",&t);
	for(tv=1;tv<=t;tv++)
	{
		scanf("%d %d",&n,&m);
		int i, j, k, l;
		for(i=0;i<n;i++)
			scanf("%s",a[i]);
		for(i=0;i<2000;i++)
			b[i] = 0;
		for(i=0;i<256;i++)
			d[i] = go(i);
		mark = 0;
		dfs(0,0, 0,0);
		for(i=1999;i>=0;i--)
			if(b[i])
				break;
		printf("Case #%d: %d %d\n",tv,i,b[i]);
	}
}