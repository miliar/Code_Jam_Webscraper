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

int main() {
  ios::sync_with_stdio(false);
  freopen(NOT_LOCAL, "r", stdin);
  freopen("output.txt", "w", stdout);

  int tests;
  cin >> tests;

  for (int test = 1; test <= tests; ++test) {

    string str;
    cin >> str;
    int ans = 0;
    for (int i = 1; i < str.size(); ++i) {
      if (str[i - 1] != str[i]) {
        ++ans;
      }
    }
    if (str.back() == '-') {
      ++ans;
    }

    printf("Case #%d: %d\n", test, ans);

  }

  return 0;
}