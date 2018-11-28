#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
#include <string>
#include <cstdlib>

#define BUG(x) cerr << #x << ": " << x << endl;
#define FOR(i, n) for (int i = 0; i < n; ++i)
#define FORV(v, i) for (int i = 0; i < int(v.size()); ++i)
#define TR(v, it) for ((typeof v.begin()) it = v.begin(); it != v.end(); ++it)
#define X first
#define Y second

using namespace std;

const int INF = 2e9;

typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef vector<vd> vvd;
typedef map<int, int> mii;
typedef set<int> si;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<string> vs;
typedef vector<si> vsi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;

int main() {
  ios_base::sync_with_stdio(false);
  srand(231234);
  int t;
  cin >> t;
  for (int tt = 1; tt <= t; ++tt) {
    cout << "Case #" << tt << ": ";
    int r, c;
    cin >> r >> c;
    vsi F(r), C(c);
    vs M(r);
    FOR (i, r) cin >> M[i];
    FOR (i, r) FOR (j, c) {
      if (M[i][j] != '.') {
        F[i].insert(j);
        C[j].insert(i);
      }
    }
    bool poss = true;
    int q = 0;
    FOR (i, r) FOR (j, c) {
      if (M[i][j] != '.') {
        bool ok = false;
        if (F[i].upper_bound(j) != F[i].end()) {
          ok = true;
          if (M[i][j] == '>') continue;
        }
        if (F[i].lower_bound(j) != F[i].begin()) {
          ok = true;
          if (M[i][j] == '<') continue;
        }
        if (C[j].upper_bound(i) != C[j].end()) {
          ok = true;
          if (M[i][j] == 'v') continue;
        }
        if (C[j].lower_bound(i) != C[j].begin()) {
          ok = true;
          if (M[i][j] == '^') continue;
        }
        if (ok) ++q;
        else poss = false;
      }
    }
    if (poss) cout << q << endl;
    else cout << "IMPOSSIBLE" << endl;
  }
  
  
}