#include <iostream>
#include <cstdio>
#include <cstring>
#include <map>
using namespace std;

map<long long, int> mp;
char str[128];

int main() {
  int cases;
  scanf("%d", &cases);
  for (int T = 1; T <= cases; ++T) {
    int n;
    scanf("%d", &n);
    mp.clear();
    int cnt[10];
    for (int i = 0; i < 10; ++i) {
      cnt[i] = 0;
    }
    bool hasAnswer = false;
    int j = 1;
    for (; ; ++j) {
      long long m = (long long)n * j;
      if (mp.count(m)) {
        break;
      }
      sprintf(str, "%lld", m);
      int len = strlen(str);
      for (int i = 0; i < len; ++i) {
        ++cnt[str[i] - '0'];
      }
      bool satisfied = true;
      for (int i = 0; i < 10; ++i) {
        if (cnt[i] == 0) {
          satisfied = false;
          break;
        }
      }
      if (satisfied) {
        hasAnswer = true;
        break;
      }
      mp[m] = 1;
    }
    printf("Case #%d: ", T);
    if (hasAnswer) {
      printf("%lld\n", (long long)n * j);
    } else {
      puts("INSOMNIA");
    }
  }
}