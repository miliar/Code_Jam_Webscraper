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

char x[105][105];
int cntt[105][105];
int cnt2[105][105];

int main() {
	int t,tc=0;
	scanf("%d",&t);
	while(t--) {
		tc++;
		RESET(cntt,0);
		RESET(cnt2,0);
		int r,c;
		scanf("%d%d",&r,&c);
		FOR(a,0,r-1) {
			scanf("%s",x[a]);
		}
		FOR(a,0,r-1) {
			FOR(b,0,c-1) {
				if (x[a][b] != '.') {
					//cout << a << " " << b << " " << x[a][b] << endl;
					cnt2[a][b]++;
				}
				if (x[a][b] == '<') {
					cntt[a][b]++;
				}
				if (x[a][b] != '.') {
					break;
				}
			}
		}
		FOR(a,0,r-1) {
			FORD(b,c-1,0) {
				if (x[a][b] != '.') {
					cnt2[a][b]++;
				}
				if (x[a][b] == '>') {
					cntt[a][b]++;
				}
				if (x[a][b] != '.') {
					break;
				}
			}
		}
		
			FOR(b,0,c-1) {
				FORD(a,r-1,0) {
				if (x[a][b] != '.') {
					cnt2[a][b]++;
				}
				if (x[a][b] == 'v') {
					cntt[a][b]++;
				}
				if (x[a][b] != '.') {
					break;
				}
			}
		}
		
			FOR(b,0,c-1) {
				FOR(a,0,r-1) {
				if (x[a][b] != '.') {
					cnt2[a][b]++;
				}
				if (x[a][b] == '^') {
					cntt[a][b]++;
				}
				if (x[a][b] != '.') {
					break;
				}
			}
		}
		bool ada4 = 0;
		int change = 0;
		FOR(a,0,r-1) {
			FOR(b,0,c-1) {
				if (cnt2[a][b] == 4) ada4 = 1;
				else if (cntt[a][b] > 0) change++;
			}
		}
		printf("Case #%d: ",tc);
		if (ada4) puts("IMPOSSIBLE");
		else printf("%d\n",change);
	}
}