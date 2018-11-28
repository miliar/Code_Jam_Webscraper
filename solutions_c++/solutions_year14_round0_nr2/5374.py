#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
#include <string.h>
#include <set>
#include <stdio.h>
#include <assert.h>
#include <sstream>
using namespace std;

int main(int argc, char* argv[]) {
  int nocases;
  cin >> nocases;
  getchar();
  for (int rr = 1; rr <= nocases; ++rr) {
    double c, f, x;
    cin >> c >> f >> x;
    double t = 0, r = 2;
    while (1) {
      if (x/r > c/r + x/(r+f))
	t += c/r, r += f;
      else {
	t += x/r;
	break;
      }
    }
    printf("Case #%d: %.7lf\n", rr, t);
  }
  return 0;
}
