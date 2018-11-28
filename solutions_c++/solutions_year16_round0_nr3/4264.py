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

string generate(int length) {
  assert(length >= 2);
  string result;
  FOR(i, 0, length - 2) {
    result += rand() % 2 + '0';
  }
  return "1" + result + "1";
}

ll interpret(string jamcoin, int base) {
  ll result = 0;
  FOR(i, 0, Size(jamcoin)) {
    result *= base;
    result += jamcoin[i] - '0';
  }
  return result;
}

ll least_divisor(ll n) {
  if (n < 2) {
    return -1;
  }
  for (int i = 2; i * i <= n && i < 100; i++) {
    if (n % i == 0) {
      return i;
    }
  }
  return -1;
}

bool is_prime(ll n) {
  return least_divisor(n) == -1;
}

bool check(string jamcoin) {
  FOR(base, 2, 11) {
    if (is_prime(interpret(jamcoin, base))) {
      return false;
    }
  }
  return true;
}

void print_jamcoin(string jamcoin) {
  cout << jamcoin;
  FOR(base, 2, 11) {
    cout << " " << least_divisor(interpret(jamcoin, base));
  }
  cout << endl;
}

int main() {
  srand(time(NULL));
  int t;
  cin >> t;
  FOR(test_number, 1, t + 1) {
    cout << "Case #" << test_number << ":" << endl;
    int n, j;
    cin >> n >> j;
    set<string> jamcoins;
    while (Size(jamcoins) < j) {
      string jamcoin = generate(n);
      if (check(jamcoin)) {
        if (!in(jamcoins, jamcoin)) {
          print_jamcoin(jamcoin);
        }
        jamcoins.insert(jamcoin);
      }
    }
  }
	return 0;
}
