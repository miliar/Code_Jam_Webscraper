
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <iostream>
#include <iomanip>
#include <sstream>

#include <algorithm>
#include <list>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <set>
#include <vector>

using namespace std;

double C;
double F;
double X;
double elapsed_time;
double rate;

bool build_farm() {
  if ((X - C) / rate < X / (rate + F)) {
    return false;
  }
  return true;
}

int main(int argc, const char *argv[]) {

  int num_cases;
  cin >> num_cases;

  cout << setprecision(7) << fixed;

  for (int i = 1; i <= num_cases; ++i) {

    cin >> C;
    cin >> F;
    cin >> X;
    rate = 2.0;
    elapsed_time = 0.0;

    while (true) {
      elapsed_time += C / rate;
      if (build_farm()) {
        rate += F;
      } else {
        elapsed_time += (X - C) / rate;
        break;
      }
    }

    cout << "Case #" << i << ": " << elapsed_time << endl;
  }

  return 0;
}

