#include <iostream>

using namespace std;

double c,f,x;

double solve() {
  double curp = 2.0;
  double t = 0.0;

  while (1) {
    double timetof = (c / curp) + (x / (curp + f));
    double timetox = x / curp;
    if (timetox < timetof) {
      t += timetox;
      break;
    } else {
      t += (c / curp);
      curp += f;
    }
  }
  return t;
}

int main() {
  int tt;
  cin >> tt;
  for (int test = 1; test <= tt; test++) {
    cin >> c >> f >> x;



    printf("Case #%d: %.7f\n", test, solve());


  }


  return 0;
}
