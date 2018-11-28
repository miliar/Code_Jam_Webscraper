/*{{{*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <unordered_map>
#include <unordered_set>
#include <cassert>
using namespace std;
typedef pair<int, int> PP;
typedef long long LL;
#define pb push_back
#define fr first
#define sc second
#define bitcnt __builtin_popcount
#define all(x) x.begin(), x.end()
inline int ri() {int x; scanf("%d", &x); return x;}
#define rep2(i, n, ...) for (int i = 0; i < (n); i ++) 
#define rep3(i, a, b, ...) for (int i = (a); i < (b); i ++)
#define GET_MACRO(_1, _2, _3, NAME, ...) NAME
#define rep(...) GET_MACRO(__VA_ARGS__, rep3, rep2)(__VA_ARGS__)
#define drep2(i, n, ...) for (int i = (n) - 1; i >= 0; i --)
#define drep3(i, a, b) for (int i = (a) - 1; i >= (b); i --)
#define drep(...) GET_MACRO(__VA_ARGS__, drep3, drep2)(__VA_ARGS__)
template<typename T>inline bool smax(T&a, T b){if(a<b){a=b;return true;}return false;} 
template<typename T>inline bool smin(T&a, T b){if(a>b){a=b;return true;}return false;} 
/*}}}*/


int B = 500;

#define double long double

int n, m;
double p[1000], ip[1000];

double w[1000][1000];

double l[300][300], r[300][300];

void test(int n = 10) {
  srand(time(0));
  int best = -1;
  double prob = 0;
  vector<double> p(n);
  rep(i, n) p[i] = (rand() % 1001) / 1000.0;
  sort(all(p));
  rep(i, 1, (1 << n)) if (bitcnt(i) == 4) {
    //cerr << i << endl;
    vector<double> t;
    rep(j, n) if (1 & i >> j) t.pb(p[j]);
    memset(w, 0, sizeof(w));
    w[0][B] = 1;
    rep(k, t.size()) {
      rep(e, -20, 20) {
        w[k + 1][B + e + 1] += w[k][B + e] * t[k];
        w[k + 1][B + e - 1] += w[k][B + e] * (1 - t[k]);
      }
    }
    if (smax(prob, w[t.size()][B])) {
      best = i;
    }
  }
  rep(i, n) if (1 & best >> i) cout << i << ' ';
}

void init(double p[], double q[300][300]) {
  //memset(q, 0, sizeof(q));
  q[0][0] = 1;
  rep(i, n) {
    rep(j, i + 1) if (q[i][j]) {
      q[i + 1][j + 1] += q[i][j] * p[i];
      q[i + 1][j] += q[i][j] * (1 - p[i]);
    }
  }
}

void solve() {
  cin >> n >> m;
  rep(i, n) cin >> p[i];
  sort(p, p + n);
  rep(i, n) ip[i] = p[n - 1 - i];
  memset(l, 0, sizeof(l));
  memset(r, 0, sizeof(r));
  init(p, l);
  init(ip, r);
  double res = 0;
  rep(i, m + 1) {
    double sum = 0;
    rep(j, m / 2 + 1) 
      sum += l[i][j] * r[m - i][m / 2 - j];
    smax(res, sum);
  }
  cout << setprecision(10) << fixed << res << endl;
}

int main() {
  #ifdef _TEST_
  freopen("input.txt", "r", stdin);
  //freopen("out.txt", "w", stdout);
    
  #endif
  int Q; cin >> Q;
  rep(i, Q) {
    cout << "Case " << "#" << i + 1 << ": ";
    solve();
  }
  return 0;
}
