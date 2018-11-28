#include <algorithm>
#include <iostream>
#include <sstream>
#include <cassert>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <deque>
#include <ctime>
#include <list>
#include <set>
#include <map>
//zlb//

using namespace std;

typedef long long     LL;
typedef pair<int,int> pii;

double PI  = acos(-1);
double EPS = 1e-7;
int INF    = 1000000000;
int MOD    = 1000000007;
int MAXINT = 2147483647;
LL INFLL   = 1000000000000000000LL;
LL MAXLL   = 9223372036854775807LL;

#define fi            first
#define se            second
#define mp            make_pair
#define pb            push_back
#define SIZE(a)       (int)a.size()
#define MIN(a, b)     (a) = min((a), (b))
#define MAX(a, b)     (a) = max((a), (b))
#define input(in)     freopen(in,"r",stdin)
#define output(out)   freopen(out,"w",stdout)
#define RESET(a, b)   memset(a,b,sizeof(a))
#define FOR(a, b, c)  for (int (a)=(b); (a)<=(c); (a)++)
#define FORD(a, b, c) for (int (a)=(b); (a)>=(c); (a)--)
#define FORIT(a, b)   for (__typeof((b).begin()) a=(b).begin(); a!=(b).end(); a++)

int mx[8] = {-1,1,0,0,-1,-1,1,1};
int my[8] = {0,0,-1,1,-1,1,-1,1};

// ------------ //


pii x[1005];
int z[1005];
int cnt1[1005];
int cnt2[1005];
int dp[1005][1005];
int n;
map<int,int> id;
int go(int l,int r)
{

	if (dp[l][r] != -1) return dp[l][r];
	int cur = n-1-(l+r);
	if (cur == -1) return dp[l][r] = 0;
	return dp[l][r] = min(cnt1[cur]+go(l+1,r),cnt2[cur]+go(l,r+1));
}

int main()
{
	int t,tc=0;
	scanf("%d",&t);
	while(t--)
	{
		tc++;
		RESET(dp,-1);
		id.clear();
		printf("Case #%d: ",tc);
		
		scanf("%d",&n);
		FOR(a,0,n-1)
		{
			scanf("%d",&z[a]);
			x[a] = mp(z[a],a);
		}
		sort(x,x+n);
		FOR(a,0,n-1)
		{
			id[x[a].fi] = x[a].se;
		}
		FOR(a,0,n-1)
		{
			z[a] = id[z[a]];
		}
		FOR(a,0,n-1)
		{
			cnt1[a] = cnt2[a] = 0;
			FOR(b,a+1,n-1)
			{
				if (id[x[b].fi] > id[x[a].fi]) cnt1[a]++;
				if (id[x[b].fi] < id[x[a].fi]) cnt2[a]++;
			}
			//cout << a << " " << cnt1[a] << " " << cnt2[a] << endl;
		}
		printf("%d\n",go(0,1));
	}
}
