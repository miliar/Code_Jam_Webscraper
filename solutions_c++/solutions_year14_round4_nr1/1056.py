#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

const int  nmax = 10000 + 18;

int n, x, s[nmax], ans;

int main()
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int T;
  scanf("%d", &T);
  for (int cases = 1; cases <= T; ++cases) {
    ans = 0;
    printf("Case #%d: ", cases);
    scanf("%d%d", &n, &x);
    for (int i = 1; i <= n; ++i) scanf("%d", s + i);
    sort(s + 1, s + n + 1);
    ans = n;
    for (int i = 1, r = n; i < r; ++i) {
      while (i < r && s[i] + s[r] > x) --r;
      if (i < r && s[i] + s[r] <= x) --ans, --r;
      else break;
      
    }
    
    printf("%d\n", ans);
    
  }
  return 0;
}

