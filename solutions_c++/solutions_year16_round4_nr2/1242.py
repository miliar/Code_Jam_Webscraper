#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef pair< ll, ll > ii;
typedef vector< ll > vi;
typedef vector< ii > vii;

#define INF 0x3F3F3F3F
#define LINF 0x3F3F3F3F3F3F3F3FLL
#define pb push_back
#define mp make_pair
#define pq priority_queue
#define LSONE(s) ((s)&(-s))
#define DEG_to_RAD(X)   (X * PI / 180)
#define F first
#define S second
#define PI 2*acos(0)

#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

//////////////////////
int dx[] = {-1,0,1,0};
int dy[] = {0,1,0,-1};
//////////////////////

const int N = 202;

int n, k;
ld pd[N][N];
short memo[N][N];
double p[N];
vector< double > at;

double solve(int pos, int qa) {
  if(pos == k) return qa == 100;
  if(memo[pos][qa]) return pd[pos][qa];
  double ret = solve(pos + 1, qa + 1) * at[pos] + solve(pos + 1, qa - 1) * (1. - at[pos]);
  return pd[pos][qa] = ret;
}

inline void main2() {
  memset(memo, 0, sizeof memo);
  scanf("%d %d", &n, &k);
  for(int i = 0; i < n; ++i) scanf("%lf", p + i);
  double ans = 0;
  for(int i = 0; i < (1 << n); ++i) {
    if(__builtin_popcount(i) != k) continue;
    memset(memo, 0, sizeof memo);
    at.clear();
    for(int j = 0; j < n; ++j) if((i >> j) & 1) at.pb(p[j]);
    ans = max(ans, solve(0, 100));
  }
  printf("%.10lf\n", ans);
}

int main() {
  int t; scanf("%d", &t);
  for(int i = 1; i <= t; ++i) {
    printf("Case #%d: ", i);
    main2();
  }
  return 0;
}