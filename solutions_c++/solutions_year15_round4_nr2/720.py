#include <string>
#include <vector>
#include <cstring>
#include <cmath>
#include <utility>
#include <algorithm>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <list>
#include <iomanip>
#include <ctime>
#include <cassert>
#include <stack>
#include <unordered_map>
#include <unordered_set>

#define what_is(x) cout << #x << " is " << x << endl;

using namespace std;

typedef long long ll;

int main () {
  std::ios::sync_with_stdio(false);
  int t;
  cin >> t;
  cout << fixed << setprecision(10);
  for (int i = 0; i < t; i++) {
    int n;
    double V, T;
    cin >> n >> V >> T;
    vector<double> r(n), t(n);
    for (int i = 0; i < n; i++) {
      cin >> r[i] >> t[i];
    }
    if (n == 1) {
      if (T != t[0]) {
	cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
      }
      else {
	cout << "Case #" << i + 1 << ": " << V / r[0] << endl;
      }
    }
    else {
      if (t[0] > t[1]) {
	swap(t[0], t[1]);
	swap(r[0], r[1]);
      }
      if (t[0] == t[1]) {
	if (T != t[0]) {
	  cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
	}
	else {
	  cout << "Case #" << i + 1 << ": " << V / (r[0] + r[1]) << endl;
	}
      }
      else {
	if (T < t[0] || T > t[1]) {
	  cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
	}
	else {
	  double v1 = (V * T - V * t[0]) / (t[1] - t[0]);
	  double v0 = V - v1;
	  cout << "Case #" << i + 1 << ": " << max(v1 / r[1], v0 / r[0]) << endl;
	}
      }
    }
  }
  return 0;
}
