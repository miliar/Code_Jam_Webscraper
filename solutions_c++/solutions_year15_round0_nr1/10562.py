// run cat sample.in | ./qra > qra_sample.out
#include <boost/format.hpp>
#include <iostream>
#include <iomanip>
using namespace std;
int debug = 0;

int main(int argc, const char *argv[]) {
  int Tc = 0;         // number of test cases
  int Smax;           // max shyness level 
  char Slevel[1002];  // shyness levels (0-1000=1001 + 1)
  char sTmp[] = {0,0}; // tmp used to count people
  int Min = 0;        // minimum number of seed people
  int sPeople = 0;    // total number standing of people
  cin >> Tc;
  if (debug == 1) {
    cout << "Debug: Tc " << Tc <<  endl;
  }
  for (int tcase = 1; tcase <= Tc; tcase++) {
    cin >> Smax >> Slevel;
    if (debug == 1) {
      cout << "Debug: Smax " << Smax  << ", Slevel " << Slevel << endl;
    }
    // start seeding
    int level = 0; // start a shyness of 0
    sPeople = 0;
    Min = 0;
    while (level <= Smax) {
      if (Slevel[level] != '0') {
	if (sPeople < level) {
	  Min += level - sPeople;
	  sPeople += Min;
	}
	sTmp[0] = Slevel[level];
	sPeople += atoi(sTmp);
      }
      level += 1;
    }
    if (debug == 1) {
      cout << "Debug: sPeople " << sPeople << endl;
    }

    // initial conditions
    cout << "Case #" << tcase << ": " << Min << endl;

  }
}
