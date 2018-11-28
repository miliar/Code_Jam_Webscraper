#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>
#include <string>
#include <math.h>
#include <vector>
using namespace std;

const int maxn = 1000 + 10;
int n, a[maxn];

int main()
{
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);
  int TextN;
  scanf("%d", &TextN);
  for (int TT = 1; TT <= TextN; TT++) {
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
      scanf("%d", a + i);
    
    int ans = 1000;
    for (int et = 1; et <= 1000; et++) {
      int tmp = 0;
      for (int i = 1; i <= n; i++) {
        int k = a[i] / et;
        if (a[i] % et == 0) --k;
        tmp += k;
      }
      ans = min(ans, et + tmp);
    }
    printf("Case #%d: %d\n", TT, ans);
  }
  return 0;
}