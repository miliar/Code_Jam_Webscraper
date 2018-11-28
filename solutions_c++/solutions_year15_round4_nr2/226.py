#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

#define DEBUG(x) cerr << #x << " = " << (x) << endl

#define FR first
#define SC second

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<ld, ld> PLL;

template <class Ta, class Tb> inline Tb cast(Ta a) {
  stringstream ss;
  ss << a;
  Tb b;
  ss >> b;
  return b;
};

const ld EPS = 1e-9;

ld max_volume(const vector<PLL>& cr, ld t) {
  int n = int(cr.size());
  vector<PLL> cv(n);
  for (int i = 0; i < n; ++i) {
    cv[i].FR = cr[i].FR;
    cv[i].SC = cr[i].SC * t;
  }
  
  ld temp_sum = 0.0, vol_sum = 0.0;
  for (int i = 0; i < n; ++i) {
    temp_sum += cv[i].FR * cv[i].SC;
    vol_sum += cv[i].SC;
  }
  ld total_temp = temp_sum / vol_sum;
  bool rev = false;
  if (total_temp < -EPS) {
    rev = true;
    reverse(cv.begin(), cv.end());
  }

  ld temp = 0.0, vol = 0.0;
  for (int i = 0; i < n; ++i) {
    ld next_temp = (vol * temp + cv[i].SC * cv[i].FR) / (vol + cv[i].SC); 
    if ((!rev && next_temp > EPS) || (rev && next_temp < -EPS)) {
      ld vol_wanted = -vol * temp / cv[i].FR;
      return vol + vol_wanted;
    }
    vol += cv[i].SC;
    temp = next_temp;
  }
  return vol;
}

int main() {
  ios_base::sync_with_stdio(false);
  cout.setf(ios::fixed);
  cout.precision(8);
  int T;
  cin >> T;
  for (int ca = 1; ca <= T; ++ca) {
    int n;
    ld v, x;
    cin >> n >> v >> x;
    vector<PLL> cr(n);
    for (int i = 0; i < n; ++i) {
      cin >> cr[i].SC >> cr[i].FR;
      cr[i].FR -= x;  // Target temperature is now 0.
    }
    sort(cr.begin(), cr.end());
    bool all_below_zero = true;
    bool all_above_zero = true;
    for (int i = 0; i < n; ++i) {
      if (cr[i].FR > -EPS) all_below_zero = false;
      if (cr[i].FR < EPS) all_above_zero = false;
    }
    cout << "Case #" << ca << ": ";
    if (all_below_zero || all_above_zero) {
      cout << "IMPOSSIBLE" << endl;
      continue;
    }

    ld lo = 0.0, hi = 1e99;
    for (; hi - lo > EPS;) {
      ld m = lo + (hi - lo) / 2.0;
      ld mx_vol = max_volume(cr, m);
      if (mx_vol < v) lo = m;
      else hi = m;
    }
    cout << (lo + hi) / 2.0 << endl;
  }
}

