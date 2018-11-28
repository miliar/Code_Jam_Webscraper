#include <cstdio>
#include <algorithm>

using namespace std;

const int N = 1e3+10;

char s[N];

inline int solve () {
  int n;
  scanf ("%d %s", &n, s);

  int sum = 0,ans = 0;
  for (int i = 0;i <= n;i ++) {
    if (sum < i) {
      ans += i-sum;
      sum += i-sum;
    }
    sum += s[i]-'0';
  }
  return ans;
}

int main () {
  int t;
  scanf ("%d", &t);

  for (int i = 1;i <= t;i ++) {
    printf ("Case #%d: %d\n", i, solve ());
  }
}
