#include <cassert>
#include <complex>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <iostream>
#include <iterator>
#include <limits>
#include <numeric>
#include <sstream>
#include <utility>

#include <algorithm>
#include <bitset>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

#include <memory.h>
using namespace std;

#pragma comment(linker, ”/STACK:108777216“)

#define Pi 3.141592653589793
#define all(c) (c).begin(), (c).end()
typedef long long ll;

int ri() {
  int res; scanf("%d", &res); return res;
}

class timer {
public:
  timer() : t_(clock()) {}
  void start() { t_ = clock(); }
  float elapsed() { return float(clock() - t_) / CLOCKS_PER_SEC; }
private:
  clock_t t_;
};

int eval1(const vector<double>& a, const vector<double>& b) {
  int res = 0;
  set<double> bb(all(b));
  for (int i = 0; i < a.size(); ++i) {
    if (a[i] > *bb.begin()) {
      ++res;
      bb.erase(bb.begin());
    } else {
      bb.erase(*bb.rbegin());
    }
  }
  return res;
}

int eval2(const vector<double>& a, const vector<double>& b) {
  set<double> bb(all(b));
  for (int i = 0; i < a.size(); ++i) {
    set<double>::iterator it = bb.lower_bound(a[i]);
    if (it == bb.end()) {
      return bb.size();
    } else {
      bb.erase(it);
    }
  }
  return 0;
}

int main() {
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);

  int T; cin >> T;
  for (int qq = 1; qq <= T; ++qq) {
    cout << "Case #" << qq << ": ";
    int n; cin >> n;
    vector<double> a(n), b(n);
    for (int i = 0; i < n; ++i)
      cin >> a[i];
    for (int i = 0; i < n; ++i)
      cin >> b[i];
    sort(all(a));
    sort(all(b));
    cout << eval1(a, b) << " " << eval2(a, b) << endl;
  }

  return 0;
}
