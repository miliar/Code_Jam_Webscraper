#include <iostream>
#include <cstdio>
using namespace std;

int testcase;
double C,F,X;

int main () {
  freopen("B-large.in","r",stdin);
  freopen("a.out","w",stdout);
  scanf("%d",&testcase);
  for(int TC=1;TC<=testcase;++TC) {
    scanf("%lf%lf%lf",&C,&F,&X);
    double rate = 2.0, cur = 0, ans = X / rate, tmp;
    while (1) {
      cur += C / rate;
      rate += F;
      tmp = cur + X / rate;
      if (tmp < ans) ans = tmp;
      else break;
    }
    printf("Case #%d: %.7lf\n",TC,ans);
  }
}
