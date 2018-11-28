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

int solve(string input) {
  int score = 0;
  vector<int> st;
  FOR(i, 0, Size(input)) {
    st.pb(input[i]);
    while (Size(st) >= 2 && st[Size(st) - 1] == st[Size(st) - 2]) {
      st.pop_back();
      st.pop_back();
      score += 10;
    }
  }
  return score + Size(st) / 2 * 5;
}

int main() {
  int t;
  cin >> t;
  FOR(test_number, 1, t + 1) {
    cout << "Case #" << test_number << ": ";
    string input;
    cin >> input;
    cout << solve(input) << endl;
  }
	return 0;
}
