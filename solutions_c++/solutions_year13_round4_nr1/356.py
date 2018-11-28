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
#define M 1005
#define MOD 1000002013
using namespace std;
typedef long long LL;
struct P{int x,id;bool in;};

int t,n,m,p[M],s[M],st[M],ed[M],fr[M],top;
P in[2*M];
LL ans,cnt;
const LL rev=500001007;

bool comp(P x,P y)
{
	if(x.x != y.x)return x.x<y.x;
	if(x.in != y.in)return x.in;
	return false;
}
LL cost(LL f)
{
	if(!f)return 0LL;
	
	LL x=(2LL*(LL)m+1ll) % MOD;
	x = (x*f)%MOD;
	LL y=(f*f)%MOD;
	
	x = (x-y)%MOD;
	x *= rev;
	return (x%MOD+MOD)%MOD;
}
LL pow(LL x,LL y)
{
	LL re=1,tmp=x;
	while(y)
	{
		if(y&1)re*=tmp;
		tmp*=tmp;
		re%=MOD;
		tmp%=MOD;
		y>>=1;
	}
	return re;
}
int main()
{	
	int x,y;

	scanf("%d",&t);
	REP(tt,1,t)
	{
		top=ans=cnt=0;
		scanf("%d %d",&m,&n);

		//printf("%I64d %I64d\n",cost(1ll),cost(2ll));
		REP(i,1,n)
		{
			scanf("%d %d %d",&x,&y,&p[i]);
			fr[i]=p[i];
			st[i]=x;
			ed[i]=y;
			in[2*i-1] = (P){x,i,true};
			in[2*i] = (P){y,i,false};
			
			cnt+=cost(y-x)*p[i];
			cnt%=MOD;
		}
		sort(in+1,in+2*n+1,comp);

		REP(i,1,2*n)
		{
			if(in[i].in)
				s[top++]=in[i].id;
			else
			{
				int cc=p[in[i].id];
				while(cc > 0)
				{
					x = min(cc, fr[s[top-1]]);
					
					ans += cost(ed[in[i].id] - st[s[top-1]]) * x;
					ans %= MOD;

					fr[s[top-1]]-=x;
					cc-=x;
					if(fr[s[top-1]] <= 0)top--;
				}
			}
		}

		ans = ((cnt-ans)%MOD + MOD) % MOD;
		printf("Case #%d: %I64d\n",tt,ans);
	}
	return 0;
}

