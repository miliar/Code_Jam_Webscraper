#include <bits/stdc++.h>
using namespace std;

int main(){
  int T,caso = 0;
  double C,F,X;
  scanf("%i",&T);
  while(T--) {
    double tme = 0.0,gain = 2.0;
    scanf("%lf %lf %lf",&C,&F,&X);
    while( ( C/gain + X/(gain+F) - X/gain ) < 0 ){
      tme += C/gain;
      gain += F;
    }
    tme += X/gain;
    printf("Case #%i: %.7lf\n",++caso,tme);
  }
  return 0;
}