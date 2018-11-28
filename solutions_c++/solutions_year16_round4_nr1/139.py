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

string best(string a, string b) {
  return a < b ? a + b : b + a;
}

string beginning(char last, int rounds) {
  if (rounds == 0) {
    return string(1, last);
  }
  pair<char, char> prev;
  if (last == 'R') {
    prev = mk('R', 'S');
  }
  if (last == 'P') {
    prev = mk('P', 'R');
  }
  if (last == 'S') {
    prev = mk('S', 'P');
  }
  return best(beginning(prev.first, rounds - 1), beginning(prev.second, rounds - 1));
}

bool verify(string str, int r, int p, int s) {
  return count(all(str), 'R') == r &&
    count(all(str), 'P') == p &&
    count(all(str), 'S') == s;
}

string solve(int n, int r, int p, int s) {
  string chars = "RPS";
  string best;
  FOR(i, 0, 3) {
    string result = beginning(chars[i], n);
    if (verify(result, r, p, s)) {
      if (best == "" || result < best) {
        best = result;
      }
    }
  }
  return best == "" ? "IMPOSSIBLE" : best;
}

int main() {
  int t;
  cin >> t;
  FOR(test_number, 1, t + 1) {
    int n, r, p, s;
    cin >> n >> r >> p >> s;
    string result = solve(n, r, p, s);
    cout << "Case #" << test_number << ": " << result << endl;
  }
	return 0;
}
