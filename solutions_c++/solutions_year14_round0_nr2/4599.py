#include<stdio.h>
#include<algorithm>

double C,F,X,a,c,m;

int main() {
  int t, T;
  int i, N;

  scanf("%d",&T);
  for(t=1;t<=T;t++) {
    scanf("%lf %lf %lf",&C,&F,&X);
    a = 0;
    m = 1e20;
    for(i=0;;i++) {
      c = a + X/(2+i*F);
      a = a + C/(2+i*F);
      if(m > c) m = c;
      if(a > m) break;
    }
    printf("Case #%d: %.7lf\n",t,m);
  }
  return 0;
}
