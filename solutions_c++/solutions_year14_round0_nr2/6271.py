#include <stdio.h>

int main() {
    int kase;
    int h = 1;
    freopen("B-large.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d", &kase);
    while (kase--) {
          double c, f, x;
          scanf("%lf %lf %lf", &c,&f, &x);
          double init = 0;
          double inc = 2;
          double ans = 0;
          for (int i = 0; ; ++i) {
              if (c >= x) break;
              double end_with_no_farm = x/inc;
              double end_with_farm = x/(inc+f)+c/inc;
              if (end_with_no_farm < end_with_farm) {
                 break;
              }
              ans += c/inc;
              inc += f;
          }
          ans += x/inc;
          printf("Case #%d: %.8f\n",h++,ans);
    }
    return 0;
}
