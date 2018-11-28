#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#define PB push_back
#define MP make_pair
#define X first
#define Y second
#define lc (k<<1)
#define rc ((k<<1)|1)
#define mi ((l+r)>>1)
#define fk puts("fuck!")
using namespace std;
typedef long long ll;
typedef unsigned long long ull;

const int N=1000003;
int dp[N];

queue<int> q;
vector<int> tmp, pos;

void getnum(int x)
{
	pos.clear();
	int xx=x;
	while(xx)
	{
		pos.PB(xx%10);
		xx/=10;
	}
}

void change(int x)
{
	tmp.clear();
	tmp.PB(x+1);
	getnum(x);
	int sz=pos.size();
	int nnn=0, quan=1;
	for(int i=0;i<sz;i++)
	{
		nnn+=pos[sz-1-i]*quan;
		quan*=10;
	//	printf("tmp[%d]=%d\n",sz-1-i,tmp[sz-i-1]);///
	}
	//printf("x=%d nnn=%d\n",x,nnn);///
	if(nnn!=x+1) tmp.PB(nnn);
}

void bfs()
{
	while(q.size()) q.pop();
	int tim=2;dp[1]=1;
	q.push(1);q.push(0);
	while(q.size()>1)
	{
		if(q.front()==0)
		{
			q.pop();
			tim++;
			q.push(0);
			continue;
		}
		int x=q.front();q.pop();
		//printf("%d\n",x);
		change(x);
		for(int i=0;i<tmp.size();i++)
		{
			int y=tmp[i];
			if(y<=1000000 && tim<dp[y])
			{
				dp[y]=tim;
				q.push(y);
			}
		}
	}
}

void test()
{
	for(int i=1;i<=100;i++)
		printf("dp[%d]=%d\n",i,dp[i]);
}

int main()
{
	freopen("in","r",stdin);///
	int cas;scanf("%d",&cas);
	memset(dp,127,sizeof(dp));
	bfs();
	//test();
	//*
	for(int t=1;t<=cas;t++)
	{
		int n;scanf("%d",&n);
		printf("Case #%d: %d\n",t,dp[n]);
	}//*/
	return 0;
}