#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;

ifstream in("data.in");
ofstream out("data.out");

int main() {
  out.precision(7);
  
  int T;
  double C,F,X;
  in >> T;
  for (int curcase = 1; curcase <= T; curcase++) {
    in >> C >> F >> X;

    double numsec=0,currate=2;
    double besttime = X / currate;

    for (int numfarm=1; ; numfarm++) {
      numsec += C / currate;
      currate += F;

      if (numsec + (X / currate) < besttime) {
	besttime = numsec + (X / currate);
      } else {
	break;
      }
    }
    
    out << "Case #" << curcase << ": " << fixed << besttime << endl;
  }
}
