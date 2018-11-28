#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <limits>
#include <numeric>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()
#define PROBLEM_ID "C"

#pragma comment(linker,"/STACK:32000000")

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<vvb> vvvb;
typedef long double ld;
typedef pair<int, int> pii;
typedef long long ll;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<vvl> vvvl;
typedef pair<ll, ll> pll;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<vvd> vvvd;

double Dist(const vi& a, const vi& b) {
  double res = 0;
  for (int i = 0; i < a.size(); ++i) {
    res += (a[i] - b[i]) * (a[i] - b[i]);
  }
  return sqrt(res);
}

bool CanTravel(const vector<vector<double> >& dist, double bound) {
  int s = 0;
  int n = dist.size();
  vector<bool> done(n, false);
  queue<int> q;
  q.push(s);
  done[s] = true;
  while (!q.empty()) {
    int cur = q.front();
    if (cur == 1) {
      return true;
    }
    q.pop();
    for (int i = 0; i < n; ++i) {
      if (dist[cur][i] < bound + 1e-10 && !done[i]) {
        done[i] = true;
        q.push(i);
      }
    }
  }
  return false;
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int tests;
  cin >> tests;
  for (int test_index = 0; test_index < tests; ++test_index) {
    int n, s;
    cin >> n >> s;
    vvi x(n, vi(3));
    vvi v(n, vi(3));
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < 3; ++j) {
        cin >> x[i][j];
      }
      for (int j = 0; j < 3; ++j) {
        cin >> v[i][j];
      }
    }
    double low = 0;
    double high = 0;
    vector< vector<double> > dist(n, vector<double>(n));
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        dist[i][j] = Dist(x[i], x[j]);
        high = max(high, dist[i][j]);
      }
    }
    while (low + 1e-5 < high) {
      double med = (low + high) / 2;
      if (CanTravel(dist, med)) {
        high = med;
      } else {
        low = med;
      }
    }
    double result = high;
    cout << "Case #" << (test_index + 1) << ": ";
    cerr << "Case #" << (test_index + 1) << ": ";
    printf("%.10lf\n", result);
    fprintf(stderr, "%.10lf\n", result);
  }
  return 0;
}
