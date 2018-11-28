#include <cstdio>
#include <iostream>
#include <string>

inline int getint() {
  int x;
  scanf("%d", &x);
  return x;
}

int main() {
  int ttt = getint();
  for (int tt = 0; tt < ttt; ++tt) {
    std::string str;
    std::cin >> str;
    int ret = 0;
    for (int i = 1; i < str.size(); ++i) {
      if (str[i] != str[i - 1]) {
        ++ret;
      }
    }
    if (str.back() == '-') {
      ++ret;
    }
    printf("Case #%d: %d\n", tt + 1, ret);
  }
}
