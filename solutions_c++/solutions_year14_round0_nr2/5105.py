#include <iostream>
#include <vector>
#include <iomanip>
#include <stdio.h>

using namespace std;
double solve(double ans, double c, double f, double x)
{

  double buyfarm = 0;
  double waitx = 0;
  int i = 1;
  double buywaitx = 0;
  double k = 2;
  while (1) {
    buyfarm = (c/ k);
    waitx = (x / k);
     k = 2 + f * i;
    buywaitx = (x / k);
    if ( ((ans + waitx) - (ans + buyfarm + buywaitx)) > 0.0) {
        ans = ans + buyfarm;

    } else {
        ans = ans + waitx;
        break;
    }
    i++;
    // printf(" %.8f\n", ans);
    //cout << "ans = " << ans << endl;
  }
   return ans;
}


int main()
{
  int t = 0;
  scanf("%d", &t);
  int k = 1;
  while (t--) {
     double c =0;
     double f = 0;
     double x = 0;


     scanf("%lf %lf %lf", &c, &f, &x);
     double val = solve(0.0, c, f, x);
     printf("Case #%d: %.8f\n", k, val);
     k++;
  }

}
