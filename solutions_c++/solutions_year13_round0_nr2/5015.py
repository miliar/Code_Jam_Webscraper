// File Name: b.cpp
// Author: Zlbing
// Created Time: 2013/4/13 12:26:57

#include<iostream>
#include<string>
#include<algorithm>
#include<cstdlib>
#include<cstdio>
#include<set>
#include<map>
#include<vector>
#include<cstring>
#include<stack>
#include<cmath>
#include<queue>
using namespace std;
#define CL(x,v); memset(x,v,sizeof(x));
#define INF 0x3f3f3f3f
#define LL long long
#define REP(i,r,n) for(int i=r;i<=n;i++)
#define RREP(i,n,r) for(int i=n;i>=r;i--)
const int MAXN=105;
int A[MAXN][MAXN];
int vis[MAXN][MAXN];
		int n,m;
struct node{
	int x,y,h;
	bool operator <(const node & a)const{
		return h<a.h;
	}
};
bool solve(node t)
{
	bool c=true,r=true;
	for(int i=1;i<=n;i++)
		if(vis[i][t.y]&&t.h<A[i][t.y])
			c=false;
	for(int i=1;i<=m;i++)
		if(vis[t.x][i]&&t.h<A[t.x][i])
			r=false;
	if(!r&&!c)return false;
	if(r)
		for(int i=1;i<=m;i++)
			A[t.x][i]=t.h;
	else
	if(c)
		for(int i=1;i<=n;i++)
			A[i][t.y]=t.h;

	return true;
}
int main()
{
	int T;
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++)
	{
		scanf("%d%d",&n,&m);
		REP(i,1,n)
			REP(j,1,m)
			A[i][j]=MAXN;
		priority_queue<node> Q;
		node t;
		REP(i,1,n)
			REP(j,1,m)
			{
				int a;
				scanf("%d",&a);
				t.x=i;t.y=j;t.h=a;
				Q.push(t);
			}
		CL(vis,0);
		bool flag=true;
		while(!Q.empty())
		{
			node t=Q.top();
			Q.pop();
			if(!solve(t))
			{
				flag=false;
				break;
			}
			vis[t.x][t.y]=1;
		}
		printf("Case #%d: ",cas);
		if(flag)printf("YES\n");
		else printf("NO\n");
	}
    return 0;
}
