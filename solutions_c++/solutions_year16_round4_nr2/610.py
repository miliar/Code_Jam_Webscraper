#pragma comment(linker, "/stack:32000000")
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <cmath>
#include <sstream>
#include <stack>
#include <cassert>
#include <string.h>
#include <ctime>

#define pb push_back
#define mp make_pair
#define PI 3.1415926535897932384626433832795
#define sqr(x) (x)*(x)
#define forn(i, n) for(int i = 0; i < n; ++i)
#define ALL(x) x.begin(), x.end()
#define sz(x) int((x).size())
#define X first
#define Y second
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
using namespace std;
typedef pair<int,int> pii;
const int INF = 2147483647;
const ll LLINF = 9223372036854775807LL;

const int maxn = 210;
double dp[maxn][maxn];


double calcprob(const vector<double>& v) {
  vector<vector<double> > dp(sz(v)+1, vector<double>(sz(v)+1));
  dp[0][0] = 1.;
  forn(i, sz(v)) forn(j, i + 1) {
    dp[i+1][j] += dp[i][j] * (1 - v[i]);
    dp[i+1][j+1] += dp[i][j] * v[i];
  }
  return dp[sz(v)][sz(v)/2];
}

double solvestupid(vector<double> a, int k) {
  sort(ALL(a));
  vector<int> tt(sz(a));
  forn(i, k) tt[i] = 1;
  reverse(ALL(tt));
  double ans = 0;
  vector<vector<int> > bres;
  do {
    vector<double> tmp;
    forn(i, sz(tt)) if (tt[i]) tmp.pb(a[i]);
    double curans = calcprob(tmp);
    if (curans >= ans) {
      if (curans > ans) bres.clear();
      ans = curans;
      bres.pb(tt);
    }
  } while(next_permutation(ALL(tt)));
  forn(j, sz(bres)) {
    if (j == 50) break;
    forn(i, sz(bres[j])) {
      cerr << bres[j][i];
      
    }
    cerr << endl;
  }
  return ans;
}


double solvesmart(vector<double> V, int K) {
  sort(ALL(V));
  
  double ans = 0;

  forn(c1, K+1) {
    vector<double> a;
    int c2 = K-c1;
    forn(i, c1) a.pb(V[i]);
    reverse(ALL(V));
    forn(i, c2) a.pb(V[i]);
    double curans = calcprob(a);
    ans = max(ans, curans);
  }
  return ans;
}

void solve() {
  int n, K; scanf("%d%d", &n, &K);
  vector<double> V(n);
  forn(i, n) cin >> V[i];
  
  /*double ans1 = solvestupid(V, K);
  double ans2 = solvesmart(V, K);  
  printf("%.7lf %.7lf\n", ans1, ans2);
  if (fabs(ans1-ans2)>0.0000001) cerr << "FAIL!!!\n", exit(0);*/
  double ans = solvesmart(V, K);
  printf("%.15lf\n", ans);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

  int T; scanf("%d", &T);
  for (int tn = 1; tn <= T; ++tn) {
    cerr << "TEST " << tn << endl;
    printf("Case #%d: ", tn);
    solve();
  }
	return 0;
}