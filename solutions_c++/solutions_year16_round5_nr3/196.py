/* ***********************************************
Author        :axp
Created Time  :2016/6/11 22:58:55
TASK		  :C.cpp
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

typedef pair<int,int> pii;
const int N = 1e3+10;
int dp[N][N];
bool vis[N];
int n;
int s;

struct Point
{
	int x[3];
	int v[3];
	void read()
	{
		for(int i=0;i<3;i++)scanf("%d",x+i);
		for(int i=0;i<3;i++)scanf("%d",v+i);
	}
}ar[N];

priority_queue<pii> q;

int sq(int x)
{
	return x*x;
}

int dis(int x,int y)
{
	int re=0;
	for(int i=0;i<3;i++)
		re+=sq(ar[x].x[i]-ar[y].x[i]);
	return re;
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
	scanf("%d",&T);
	for(int kase=1;kase<=T;kase++)
	{
		scanf("%d%d",&n,&s);
		for(int i=1;i<=n;i++)
			ar[i].read();
		int ans;
		while(!q.empty())q.pop();
		memset(vis,0,sizeof vis);
		q.push(make_pair(0,1));
		for(;;)
		{
			pii p=q.top();
			q.pop();
			int k=-p.first;
			int x=p.second;
			//cout<<x<<' '<<k<<' '<<q.size()<<endl;
			if(vis[x])continue;
			if(x==2)
			{
				ans=k;
				break;
			}
			vis[x]=1;
			for(int i=1;i<=n;i++)
			{
				if(vis[i])continue;
				q.push(make_pair(-max(k,dis(i,x)),i));
			}
		}
		printf("Case #%d: %.7lf\n",kase,sqrt(ans));
	}
    return 0;
}
