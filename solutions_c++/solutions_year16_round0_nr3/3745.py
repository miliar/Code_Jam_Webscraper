#include <algorithm>
#include <bitset>
#include <cmath>
#include <iostream>
#include <iterator>
#include <string>
#include <vector>
#include <utility>

using namespace std;

long long convertToBase(int n, int b) {
  long long N = 0;
  long long current = 1;
  while (n > 0) {
    if (n % 2 == 1) {
      N += current;
    }
    current *= b;
    n >>= 1;
  }
  return N;
}

string convertToBinaryString(unsigned int p) {
  string s;
  while (p > 0) {
    s.push_back(p % 2 == 1 ? '1' : '0');
    p >>= 1;
  }
  reverse(s.begin(), s.end());
  return s;
}

long long findDivisor(long long n) {
  for (int d = 3; d <= sqrt(n); d += 2) {
    if (n % d == 0) return d;
  }
  return n;
}

vector<pair<unsigned int, vector<long long>>> findCoins(int N, int J) {
  vector<pair<unsigned int, vector<long long>>> coins; coins.reserve(J);
  unsigned int n = 1 + (1 << (N - 1));
  for (unsigned int m = 0; m < (1 << (N - 1)) && coins.size() < J; m += 2) {
    unsigned int p = n + m;
    vector<long long> divisors;
    for (int b = 2; b <= 10; ++b) {
      long long q = convertToBase(p, b);
      long long d = findDivisor(q);
      if (q != d) divisors.push_back(d);
    }
    if (divisors.size() == 9) coins.emplace_back(p, divisors);
  }
  return coins;
}

int main(int argc, char *argv[]) {
  ios::sync_with_stdio(false); cin.tie(NULL);
  int T; cin >> T;
  for (int t = 0; t < T; ++t) {
    int N, J;
    cin >> N >> J;              // string length, number of coins
    vector<pair<unsigned int, vector<long long>>> coins = findCoins(N, J);
    cout << "Case #" << (t + 1) << ": " << '\n';
    for (pair<unsigned int, vector<long long>> coin : coins) {
      cout << convertToBinaryString(coin.first) << ' ';
      copy(coin.second.begin(), coin.second.end() - 1, ostream_iterator<int>(cout, " "));
      cout << coin.second.back() << '\n';
    }
  }
  cout << flush;
  return 0;
}
