#include<iostream>
#include<cmath>
#include<cstdio>

using namespace std;

int main() {
  int T;
  cin >> T;

  for (int t=0; t<T; ++t) {
    double time = 0.0, v = 2.0, c, f, x;
    cin >> c >> f >> x;


    while ( c/v + x/(v+f) < x/v ) {
      time += c/v;
      v += f;
    }

    time += x / v;

    printf("Case #%d: %.7f\n", t+1, time);
  }

  return 0;
}
