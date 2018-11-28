#include<cstdio>
#include<iostream>
#include<queue>
#include<map>
#include<set>
#include<algorithm>
#include<cmath>
#include<cstdlib>
using namespace std;

#define inf 1023456789
#define linf 1023456789123456789ll
#define pii pair<int,int>
#define pipii pair<int, pii >
#define pll pair<long long,long long>
#define vint vector<int>
#define vvint vector<vint >
#define ll long long
#define pdd pair<double, double>

#define DEBUG
#ifdef DEBUG
#define db(x) cerr << #x << " = " << x << endl
#else
#define db(x)
#endif

int main()
{
	int t;
	scanf("%d",&t);
	for(int test=0; test<t; test++)
	{
		int n,k;
		scanf("%d %d",&n,&k);
		vector<ll> sum(n-k+1);
		for(int i=0; i<n-k+1; i++)
		{
			scanf("%lld",&sum[i]);
		}
		vector<ll> delta(n, 0);
		vector<ll> classmin(k, 0), classmax(k, 0);
		for(int i=k; i<n; i++)
		{
			delta[i] = delta[i-k] + sum[i-k+1] - sum[i-k];
			classmax[i%k] = max(classmax[i%k], delta[i]);
			classmin[i%k] = min(classmin[i%k], delta[i]);
		}
		
		ll lo = -1, hi = inf;
		while(lo < hi-1)
		{
			ll mid = (lo+hi)/2;
			bool dasa = 1;
			ll mins = 0, maxs = 0;
			for(int i=0; i<k; i++)
			{
				if(classmax[i] - classmin[i] > mid)
				{
					dasa = 0;
					break;
				}
				mins += -classmin[i];
				maxs += mid - classmax[i];
			}
			if(dasa)
			{
				ll mod = (sum[0] + (k * 10000))% k;
				ll chcem = mins - (mins%k) + mod;
				if(mins % k > mod)
				{
					chcem += k;
				}
				if(maxs < chcem)dasa = 0;
			}
			if(dasa)hi = mid;
			else lo = mid;
		}
		printf("Case #%d: %lld\n",test+1, hi);
	}
	return 0;
}