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
#define MOD 1000000007
#define MP make_pair
#define tr(container , it) for(typeof(container.begin()) it=container.begin() ; it!=container.end() ; it++)
#define FOR(i,a,b) for(i=a;i<b;i++)
#define REP(i,a) FOR(i,0,a)
#define LL long long
#define VI vector < int >
#define PII pair < int , int >


void precompute(void)
{
}


int main()
{
	LL cur,sz,n,p,t,test,temp,jump,willwin,canwin,jump2;
	precompute();
	while(scanf("%lld",&t)!=EOF)
	{
		test=0;
		while(t--)
		{
			test++;
			printf("Case #%lld: ",test);
			fprintf(stderr,"Case #%lld: ",test);

			scanf("%lld%lld",&n,&p);
			sz=(1LL<<n);
			temp=p;
			canwin=0;
			jump=sz;
			while(temp>1)
			{
				jump/=2;
				canwin+=jump;
				temp/=2;
			}

			if(p==sz)
				willwin=sz-1;
			else
			{
				cur=sz/2;

				willwin=0;
				jump=1;
				jump2=sz/2;
				while(p>cur)
				{
					jump*=2;
					willwin+=jump;
					jump2/=2;
					cur+=jump2;
				}
			}
			printf("%lld %lld\n",willwin,canwin);
			fprintf(stderr,"%lld %lld\n",willwin,canwin);
		}
	}
	return 0;
}
