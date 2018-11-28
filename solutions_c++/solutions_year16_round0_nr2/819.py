#include <cstdio>

#include <iostream>
#include <string>

using std::string;

string apply(const string& s, int len) {
  string res = s;
  for (int i = 0; i < len; ++i) {
    res[i] = s[len - i - 1] == '0' ? '1' : '0';
  }
  return res;
}

bool isFinal(const string& s) {
  return std::count(s.begin(), s.end(), '0') == 0;
}

int slow(const string& s) {
  if (isFinal(s)) {
    return 0;
  }
  int res = INT_MAX;
  for (int len = 1; len <= s.size(); ++len) {
    auto next = apply(s, len);
    if (next != s) {
      res = std::min(res, 1 + slow(next));
    }
  }
  return res;
}

int solve(const string& s) {
  int lastZero = s.size() - 1;
  while (lastZero >= 0 && s[lastZero] == '1') {
    --lastZero;
  }
  if (lastZero == -1) {
    return 0;
  }
  if (s[0] == '0') {
    return solve(apply(s, lastZero + 1)) + 1;
  }
  int prevOne = lastZero;
  while (s[prevOne] == '0') {
    // No need for bounds checking as s[0] == '1'.
    --prevOne;
  }
  return solve(apply(s, prevOne + 1)) + 1;
}

string binarize(const string& s) {
  string res;
  for (char c: s) {
    res += c == '+' ? '1' : '0';
  }
  return res;
}

int main() {
  int T;
  std::cin >> T;
  for (int t = 1; t <= T; ++t) {
    string s;
    std::cin >> s;
    printf("Case #%d: %d\n", t, solve(binarize(s)));
  }
//   string s;
//   int n;
//   while (std::cin >> s) {
//     std::cout << solve(s) << "\n";
//   }
}
