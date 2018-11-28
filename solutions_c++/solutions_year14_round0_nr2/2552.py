#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
typedef pair<int,int> ii;

int main() {
  int tests;
  double c, f, x;
  scanf("%d", &tests);
  for(int i = 1; i <= tests; ++i) {
    double rate = 2;
    double t = 0;
    scanf("%lf %lf %lf", &c, &f, &x);
    while(x / rate > c / rate + x / (rate + f)) {
	t += c / rate;
	rate += f;
    }
    printf("Case #%d: %.7lf \n", i, t + x / rate);
  }
}

