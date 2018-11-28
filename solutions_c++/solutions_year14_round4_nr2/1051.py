#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
const int nmax = 1000 + 18;

int n, a[nmax], p[nmax], pp[nmax];
int ans;
int base;

// int getf(int i, int j, int k, int l)
// {
//   if (i < j || j < 0) return 1000000000;
//   return f[i][j] + (k > l ? k - l : l - k);
// }

bool cmpor(int i, int j)
{
  return a[i] < a[j];
}

int main()
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int T;
  scanf("%d", &T);
  for (int cases = 1; cases <= T; ++cases) {
    ans = 0;
    printf("Case #%d: ", cases);
    scanf("%d", &n);
    for (int i = 1; i <= n; ++i) {
      scanf("%d", a + i);
      p[i] = pp[i] = i;
    }
    // f[0][0] = 0;
    sort(p + 1, p + n + 1, cmpor);
    for (int i = 1; i <= n; ++i) {
      int l = pp[p[i]] - 1, r = n - i + 1 - pp[p[i]];
      if (l > r) {
	ans += r;
      }
      else {
	ans += l;
      }
      for (int j = p[i] + 1; j <= n; ++j) --pp[j];
      // printf("%d\n", p[i]);
      // for (int j = 1; j <= n; ++j) {
      // 	printf("%d ", pp[j]);
      // }
      // printf("\n");
    }
    
    
    // for (int i = 0; i <= n; ++i) ans = min(ans, f[n][i]);
    printf("%d\n", ans);
    
  }
  return 0;
}

