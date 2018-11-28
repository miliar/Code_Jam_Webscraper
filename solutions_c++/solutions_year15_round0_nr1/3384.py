#include <cstdio>
#include <cstdlib>
using namespace std;

int n, num[1005];
char str[1005];

int solve() {
  int cnt = 0, inv = 0;
  for (int i = 0; i <= n; i++) {
    num[i] = str[i] - '0';
    if (cnt < i) inv += i - cnt, cnt += i - cnt;
    cnt += num[i];
  }
  return inv;
}

int main() {
  int t;
  scanf("%d", &t);
  for (int i=0 ; i<t ; i++) {
    scanf("%d", &n);
    scanf("%s", str);
    printf("Case #%d: %d\n", i + 1, solve());
  }
}