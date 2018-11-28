#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;

double c, f, x;
double ans;
double rate;


int main() {
  int TC;
  scanf("%d", &TC);

  for (int TCi = 1; TCi <= TC; ++TCi) {
    printf("Case #%d: ", TCi);
    ans = 0.0;
    rate = 2.0;
    
    scanf("%lf%lf%lf", &c, &f, &x);

    double t, tnext;

    // do {
    //   t = x / rate;
    //   tnext = c / rate + (x / (rate + f));
    //   rate += f;
    // } while ( t > tnext );

    while(1) {
      t = x / rate;
      tnext = c / rate + (x / (rate + f));

      if ( t > tnext) {
        ans += c / rate;
        rate += f;
      }
      else {
        ans += x / rate;
        break;
      }
        
    }

    printf("%.7lf\n", ans);
  }

  return 0;
}
