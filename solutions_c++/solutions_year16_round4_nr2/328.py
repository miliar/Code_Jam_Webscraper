#include <string>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string.h>
#include <utility>
#include <queue>
#include <stack>
#include <iomanip>
#include <ctype.h>
#include <map>
#include <set>
#include <stdio.h>
#include <assert.h>
#include <ctype.h>
#include <math.h>
#include <time.h>
#include <iostream>
#include <iomanip>

using namespace std;

typedef long long LL;

#define FOR(i,n) for(int i = 0;i < n;i++)
#define MP make_pair
#define PB push_back
#define ALL(a) (a).begin(),(a).end()
#define PII pair<int, int>
#define PLL pair<long long, long long>
#define CLEAR(a) memset(a, 0, sizeof(a))
#define INF 2000000007
#define y1 uu1
#define y2 uu2
#define hash mash
const double EPS = 1E-12;
const double PI = acos(-1.0);
const LL mod = 1000000007;

using namespace std;

int n,k;
double x;
vector<double> p;
vector<double> choice;
double dp[205][205];

double mg(int alc, int arc) {
  if (alc > k/2 || arc > k/2) return 0;
  int idx = alc+arc;
  if (idx == choice.size()) return 1;

  if (dp[alc][arc] >= -0.5)
    return dp[alc][arc];

  return dp[alc][arc] = mg(alc+1,arc) * choice[idx] + mg(alc,arc+1) * (1 - choice[idx]);
}

double calc() {
  return mg(0,0);
}

void solve() {
  cin >> n >> k;
  p.clear();

  FOR(i, n) {
    cin >> x;
    p.push_back(x);
  }
  sort(ALL(p));

  double bst = -1;
  FOR(i, k+1) {
    choice.clear();
    FOR(j, i) choice.push_back(p[j]);
    FOR(j, k-i) choice.push_back(p[n-1-j]);

    FOR(j,k+1) FOR(g,k+1) dp[j][g] = -1;

    bst = max(bst, calc());
  }

  cout << fixed << setprecision(9) << bst << endl;
}

int main() {
  ios_base::sync_with_stdio(0);
  int tt;
  cin >> tt;

  FOR(t,tt) {
    cout << "Case #" << t+1 << ": ";
    solve();
  }

  return 0;
}
