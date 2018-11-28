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

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int N = 16;
  int J = 50;
  vector<string> jamcoins;
  vvi divisors;
  for (int mask = (1 << (N - 1)) + 1; mask < (1 << N); mask += 2) {
    bool is_jamcoin = true;
    vector<int> divs;
    for (int base = 2; base <= 10; ++base) {
      ll x = 0;
      for (int j = N - 1; j >= 0; --j) {
        x = x * base + ((mask >> j) & 1);
      }
      bool is_prime = true;
      for (ll i = 2; i * i <= x; ++i) {
        if (x % i == 0) {
          is_prime = false;
          divs.push_back(i);
          break;
        }
      }
      if (is_prime) {
        is_jamcoin = false;
        break;
      }
    }
    if (is_jamcoin) {
      divisors.push_back(divs);
      string s = "";
      for (int i = 0; i < N; ++i) {
        s += ('0' + ((mask >> (N - i - 1)) & 1));
      }
      jamcoins.push_back(s);
      if (jamcoins.size() == J) {
        break;
      }
    }
  }
  cout << "Case #1:" << endl;
  for (int j = 0; j < jamcoins.size(); ++j) {
    cout << jamcoins[j];
    for (int k = 0; k < divisors[j].size(); ++k) {
      cout << ' ' << divisors[j][k];
    }
    cout << endl;
  }
  return 0;
}
