#include <vector>
#include <cstring>
#include <cstdio>
#include <queue>
#include <cmath>
#include <string>
#include <iostream>
#include <algorithm>
#include <cassert>
#include <ctype.h>
#include <ctime>
#include <map>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);i++)

typedef long long ll;

const int MAXN=50;
char buf[3000];

int bitcnt(int n)
{
	int res=0;
	while(n)
	{
		res+=n&1;
		n>>=1;
	}
	return res;
}

int testbit(int n, int m)
{
	return (n>>m)&1;
}

int n;

int used[2*MAXN];
int adj[2*MAXN][2*MAXN];


int dfs(int cur, int clr)
{
	if(used[cur]==clr) return 0;
	int res=(cur<n)?1:-1;
	used[cur]=clr;
	for(int i=0;i<2*n;i++)
		if(adj[cur][i])
			res+=dfs(i,clr);
	return res;
}

struct State
{
	vector<pair<int,int> > bal;
	int pos, curb, curv;
	State(const vector<pair<int,int> > &bal, int pos, int curb, int curv):
		bal(bal), pos(pos),curb(curb), curv(curv)
	{}
	bool operator<(const State& b) const
	{
		if(pos!=b.pos)
			return pos<b.pos;
		if(curb!=b.curb)
			return curb<b.curb;
		if(curv!=b.curv)
			return curv<b.curv;
		return bal<b.bal;
	}
};

map<State,int> dp;
const int INF=1000000000;

int solve(const vector<pair<int,int> > &bal, int pos, int curb, int curv)
{
	if(bal.empty()) return curv*curv;
	if(curv!=0 && curb==0) return solve(bal, 0, 0, 0)+curv*curv;
	if(curv==0 && curb==0)
	{
		vector<pair<int,int> > t=bal;
		pair<int,int> bv=*(t.end()-1);
		t.erase(t.end()-1);
		return solve(t, 0, curb+bv.first, curv+bv.second);
	}
	if(pos==bal.size())
		return INF;

	State st(bal,pos,curb,curv);
	map<State,int>::iterator it=dp.find(st);
	if(it==dp.end())
	{
		int res=INF;
		res=min(res, solve(bal, pos+1, curb, curv));
		{
			vector<pair<int,int> > t=bal;
			pair<int,int> bv=*(t.end()-1-pos);
			t.erase(t.end()-1-pos);
			res=min(res, solve(t, pos, curb+bv.first, curv+bv.second));
		}
		dp[st]=res;
		return res;
	}
	return it->second;
}

int solve()
{
	scanf("%d",&n);
	memset(adj,0,sizeof(adj));
	int cnt=0;
	REP(i,n)
	{
		scanf("%s",buf);
		REP(j,n)
		{
			adj[i][j+n]=adj[j+n][i]=buf[j]-'0';
			if(buf[j]=='1')
				cnt++;
		}
	}
	memset(used,0,sizeof(used));
	vector<pair<int,int> > bal;
	for(int i=0;i<2*n;i++)
		if(!used[i])
		{
			int balance=dfs(i,i+1);
			int cnt=count(used,used+n,i+1);
			bal.push_back(make_pair(balance,cnt));
		}
	sort(bal.begin(), bal.end());
	dp.clear();
	return solve(bal, 0, 0, 0 )-cnt;
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
	{
		printf("Case #%d: %d\n",test,solve());
	}
	return 0;
}
