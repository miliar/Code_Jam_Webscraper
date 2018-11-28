#include <iostream>
#include <cstdio>

using namespace std;

double getTimeForFactories(long count, double c, double f) {
  double result = 0.0;
  for(long i = 0; i < count; i++) {
    double rate = 2.0 + i * f;
    result += (c / rate);
  }
  return result;
}

int main() {
  long cases;
  cin >> cases;
  for(long i = 0; i < cases; i++) {
    double c, f, x;
    cin >> c >> f >> x;
    if(x < c) {
      double result = x / 2.0;
      printf("Case #%ld: %.7f\n", i+1, result);
    }
    else {
      double catchdist = x - c;
      double catchtime = c / f;
      double exactspeed = catchdist / catchtime;
      long count = 0;
      for(long j = 0; j >= 0; j++) {
	if (2.0 + (double) j * f > exactspeed) {
	  break;
	}
	count = j + 1;
      }
      double timeforfacts = getTimeForFactories(count, c, f);
      double result = timeforfacts + (x / (2.0 + f * count));
      printf("Case #%ld: %.7f\n", i+1, result);
    }
  }
  return 0;
}
