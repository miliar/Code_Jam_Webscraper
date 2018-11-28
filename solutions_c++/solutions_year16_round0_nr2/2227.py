#include <cstdio>
#include <string>

using namespace std;

void Negate(char& c) { c = (c == '+' ? '-' : '+'); }

int Solve(string s) {
  auto f = [&s](int k) {
    for (size_t i = 0; i < k; ++i) Negate(s[i]);
    k /= 2;
    for (size_t i = 0; i < k; ++i) swap(s[i], s[k - i]);
  };

  int ret = 0;
  const int n = s.size();
  while (ret < n) {
    int k = 1;
    while (k < n && s[k] == s[0]) ++k;
    if (k == n) break;
    // printf("<%s>", s.c_str());
    ++ret, f(k);
    // printf("[%s] %d (%d)\n", s.c_str(), ret, k);
  }
  return ret += (s[0] == '-');
}

int main() {
  int t;
  scanf("%d", &t);
  for (int tc = 0; tc < t; ++tc) {
    char s[101];
    scanf("%s", s);
    printf("Case #%d: %d\n", tc + 1, Solve(s));
  }
  return 0;
}
