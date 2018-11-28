#include <cstdio>

using namespace std;

int main() {
  int t, d, p[1010], ans, pmax;
  scanf("%d", &t);
  for(int tc = 1; tc <= t; tc++) {
    scanf("%d", &d);
    pmax = 1;
    for(int i = 0; i< d; i++) {
      scanf("%d", p+i);
      if(p[i]>pmax)
        pmax = p[i];
    }
    ans = pmax;
    for(int i = pmax-1; i>0; i--) {
      int temp = i;
      for(int j = 0; j<d; j++) {
        temp += (p[j]-1)/i;
      }
      if(temp < ans)
        ans = temp;
    }
    printf("Case #%d: %d\n", tc, ans);
  }
  return 0;
}