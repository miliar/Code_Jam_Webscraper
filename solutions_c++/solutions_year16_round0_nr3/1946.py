#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cassert>
#include <iomanip>
using namespace std;

#define INF 1e+9
#define mp make_pair
#define lint long long
#define pii pair<int, int>

void out(vector<bool> v1, vector<lint> v2) {
  for (bool i: v1) {
    cout << i;
  }
  for (int i: v2) {
    cout << " " << i;
  }
  cout << "\n";
}

pair<vector<bool>, vector<lint>> gen(int n, int len) {
  vector<bool> r2;
  for (int b = n; b > 0; b /= 2) {
    r2.push_back(b%2);
  }
  std::reverse(r2.begin(), r2.end());
  r2.push_back(1);

  vector<bool> num(2 * len);
  for (int i = 0; i < r2.size(); i++) {
    num[i] = r2[i];
    num[n - r2.size() + i] = r2[i];
  }
  vector<lint> divs;

  for (int base = 2; base <= 10; base++) {
    lint v = 0;
    for (int i = 0; i < r2.size(); i++) {
      v = v * base + r2[i];
    }
    divs.push_back(v);
  }
  return mp(num, divs);
}

int main() {
  ios_base::sync_with_stdio(false);
  cout << setprecision(10) << fixed;
  int t; cin >> t;
  for (int ii = 0; ii < t; ii++) {
    int n, lim;
    cin >> n;
    cin >> lim;
    cout << "Case #1:\n";
    for (int i = 0; i < lim; i++) {
      auto r = gen(i, n);
      out(r.first, r.second);
    }
  }
}
