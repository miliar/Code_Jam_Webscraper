#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <map>
#include <set>

#define LOCAL
#define input_l "input.txt"
#define input_nl "cur1.in"
typedef long long ll;

using namespace std;

long long count(long long num) {
  set<int> digits;
  long long res = 0;
  long long cur_num = 0;
  while (digits.size() < 10) {
    cur_num += num;
    long long cur = cur_num;
    while (cur > 0) {
      digits.insert(cur % 10);
      cur /= 10;
    }
  }
  return cur_num;
}

int main() {
  ios::sync_with_stdio(false);
#ifdef LOCAL
  freopen(input_nl, "r", stdin);
  freopen("output.txt", "w", stdout);
#endif

  int tests;
  cin >> tests;
  int max_res = 0;

  for (int test = 1; test <= tests; ++test) {

    int num;
    cin >> num;
    printf("Case #%d: ", test);
    if (num == 0) {
      printf("INSOMNIA\n");
    }
    else {
      printf("%lld\n", count(num));
    }

  }

  return 0;
}