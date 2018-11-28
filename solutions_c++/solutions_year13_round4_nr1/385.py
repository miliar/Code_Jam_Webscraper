#include<cstdio>
#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<string>
#include<cstdlib>
#include<climits>
#include<cstring>
using namespace std;

#define CLR(a,x) memset(a,x,sizeof(a))
#define PB push_back
#define INF 1000000000
#define MOD 1000002013  
#define MP make_pair
#define tr(container , it) for(typeof(container.begin()) it=container.begin() ; it!=container.end() ; it++)
#define FOR(i,a,b) for(i=a;i<b;i++)
#define REP(i,a) FOR(i,0,a)
#define LL long long
#define VI vector < int >
#define PII pair < LL , LL >


void precompute(void)
{
}
LL n;
multiset < PII > S,tickets;
LL getcost(LL o,LL d)
{
	LL travel=d-o;
	return ((n*travel)%MOD - ((travel*(travel-1))/2)%MOD + MOD)%MOD;
}

int main()
{
	LL t,test,from,m,i,o,d,num,ans;
	LL station,avail,canbe,expected;
	PII top;
	precompute();
	while(scanf("%lld",&t)!=EOF)
	{
		test=0;
		while(t--)
		{
			test++;
			printf("Case #%lld: ",test);
			fprintf(stderr,"Case #%lld: ",test);
			
			scanf("%lld%lld",&n,&m);
			S.clear();
			expected = 0;
			for(i=0;i<m;i++)
			{
				scanf("%lld%lld%lld",&o,&d,&num);
				S.insert(MP(o,-num));
				S.insert(MP(d,num));
					
				expected += (num*getcost(o,d))%MOD;
				expected %= MOD;	
			}

			ans=0;
			tickets.clear();
			while(!S.empty())
			{
				top=*(S.begin());
				S.erase(S.begin());
				num=-top.second;
				station=top.first;
				if(num > 0)
				{
					tickets.insert(MP(-station,num));
				}
				else
				{
					num = -num;
					while(num>0)
					{
						top=*(tickets.begin());
						tickets.erase(tickets.begin());

						from = -top.first;
						avail=top.second;

						canbe=min(avail,num);
						ans += canbe*getcost(from,station);
					//	printf("%lld %lld %lld %lld\n",canbe,from,station,getcost(from,station));
						ans %= MOD;
						num-=canbe;
						if(avail>canbe)
							tickets.insert(MP(-from,avail-canbe));
					}
				}
			}
		//	printf("%lld %lld\n",ans,expected);
			ans = (expected - ans + MOD)%MOD;
			printf("%lld\n",ans);
			fprintf(stderr,"%lld\n",ans);
		}
	}
	return 0;
}
