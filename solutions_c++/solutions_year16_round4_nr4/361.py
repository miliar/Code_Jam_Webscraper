/* ***********************************************
Author        :axp
Created Time  :2016/5/28 23:47:23
TASK		  :D.cpp
LANG          :C++
************************************************ */

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

const int N = 4;
int T;
int n;
bool ar[N][N];
bool b[N][N];
char ch[N<<1];
int ans;
bool dp[N+1][1<<N];
bool vis[N+1][1<<N];
int ord[N];

bool f(int id,int st)
{
	bool &re=dp[id][st];
	if(vis[id][st])return re;
	vis[id][st]=1;
	if(id==n)return re=1;
	int now=ord[id];
	re=0;
	bool flag=0;
	for(int i=0;i<n;i++)
	{
		if(st&(1<<i))continue;
		if(b[now][i])
		{
			if(f(id+1,st|(1<<i))==0)return re=0;
			flag=1;
		}
	}
	return re=flag;
}

int cal(int x)
{
	int re=0;
	while(x)
	{
		re++;
		x-=x&-x;
	}
	//cout<<x<<' '<<re<<endl;
	return re;
}

bool ok(int st)
{
	for(int i=0;i<n;i++)
		for(int j=0;j<n;j++)
		{
			b[i][j]=ar[i][j];
			if(st&(1<<(i*n+j)))
				b[i][j]=1;
		}
	for(int i=0;i<n;i++)
		ord[i]=i;
	do
	{
		memset(vis,0,sizeof vis);
		if(f(0,0)==0)return 0;
	}while(next_permutation(ord,ord+n));
	//cout<<st<<endl;
	return 1;
}

int main()
{
    //freopen("in.txt","r",stdin);
    freopen("D-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
	for(int kase=1;kase<=T;kase++)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%s",ch);
			for(int j=0;j<n;j++)
				ar[i][j]=ch[j]-'0';
		}
		ans=N*N;
		for(int st=0;st<(1<<(n*n));st++)
			if(ok(st))
				ans=min(ans,cal(st));
		printf("Case #%d: %d\n",kase,ans);
	}
    return 0;
}
