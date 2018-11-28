#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

const int MaxN = 1010;
const int inf = 1e9;

int main(void) {
  int tc;
  scanf("%d",&tc);
  for (int t = 1; t <= tc; ++t) {
    int n, p[MaxN], sol = 0;
    scanf("%d",&n);
    for (int i = 0; i < n; ++i) {
      scanf("%d",&p[i]);
      sol = max(sol, p[i]);
    }
    
    for (int k = 1; k <= 1000; ++k) {
      int tot = 0;
      for (int i = 0; i < n; ++i)
	tot += (p[i] + k - 1) / k - 1;
      sol = min(sol, tot + k);
    }
    printf("Case #%d: %d\n",t,sol);
  } 
  return 0;
}
