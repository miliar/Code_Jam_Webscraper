#include <bits/stdc++.h>

#define fori(i,b,e) for (int i = (b); i < (e); i++)
#define mp make_pair
#define pb push_back
#define all(a) (a).begin(), (a).end()
#define elsif else if
#define sz(a) ((int)(a).size())
#define X first
#define Y second

using namespace std;

typedef long long int int64;
typedef pair<int, int> pii;
typedef vector<int> vi;

inline int getInt() { int res;  scanf("%d", &res);  return res; }
inline double getDbl() { double res;  scanf("%lf", &res);  return res; }

const int maxn = 201;
double dp[maxn][maxn];

double a[maxn];
double p[maxn];

void solve() {
  int n = getInt(), k = getInt();
  fori(i,0,n) {
    p[i] = getDbl();
  }
  /*fori(i,0,n) {
    printf("%f ", p[i]);
  }
  printf("\n");*/
  sort(p, p+n);
  fori(i,0,n) {
    a[i] = p[i];
  }
  double maxv = 0;
  for (int left = 0; left <= k; left++) {
    fori(i,0,left) {
      p[i] = a[i];
    }
    int rem = k - left;
    fori(i,0,rem) {
      p[left+i] = a[n-rem+i];
    }
    dp[0][0] = 1 - p[0];
    dp[0][1] = p[0];
    fori(i,1,k) {
      fori(j,1,k+1) {
        dp[i][j] = dp[i-1][j] * (1 - p[i]) + dp[i-1][j-1] * p[i];
      }
      dp[i][0] = dp[i-1][0] * (1 - p[i]);
    }
    maxv = max(maxv, dp[k-1][k/2]);
  }
  //cout.precision(20);
  //cout << dp[n-1][n/2] << endl;
  printf("%.20f\n", maxv);
}

int main() {
  freopen("in.txt", "rt", stdin);
  freopen("out.txt", "wt", stdout);
  srand(time(0));
  int N = getInt();
  fori(T,1,N+1) {
    printf("Case #%d: ", T);
    solve();
  }
  return 0;
}
