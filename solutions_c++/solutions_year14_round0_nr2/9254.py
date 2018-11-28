#include <cstdio>

using namespace std;

int main() {
  int n;
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) {
    double c, f, x;
    double s_sofar = 0;
    double s = 0;
    double income = 2;
    scanf("%lf %lf %lf\n", &c, &f, &x);
    double bought, best = x / income;
    while(true) {
      s = c / income;
      s_sofar += s;
      income += f;
      bought = s_sofar + x / income;
      if(bought < best) {
        best = bought;
      } else {
        break;
      } 
    }
    printf("Case #%d: %.7f\n", i, best);
  }
  return 0;
}