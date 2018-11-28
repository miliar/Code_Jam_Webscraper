#include <algorithm>
#include <iostream>
#include <valarray>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <complex>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <ctime>
#include <cmath>
#include <queue>
#include <deque>
#include <map>
#include <set>

using namespace std;

#define FOREACH(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define FOR(i, a, n) for (int i = (a); i < int(n); ++i)
#define error(x) cout << #x << " = " << (x) << endl;
#define all(n) (n).begin(), (n).end()
#define Size(n) ((int)(n).size())
#define mk make_pair
#define pb push_back

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

template <class P, class Q> void smin(P &a, Q b) { if (b < a) a = b; }
template <class P, class Q> void smax(P &a, Q b) { if (b > a) a = b; }
template <class P, class Q> bool in(const P &a, const Q &b) { return a.find(b) != a.end(); }

const int MAXN = 128;

int n, size[MAXN];
bool is_basic[MAXN];
vector<int> children[MAXN];
string type;

void calculate_sizes(int v) {
  size[v] = 1;
  FOR(i, 0, Size(children[v])) {
    int next = children[v][i];
    calculate_sizes(next);
    size[v] += size[next];
  }
}

string generate_random() {
  vector<int> roots;
  FOR(i, 0, n) {
    if (is_basic[i]) {
      roots.pb(i);
    }
  }
  string result = "";
  while (!roots.empty()) {
    int total_size = 0;
    FOR(i, 0, Size(roots)) {
      total_size += size[roots[i]];
    }
    int position = random() % total_size;
    int selected = 0;
    while (position >= size[roots[selected]]) {
      position -= size[roots[selected]];
      selected++;
    }
    int node = roots[selected];
    roots.erase(find(all(roots), node));
    FOR(i, 0, Size(children[node])) {
      roots.pb(children[node][i]);
    }
    result += type[node];
  }
  return result;
}

void solve_pattern(string pattern) {
  int count = 0;
  int total = 0;
  FOR(i, 0, 3000) {
    string random_string = generate_random();
    // cout << random_string << endl;
    if (random_string.find(pattern) != random_string.npos) {
      count++;
    }
    total++;
  }
  double ratio = 1. * count / total;
  cout << fixed << setprecision(5);
  cout << " " << ratio;
}

void solve() {
  FOR(i, 0, MAXN) {
    children[i] = vector<int>();
    size[i] = 0;
    is_basic[i] = true;
  }
  cin >> n;
  FOR(i, 0, n) {
    int p;
    cin >> p;
    p--;
    if (p >= 0) {
      is_basic[i] = false;
      children[p].pb(i);
    }
  }
  FOR(i, 0, n) {
    if (is_basic[i]) {
      calculate_sizes(i);
    }
  }
  cin >> type;
  int m;
  cin >> m;
  while (m--) {
    string pattern;
    cin >> pattern;
    solve_pattern(pattern);
  }
  cout << endl;
}

int main() {
  int t;
  cin >> t;
  FOR(test_number, 1, t + 1) {
    cout << "Case #" << test_number << ":";
    solve();
  }
	return 0;
}
