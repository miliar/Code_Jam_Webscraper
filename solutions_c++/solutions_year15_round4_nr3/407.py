#include<set>
#include<map>
#include<cmath>
#include<queue>
#include<string>
#include<cstdio>
#include<vector>
#include<cassert>
#include<cstring>
#include<cstdlib>
#include<utility>
#include<iostream>
#include<algorithm>
#include<functional>
#define REP(x,y,z) for(int x=y;x<=z;x++)
#define FORD(x,y,z) for(int x=y;x>=z;x--)
#define MSET(x,y) memset(x,y,sizeof(x))
#define FOR(x,y) for(__typeof(y.begin()) x=y.begin();x!=y.end();x++)
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define SZ size()
#define M 105
using namespace std;
typedef long long LL;
int t,n,ans,now;
bool type[M];
vector<string> in[M];
map<string,int> v1,v2;

void readline(vector<string> &res)
{
	res.clear();
	
	string tmp, tmp2="";
	getline(cin, tmp);
	REP(i,0,(int)tmp.length()-1)
	{
		if(tmp[i]!=' ')
		{
			tmp2 += tmp[i];
		}
		else
		{
			if(tmp2!="") res.PB(tmp2);
			tmp2 = "";
		}
	}
	if(tmp2!="") res.PB(tmp2);
}
inline void add(int i,string x,int v)
{
	if(i==0)
	{
		v1[x] += v;
		if(v==-1 && v1[x]==0 && v2[x]) now--;
		if(v== 1 && v1[x]==1 && v2[x]) now++;
	}
	else
	{
		v2[x] += v;
		if(v==-1 && v2[x]==0 && v1[x]) now--;
		if(v== 1 && v2[x]==1 && v1[x]) now++;
	}
}
void dfs(int d)
{
	if(now >= ans) return;
	if(d>n)
	{
		ans = min(ans, now);
		return;
	}
	
	type[d] = 0;
	FOR(i,in[d]) add(0, *i, 1);
	dfs(d+1);
	FOR(i,in[d]) add(0, *i, -1);

	type[d] = 1;
	FOR(i,in[d]) add(1, *i, 1);
	dfs(d+1);
	FOR(i,in[d]) add(1, *i, -1);
}
int main()
{
	scanf("%d",&t);
	REP(tt,1,t)
	{
		now = 0;
		v1.clear();
		v2.clear();
		ans = 2000000000;
		scanf("%d\n",&n);
		REP(i,1,n) readline(in[i]);

		type[1] = 0;
		type[2] = 1;
		FOR(i,in[1]) add(0, *i, 1);
		FOR(i,in[2]) add(1, *i, 1);
		
		dfs(3);

		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}

