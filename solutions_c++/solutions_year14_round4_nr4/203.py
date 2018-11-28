/*
Author: elfness@UESTC
*/
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<vector>
#include<string>
using namespace std;
typedef long long LL;
struct tree
{
    tree *ne[26],*fail;
    int ct;
}tr[500100],VD,*root,*Q[500100];
int tn;
void init()
{
    tr[tn=0]=VD;
    root=tr+(tn++);
}
char s[100][110];
void build(int id)
{
    tree *p=root;
    for(int i=0;s[id][i];i++)
    {
        if(p->ne[s[id][i]-'A']==NULL)
        {
            tr[tn]=VD;
            p->ne[s[id][i]-'A']=tr+(tn++);
        }
        p=p->ne[s[id][i]-'A'];
    }
    p->ct++;
}
const int V=(1<<16)+10;
int a[V],t,bel[12],n,m,_;
void dfs(int k)
{
	if(k==n)
	{
		int cost=0;
		for(int i=0;i<m;i++)
		{
			init();
			for(int j=0;j<n;j++)
			if(bel[j]==i)build(j);
			if(tn==1)tn=0;
			cost+=tn;
		}
		a[t++]=cost;
		return;
	}
	for(int i=0;i<m;i++)
	{
		bel[k]=i;
		dfs(k+1);
	}
}
int main()
{
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	for(int i=0;i<26;i++)VD.ne[i]=NULL;VD.ct=0;
	scanf("%d",&_);
	for(int ca=1;ca<=_;ca++)
	{
		scanf("%d%d",&n,&m);
		t=0;
		for(int i=0;i<n;i++)
		scanf("%s",s[i]);
		dfs(0);
		sort(a,a+t);
		int ret=0;
		for(int i=0;i<t;i++)
		if(a[i]==a[t-1])ret++;
		printf("Case #%d: %d %d\n",ca,a[t-1],ret);
	}
	return 0;
}
