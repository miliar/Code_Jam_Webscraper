#include <bits/stdc++.h>
using namespace std;
int main() {
  int T;
  scanf("%d",&T);
  for (int ts=1;ts<=T;ts++) {
    int n;
    scanf("%d",&n);
    if (n == 0) {
      printf("Case #%d: INSOMNIA\n",ts);
      continue;
    }
    int prod = 0;
    int dd = 0;
    bool d[10];
    for (int i=0;i<10;i++) d[i] = false;
    while (dd < 10) {
      prod += n;
      int tmp = prod;
      while (tmp > 0) {
        if (d[tmp % 10] == false) {
          d[tmp % 10] = true;
          dd++;
        }
        tmp /= 10;
      }
    }
    printf("Case #%d: %d\n",ts,prod);
  }
  return 0;
}