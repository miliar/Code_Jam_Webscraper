#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <map>
#include <set>

#define LOCAL "input.txt"
#define NOT_LOCAL "tests.in"
typedef long long ll;

using namespace std;

bool isPrime(ll num) {
  for (ll div = 2; div * div <= num; ++div) {
    if (num % div == 0) {
      return false;
    }
  }
  return true;
}

vector<ll> getNums(ll str) {
  vector<ll> res;
  for (int base = 2; base <= 10; ++base) {
    ll num = str;
    ll cur = 0;
    ll power = 1;

    while (num > 0) {
      cur += num % 2 * power;
      num /= 2;
      power *= base;
    }

    res.push_back(cur);
  }

  return res;
}

int main() {
  ios::sync_with_stdio(false);
  freopen(NOT_LOCAL, "r", stdin);
  freopen("output.txt", "w", stdout);

  int tests;
  cin >> tests;

  for (int test = 1; test <= tests; ++test) {

    int n, m, s;
    cin >> n >> m >> s;
    printf("Case #%d: ", test);
    for (int i = 1; i <= n; ++i) {
      cout << i << " ";
    }
    cout << endl;

  }

  return 0;
}