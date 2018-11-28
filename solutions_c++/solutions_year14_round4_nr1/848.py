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


int n,x;
int p[100005];
int y[100005];

int main()
{
	int t,tc=0;
	scanf("%d",&t);
	while(t--)
	{
		tc++;
		printf("Case #%d: ",tc);
		scanf("%d%d",&n,&x);
		FOR(a,1,n)
		{
			y[a] = 0;
			scanf("%d",&p[a]);
		}
		sort(p+1,p+n+1);
		int it = n;
		int ans = 0;
		FOR(a,1,n)
		{
			if (y[a]) continue;
			while (it > a && p[it]+p[a] > x) it--;
			if (it > a && p[it]+p[a] <= x) y[it]=1,it--;
			y[a] = 1;
			ans++;
		}
		printf("%d\n",ans);
	}
}
