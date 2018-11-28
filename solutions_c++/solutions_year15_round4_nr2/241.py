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
#include <sstream>
#include <map>
#include <set>
#include <stdio.h>
#include <assert.h>
#include <ctype.h>
#include <math.h>
#include <time.h>
#include <sys/time.h>
#include <iostream>
#include <iomanip>

using namespace std;

typedef long long LL;

#define FOR(i,n) for(int i = 0;i < n;i++)
#define MP make_pair
#define PB push_back
#define ALL(a) (a).begin(),(a).end()
#define PII pair<int, int>
#define PDD pair<long double,long double>
#define CLEAR(a) memset(a, 0, sizeof(a))
#define prev eruyvuy
#define INF 2000000007
#define next abc
#define y1 uu1
#define y2 uu2
const long double EPS = 1E-11;
const long double PI = acos(-1.0);

using namespace std;

int n;
long double v,x,r,c;
vector<PDD> a;

bool can(long double tm) {
  long double need = v;
  vector<PDD> q;
  bool g = 0;

  FOR(i, n) {
    long double ev = a[i].second * tm;
    if (ev >= need) {
      q.push_back(MP(a[i].first, need));
      g = 1;
      break;
    } else {
      q.push_back(MP(a[i].first, ev));
      need -= ev;
    }
  }

  if (!g)
    return false;

  long double tp = 0;
  FOR(i, q.size()) tp += q[i].first * q[i].second;
  tp /= v;

  if (tp > x + EPS) return false;

  q.clear();
  g = 0;
  need = v;

  for (int i = n-1; i >= 0; i--) {
    long double ev = a[i].second * tm;
    if (ev >= need) {
      q.push_back(MP(a[i].first, need));
      g = 1;
      break;
    } else {
      q.push_back(MP(a[i].first, ev));
      need -= ev;
    }
  }

  if (!g)
    return false;

  tp = 0;
  FOR(i, q.size()) tp += q[i].first * q[i].second;
  tp /= v;

  if (tp < x - EPS) return false;

  return true;
}

void solve() {
  cin >> n >> v >> x;

  a.clear();
  FOR(i, n) {
    cin >> r >> c;
    a.push_back(MP(c,r));
  }
  sort(ALL(a));

  //cout << "HERE " << a[0].first << ' ' << a.back().first << ' ' << x << endl;

  if (a[0].first > x+EPS) {
    cout << "IMPOSSIBLE" << endl;
    return;
  }

  if (a.back().first < x-EPS) {
    cout << "IMPOSSIBLE" << endl;
    return;
  }

  //cout << "HERE" << endl;

  long double l = 0;
  long double r = 20000.0 * 20000.0;

  while (r - l > EPS) {
    long double mid = (r+l)/2;
    if (can(mid)) {
      r = mid;
    } else {
      l = mid;
    }
  }

  cout << fixed << setprecision(9) << (r+l)/2 << endl;
}

int main() {
  int t;
  cin >> t;

  FOR(tt,t) {
    cout << "Case #" << tt+1 << ": ";
    solve();
  }
  return 0;
}
