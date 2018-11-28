#include <bits/stdc++.h>

using namespace std;

typedef long long     LL;
typedef pair<int,int> pii;

double PI  = acos(-1);
double EPS = 1e-7;
int INF    = 1000000000;
LL INFLL   = 1000000000000000000LL;

#define fi            first
#define se            second
#define mp            make_pair
#define pb            push_back

#define input(in)     freopen(in,"r",stdin)
#define output(out)   freopen(out,"w",stdout)

#define MIN(a, b)     (a) = min((a), (b))
#define MAX(a, b)     (a) = max((a), (b))

#define RESET(a, b)   memset(a,b,sizeof(a))
#define ALL(a)        (a).begin(), (a).end()
#define SIZE(a)       (int)a.size()
#define SORT(a)       sort(ALL(a))
#define UNIQUE(a)     (a).erase( unique( ALL(a) ), (a).end() )
#define FOR(a, b, c)  for (int (a)=(b); (a)<=(c); (a)++)
#define FORD(a, b, c) for (int (a)=(b); (a)>=(c); (a)--)
#define FORIT(a, b)   for (__typeof((b).begin()) a=(b).begin(); a!=(b).end(); a++)

int mx[8] = {-1,1,0,0,-1,-1,1,1};
int my[8] = {0,0,-1,1,-1,1,-1,1};

// ----- //

char s[10005];
vector<string> words[25];
vector<int> wordsint[25];
vector<string> data;
pair<int,int> h[1000005];
pair<int,int> g[1000005];

int main() {
	int t,tc=0;
	scanf("%d",&t);
	while(t--) {
		tc++;
		data.clear();
		int n;
		scanf("%d",&n);
		FOR(a,1,n) {
			words[a].clear();
			wordsint[a].clear();
		}
		FOR(a,1,n) {
			while(scanf("%s",s) != EOF) {
				words[a].pb(s);
				data.pb(s);
				if (getchar() != ' ') break;
			}
		}

		SORT(data);
		UNIQUE(data);
		FOR(a,0,SIZE(data)-1) {
			h[a] = g[a] = mp(0,0);
		}
		FOR(a,1,n) {
			FOR(b,0,SIZE(words[a])-1) {
				wordsint[a].pb(lower_bound(data.begin(),data.end(),words[a][b])-data.begin());
			}
			if (a == 1) {
				FOR(b,0,SIZE(words[a])-1) {
					g[wordsint[a][b]].fi = 1;
					h[wordsint[a][b]].fi = 1;
				}
			}
			if (a == 2) {
				FOR(b,0,SIZE(words[a])-1) {
					g[wordsint[a][b]].se = 1;
					h[wordsint[a][b]].se = 1;
				}
			}
			

		}
		printf("Case #%d: ",tc);
		int ans = INF;
		for(int mask =0;mask <(1 <<(n-2));mask++) {
			FOR(a,0,n-3) {
				if (mask & (1 << a)) {
					FOR(b,0,SIZE(wordsint[a+3])-1) {
						h[wordsint[a+3][b]].fi = 1;
					}
				}
				else {
					FOR(b,0,SIZE(wordsint[a+3])-1) {
						h[wordsint[a+3][b]].se = 1;
					}
				}
			}
			int res = 0;
			FOR(a,0,SIZE(data)-1) {
				if (h[a] == mp(1,1)) {
					res++;
				}
				h[a] = g[a];
			}
			MIN(ans,res);
		}
		printf("%d\n",ans);
	}
}