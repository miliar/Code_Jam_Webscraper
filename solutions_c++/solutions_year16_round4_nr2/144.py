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

double x[10005];
double y[10005];

double dp[205][405];
int vs[205][405];
int TT = 0;

double go(int p, int bal) {
  if (p == -1) {
    return (bal == 0);
  }
  if (vs[p][bal+202] == TT) {
    return dp[p][bal+202];
  }
  vs[p][bal+202] = TT;
  double &ret = dp[p][bal+202];
  return ret = y[p] * go(p - 1, bal + 1) + (1.0 - y[p]) * go(p - 1, bal - 1);
}

int main() {
  int tc;
  scanf("%d", &tc);
  while(tc--) {
    static int t = 0;
    printf("Case #%d: ", ++t);

    int n, k;
    scanf("%d%d",&n,&k);
    for(int i = 0; i < n; i++) {
      scanf("%lf", &x[i]);
    }
    sort(x, x+n);
    double res = 0.0;
    for(int i = 0; i <= k; i++) {
      TT++;
      for(int j = 0; j < i; j++) {
        y[j] = x[j];
      }
      for(int j = 0; j < k - i; j++) {
        y[k-1-j] = x[n-1-j];
      }
      MAX(res, go(k - 1, 0));
    }
    printf("%.8lf\n", res);
  }
}