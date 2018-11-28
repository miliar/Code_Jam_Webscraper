#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <set>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <map>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef vector<pii> vii;
typedef vector<string> vs;

void out(vi v) {
  for (int x : v) cerr << x << ' ';
  cerr << endl;
}

void out(vvi v) {
  for (auto x : v) out(x);
  cerr << endl;
}

int main() {
  int T;
  cin >> T;
  for (int test = 1; test <= T; ++test) {
    int n;
    cin >> n;
    vs in(n);
    vvi v0(n, vi(n));
    int c = 0;
    for (int i = 0; i < n; ++i) {
      cin >> in[i];
      for (int j = 0; j < n; ++j) if (in[i][j] == '1') {
        v0[i][j] = 1;
        ++c;
      }
    }
    int res = n*n - c;
//    cerr << test << ' ' << c << endl;
    for (int mask = 0; mask < (1 << (n * n)); ++mask) {
      vvi v = v0;
      bool fail = 0;
      for (int i = 0; i < n; ++i) for (int j = 0; j < n; ++j) {
        bool h = (mask & (1 << (i*n+j))) > 0;
        if (v0[i][j] && !h) fail = 1;
        if (h) v[i][j] = 1;
      }
      if (fail) continue;
      for (int i = 0; !fail && i < n; ++i) {
        vi todo;
        for (int j = 0; j < n; ++j) if (v[i][j]) todo.push_back(j);
        if (todo.empty()) {
          fail = 1;
          break;
        }
        vi ord;
        for (int j = 0; j < n; ++j) if (i != j) ord.push_back(j);
//        if (mask == 281 && i == 0) {out(todo); out(ord);}
        if (ord.size() < todo.size()) continue;
        do {
          fail = 1;
          for (int j = 0; j < todo.size(); ++j) if (!v[ord[j]][todo[j]]) {
            fail = 0;
          }
          //if (mask == 281 && i == 0) {out(ord); cerr << fail << endl;}
        } while (!fail && next_permutation(ord.begin(), ord.end()));
      }
      if (!fail) {
        int cand = __builtin_popcount(mask) - c;
        if (res > cand) {
          res = cand;
//          out(v);
//          cerr << test << ' ' << mask << endl;
        }
      }
    }
    printf("Case #%d: %d\n", test, res);
  }
  return 0;
}
