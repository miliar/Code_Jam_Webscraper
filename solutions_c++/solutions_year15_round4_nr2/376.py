#include <bits/stdc++.h>

using namespace std;

typedef long long     LL;
typedef pair<int,int> pii;

double PI  = acos(-1);
double EPS = 1e-12;
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

double r[1005];
double c[1005];

int main() {
	int t,tc=0;
	scanf("%d",&t);
	while(t--) {
		tc++;
		int n;
		double V,x;
		scanf("%d%lf%lf",&n,&V,&x);
		FOR(a,1,n) {
			scanf("%lf %lf",&r[a],&c[a]);
		}
		if (n == 2 && c[1] == c[2]) {
			n = 1;
			r[1] += r[2];
		}
		if (n == 2) {
			if (c[1] > c[2]) {
				swap(c[1],c[2]);
				swap(r[1],r[2]);
			}
		}
		/*
		double left = 0.0;
		double right = 1000000000.0;
		FOR(iter,1,50) {
			double mid = (left+right)/2.0;

		}
		*/
		printf("Case #%d: ",tc);
		if (n == 2) {
			if (c[1] <= x && x <= c[2]) {
				double v2 = V*(x-c[1])/(c[2]-c[1]);
				double v1 = V*(x-c[2])/(c[1]-c[2]);
				
				if ( v1 >= 0 && v2 >= 0 ) {
					double t1 = v1/r[1];
					double t2 = v2/r[2];
					printf("%.10lf\n",max(t1,t2));
				}
				else {
					printf("IMPOSSIBLE\n");
				}
			}
			else {
				printf("IMPOSSIBLE\n");
			}
		}
		else if (n == 1) {
			if (x == c[1]) {
				printf("%.10lf\n",V/r[1]);
			}
			else {
				printf("IMPOSSIBLE\n");
			}
		}
		
	}
}