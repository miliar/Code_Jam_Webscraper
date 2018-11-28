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

int minimum_flips(string pancakes) {
  pancakes += "+";
  int flips = 0;
  FOR(i, 0, Size(pancakes) - 1) {
    if (pancakes[i] != pancakes[i + 1]) {
      flips++;
    }
  }
  return flips;
}

int main() {
  int t;
  cin >> t;
  FOR(test_number, 1, t + 1) {
    string pancakes;
    cin >> pancakes;
    cout << "Case #" << test_number << ": " << minimum_flips(pancakes) << endl;
  }
	return 0;
}
