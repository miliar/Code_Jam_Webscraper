#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

const double eps = 1E-9;
double c, f, x;

int main()
{
  int t;
  freopen("in2.txt", "r", stdin);
  scanf("%d", &t);
  for(int test = 1; test <= t; test ++){
      scanf("%lf%lf%lf", &c, &f, &x);
      //printf("%.7f %.7f %.7f\n", c, f, x);
      double temp, ans;
      temp = ans = 0;
      double tempx = 0.0; // 手上有多少cookie
      double rate = 2.0;
      while(x > eps){
        //printf("%f %f %f\n", x, rate, ans);
        if(ans + x/rate < ans + c/rate + x/(rate+f)) {
          temp = x / rate;
          x -= temp * rate;
          ans += temp;
        }
        else{
            temp = c / rate;
            //x -= temp * rate;
            ans += temp;
            rate += f;
        }
      }
      printf("Case #%d: %.7f\n", test, ans);
  }
  return 0;
}
