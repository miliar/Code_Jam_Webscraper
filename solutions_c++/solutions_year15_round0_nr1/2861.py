#include <cstdio>

using namespace std;

int main() {
  int t, sm, ans, sum;
  char s[1010];
  scanf("%d", &t);
  for(int tc = 1; tc <= t; tc++) {
    sum = ans = 0;
    scanf("%d %s", &sm, s);
    for(int i = 0; i<=sm; i++) {
      if(i>sum && s[i]>'0') {
        ans += i - sum;
        sum = i;
      }
      sum += s[i]-'0';
    }
    printf("Case #%d: %d\n", tc, ans);
  }
  return 0;
}