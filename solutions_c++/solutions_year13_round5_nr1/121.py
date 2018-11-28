#include <cstdio>
#include <cassert>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);i++)
typedef long long ll;

vector<int> my_bet;

struct cmp
{
	bool operator() (pair<int,int> a, pair<int,int> b)
	{
		if(a.first!=b.first)
			return a.first>b.first;
		return my_bet[a.second]>my_bet[b.second];

	}
};

const int n=37;


int main()
{
	int t;
	scanf("%d",&t);
	for(int test=1;test<=t;test++)
	{
		fprintf(stderr,"%d\n",test);
		ll N,B;
		scanf("%lld%lld",&B,&N);
		vector<ll> bet(37);
		REP(i,N)
			scanf("%lld",&bet[i]);
		sort(bet.begin(),bet.end());

		double gres=0;

		for(int j=1;j<=n;j++)
			for(int i=0;i+j<=n;i++)
			{
				ll v=B-i;
				REP(k,i+j)
					v+=bet[k];
				if(v<0) continue;
				v=v/(i+j);
				if(i+j<n)
					v=min(v,bet[i+j]-1);
				if(v<0 || v+1<bet[i+j-1] ||  v<bet[j-1]) continue;
				//v - ставка
				ll cost=0;
				for(int k=0;k<j;k++)
				{
					assert(v-bet[k]>=0);
					cost+=v-bet[k];
				}
				for(int k=j;k-j<i;k++)
				{
					assert(v+1-bet[k]>=0);
					cost+=v+1-bet[k];
				}
				double res=0;
				for(int k=0;k<j;k++)
				{
					res+=36*(v-bet[k])-cost;
				}
				res/=j;
				gres=max(gres,res);
			}

		printf("Case #%d: %.10lf\n",test,gres);
	}
	return 0;
}
