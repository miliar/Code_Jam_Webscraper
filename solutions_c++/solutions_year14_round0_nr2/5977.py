#include <cstdio>
#include <iostream>

using namespace std;

int main() {
  int T; scanf("%d\n", &T);
  for (int tt = 1; tt <= T; ++tt) {
  	double c, f, x;
  	cin >> c >> f >> x;
  	double a = x / 2;
  	double t = 0;
  	double r = 2;
  	while (true) {
  		double dt1 = x / r;
  		double dt2 = c / r;
		if (t + dt1 < a) a = t + dt1;
  		t += dt2;
  		if (t + 1e-8 > a) break;
  		r += f;
  	}
    printf("Case #%d: ", tt);
    printf("%.9lf", a);
    putchar('\n');
  }
  return 0;
}

