#include <bits/stdc++.h>
using namespace std;

int t;
double c, f, x, ans;

double calc(int tb){
  double time = 0.00;
  double prod = 2.00;
  for(int i = 0; i < tb; i ++){
    time += c / prod;
    prod += f;
  }
  time += x / prod;
  return time;
}

int main(){

  scanf("%d", &t);
  for(int ct = 1; ct <= t; ct ++){
    
    scanf("%lf %lf %lf", &c, &f, &x);

    int lo = 0, hi = x;
    while(lo < hi){
      int med = (lo + hi) / 2;
      double t1 = calc(med);
      double t2 = calc(med + 1);
      if(t1 <= t2)
        hi = med;
      else
        lo = med + 1;
    }

    ans = calc(lo);

    printf("Case #%d: %.17lf\n", ct, ans);

  }

  return 0;
}
