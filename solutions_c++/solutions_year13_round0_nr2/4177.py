#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <ctime>
#include <cmath>
#include <iostream>

using namespace std;

#define pb push_back
#define mp make_pair
#define x first
#define y second
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define sz(a) (int)((a).size())
#define all(a) (a).begin(), (a).end()

typedef long long ll;
typedef long double ld;
typedef pair <int, int> pii;

vector<string> outcomes = {
  "NO",
  "YES"
};

int f(const vector<vector<int> > &a,
      int x0, int y0, int x1, int y1) {
  int res = 0;
  for (int i = x0; i <= x1; ++i)
    for (int j = y0; j <= y1; ++j)
      res = max(res, a[i][j]);
  return res;
}

int solve(const vector<vector<int> > &a) {
  int w = a.size(), h = a[0].size();

  for (int i = 0; i < w; ++i) {
    for (int j = 0; j < h; ++j) {
      int x = a[i][j];
      if (x < f(a, i, 0, i, h - 1) &&
          x < f(a, 0, j, w - 1, j)) {
        return 0;
      }
    }
  }

  return 1;
}

int main() {
  int t;
  cin >> t;
  for (int q = 1; q <= t; ++q) {
    int w, h;
    cin >> w >> h;
    
    vector<vector<int> > a(w);
    for (int i = 0; i < w; ++i) {
      a[i].resize(h);
      for (int j = 0; j < h; ++j) {
        cin >> a[i][j];
      }
    }

    cout << "Case #" << q << ": " << outcomes[solve(a)] << endl;
  }

  return 0;
}
