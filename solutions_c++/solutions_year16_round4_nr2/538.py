#include <bits/stdc++.h>
#include <ext/hash_map>
#include <ext/hash_set>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/priority_queue.hpp>
using namespace std;
using namespace __gnu_cxx;
using namespace __gnu_pbds;
#define XINF INT_MAX
#define INF 0x3F3F3F3F
#define MP(X,Y) make_pair(X,Y)
#define PB(X) push_back(X)
#define REP(X,N) for(int X=0;X<N;X++)
#define REP2(X,L,R) for(int X=L;X<=R;X++)
#define DEP(X,R,L) for(int X=R;X>=L;X--)
#define CLR(A,X) memset(A,X,sizeof(A))
#define IT iterator
#define RIT reverse_iterator
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> PII;
typedef vector<PII> VII;
typedef vector<int> VI;
typedef tree<int, int, greater<int>, rb_tree_tag, tree_order_statistics_node_update > rb_tree;
#define ALL(X) (X).begin(),(X).end()
#define PQ std::priority_queue
#define HEAP __gnu_pbds::priority_queue
#define X first
#define Y second
#define lson(X) ((X)<<1)
#define rson(X) ((X)<<1|1)

void chmax(double &a, double b) {
	if(a < b) a = b;
}

double dp[211][211];
double p[201];
int main()
{
#ifdef LOCAL
	   freopen("B-large.in","r",stdin);
	   freopen("B-large.out","w",stdout);
#endif
	ios::sync_with_stdio(false);
	int t,cs=1;
	cin>>t;
	while(t--) {
		int n,k;
		cin>>n>>k;
		REP(i,n) cin>>p[i];
		sort(p, p+n);
		double ans = 0;
		REP(l,k+1) {
			int r = k-l;
			vector<double> v;
			REP(i,l) v.PB(p[i]);
			REP(i,r) v.PB(p[n-i-1]);
			CLR(dp,0);
			dp[0][0] = 1;
			REP(i,k) {
				REP(j,k/2+1) {
					dp[i+1][j+1] += dp[i][j] * v[i];
					dp[i+1][j] += dp[i][j] * (1-v[i]);
				}
			}
			ans = max(ans, dp[k][k/2]);
		}
		
		cout<<"Case #"<<cs++<<": ";
		cout<<fixed<<setprecision(10)<<ans<<endl;
	}
	return 0;
}


