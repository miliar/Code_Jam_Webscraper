#include <iostream>
#include <algorithm>
#include <cmath>
#include <assert.h>
#include <stdio.h>
#include <ctime>
#include <cstdlib>
#include <utility>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
 
#define INF (1<<30)
#define pii pair<int,int>
#define pll pair<long long,long long>
#define eps 1e-9
 
#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) //fprintf(stderr,args)
#endif

#define pb push_back

using namespace std;

int v[1010];

int dp[1010][1010];

int l[1010];

int n;
int r[1010];

int get(int a,int b){

	int t = max(a,b);

	if(t == n-1)
		return 0;

	if(dp[a+1][b+1]+1)
		return dp[a+1][b+1];

	int ret = dp[a+1][b+1] = min(l[t+1] + get(t+1,b), r[t+1] + get(a,t+1));
	debug("dp[%d][%d] = %d\n",a,b,ret);
	return ret;
}

main(){

		int t;
		scanf("%d",&t);

		for(int te=1;te<=t;te++){

			printf("Case #%d: ",te);

			memset(dp,-1,sizeof(dp));
			memset(l,0,sizeof(l));
			memset(r,0,sizeof(r));

			scanf("%d",&n);

			vector<int> u;
			for(int i=0;i<n;i++){
				scanf("%d",v+i);
				u.pb(v[i]);
			}

			sort(u.begin(), u.end());

			map<int,int> mp;

			for(int i=1;i<n;i++)
				mp[u[i]] = i;

			for(int i=0;i<n;i++)
				v[i] = mp[v[i]];

			debug(": ");
			for(int i=0;i<n;i++)
				debug("%d ",v[i]);
				debug("\n");

			for(int i=0;i<n;i++){

				for(int j=0;j<i;j++)
					if(v[j] > v[i])
						l[v[i]]++;
				for(int j=i+1;j<n;j++)
					if(v[j] > v[i])
						r[v[i]]++;

				}

			for(int i=0;i<n;i++)
				debug("%d: l = %d r = %d\n",i,l[i],r[i]);

			printf("%d\n",get(-1,-1));

		}

}
