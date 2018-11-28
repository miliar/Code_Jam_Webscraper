#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

char a[20][20];
int n,mn,m,s1,s2;
int next[100][30];

int bld(int b)
{
	int i,j,bb,nn=1,rt;
	memset(next,0,sizeof(next));
	for(i=0,bb=1;i<n;i++,bb<<=1)
		if(b&bb)
			for(rt=0,j=0;a[i][j];j++)
			{
				if(!next[rt][a[i][j]-'A'])
					next[rt][a[i][j]-'A']=nn++;
				rt=next[rt][a[i][j]-'A'];
			}
	return nn;
}

void dfs(int d,int b,int ss)
{
	int i,bb;
	if(d==m)
	{
		b=~b;
		for(i=0,bb=1;i<n;i++,bb<<=1)
			if(bb&b)
				break;
		if(i<n)
		{
			ss+=bld(b);
			if(ss>s1)
				s1=ss,s2=0;
			if(ss==s1)
				s2++;
		}
	}
	else
	{
		for(bb=1;bb<mn;bb++)
		{
			if(b&bb)
				continue;
			dfs(d+1,b|bb,ss+bld(bb));
		}
	}
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,t,i;
	for(scanf("%d",&T),t=1;t<=T;t++)
	{
		for(scanf("%d %d",&n,&m),i=0;i<n;i++)
			scanf("%s",a[i]);
		mn=1<<n;
		s1=-1;
		dfs(1,0,0);
		printf("Case #%d: %d %d\n",t,s1,s2);
	}
	return 0;
}
