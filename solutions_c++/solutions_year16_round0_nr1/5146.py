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

const int FINAL_MASK = (1 << 10) - 1;

int digit_mask(int number) {
  if (number == 0) {
    return 1;
  }
  int mask = 0;
  while (number) {
    mask |= 1 << (number % 10);
    number /= 10;
  }
  return mask;
}

int sleep_number(int number) {
  int mask = 0;
  FOR(c, 1, 1000) {
    mask |= digit_mask(number * c);
    if (mask == FINAL_MASK) {
      return number * c;
    }
  }
  return -1;
}

int main() {
  int t;
  cin >> t;
  FOR(test_number, 1, t + 1) {
    int n;
    cin >> n;
    int result = sleep_number(n);
    cout << "Case #" << test_number << ": ";
    if (result == -1) {
      cout << "INSOMNIA" << endl;
    } else {
      cout << result << endl;
    }
  }
	return 0;
}
