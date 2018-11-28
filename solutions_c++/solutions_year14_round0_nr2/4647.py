#include <stdio.h>

int main() {
  int T;scanf("%d",&T);
  for (int cas = 1;cas <= T;cas++) {
    double c,f,x;scanf("%lf%lf%lf",&c,&f,&x);
    double res = x/2,past = 0,cur = 2;
    
    while (true) {
      past += c/cur;
      double tmp = past + x/(cur+f);
      if (tmp > res) break;
      cur += f;
      res = tmp;
    }

    printf("Case #%d: %.7lf\n",cas,res);
    
  }
  return 0;
}
