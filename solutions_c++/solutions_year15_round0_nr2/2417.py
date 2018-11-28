#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

const int N = 1e3+10;

int x[N];

inline int solve () {
  int n;
  scanf ("%d", &n);

  for (int i = 0;i < n;i ++) {
    scanf ("%d", &x[i]);
  }

  int ans = -1u/2;
  for (int i = 1;i <= 1000;i ++) {
    int sum = 0;
    for (int j = 0;j < n;j ++) {
      sum += (x[j]-1)/i;
    }
    ans = min (ans, sum+i);
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

