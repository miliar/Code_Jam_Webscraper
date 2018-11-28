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
#define M 40
using namespace std;
typedef long long LL;
int t,n,tot,in[M],calc[M];
double ans;
int same()
{
	REP(i,1,n)
		if(in[i]+calc[i]!=in[1]+calc[1])
			return i-1;
	return n;
}
double work()
{
	int m=same();
	double p=1.0 / (double)same();
	double re=0.0;
	
	REP(i,1,m)re += calc[i]*36.0*p;
	return re;
}
void work(int ed,int val)
{
	int use=0;
	MSET(calc,0);


	REP(i,1,ed)
	{
		if(val < in[i])return;
		use+=val-in[i];
		calc[i]=val-in[i];
	}
	REP(i,ed+1,n)
	{
		if(val+1 < in[i])continue;
		use+=val+1-in[i];
		calc[i]=val+1;
	}
	if(use > tot)return;

	ans=max(ans,work()-use);
}
int main()
{
	scanf("%d",&t);
	REP(tt,1,t)
	{
		ans=0;
		MSET(in,0);
		
		scanf("%d %d",&tot,&n);
		REP(i,1,n)scanf("%d",&in[i]);
		n=37;
		sort(in+1,in+n+1);

		REP(i,1,n)REP(j,0,1500)work(i,j);
		printf("Case #%d: %.10f\n",tt,ans);
		        
	}
	return 0;
}

