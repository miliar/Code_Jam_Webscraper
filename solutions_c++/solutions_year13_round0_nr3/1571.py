#include <iostream>
#include <vector>
#include <stdio.h>
#include <math.h>
using namespace std;
long long GetInvert(long long value, int leading_zero, bool odd) {
  char s[20];
  sprintf(s, "%lld", value);
  char r[20];
  int pos = 0;
  int ls = strlen(s);
  for (int i = 0; i < ls - (leading_zero == 0 ? odd : 0); ++i) {
    r[pos++] = s[ls - 1 - i];
  }
  for (int i = 0; i < leading_zero * 2 - odd; ++i) r[pos++] = '0';
  for (int i = 0; i < ls; ++i) r[pos++] = s[i];
  r[pos++] = 0;
  long long ans;
  sscanf(r, "%lld", &ans);
  return ans;
}

bool check_par(long long value) {
  char s[20];
  sprintf(s, "%lld", value);
  int ls = strlen(s);
  for (int i = 0; i < ls / 2; ++i) {
    if (s[i] != s[ls - 1 - i]) return false;
  }
  return true;
}

std::vector<long long> ans;
void PrintAll() {
  // { long long i = 21;
   for (long long i = 1; i < 100000; ++i) {
    if (i % 10 == 0) continue;
    char buf[20];
    sprintf(buf, "%lld", i);
    int ln = strlen(buf);
    for (int x = 0; x + ln < 5; ++x) {
      long long num = GetInvert(i, x, false);
      long long num2 = num * num;
      if (num <= 100000000 && check_par(num2)) {
        ans.push_back(num2);
      }
      num = GetInvert(i, x, true);
      num2 = num * num;
      if (num <= 100000000 && check_par(num2)) {
        ans.push_back(num2);
      }
    }
  }
  std::sort(ans.begin(), ans.end());
//  for (int i = 0; i < ans.size(); ++i) {
//    printf("%lld\n", ans[i]);
//  }
}

int Count(long long low_bound, long long up_bound) {
  int result = 0;
  for (int i = 0; i < ans.size(); ++i) {
    if (ans[i] >= low_bound && ans[i] <= up_bound) ++result;
  }
  return result;
}
int main(int argc, char** argv) {
  PrintAll();
  int tc;
  scanf("%d", &tc);
  for (int cas= 1; cas <= tc; ++cas) {
    long long low_bound;
    long long up_bound;
    scanf("%lld%lld", &low_bound, &up_bound);
    printf("Case #%d: %d\n", cas, Count(low_bound, up_bound));
  }
  return 0;
}
