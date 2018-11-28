#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main (int argc, char* argv[]) {

  if (argc < 2) {
    cout << "not enough arguments" << endl;
    return -1;
  }

  ifstream input(argv[1]); // open file 

  int numcases = 0;

  if (input.good()) {
    input >> numcases;

    for (int i = 1; i <= numcases; i++) {
      double currCookieProduction = 2.0000000;
	  double numCookies = 0.0000000;
	  double C_farmPrice = 0.0000000;
	  double F_farmProd = 0.0000000;
	  double X_cookiesNeeded = 0.0000000;
	  double seconds = 0.0000000;
	  input >> C_farmPrice;
	  input >> F_farmProd;
	  input >> X_cookiesNeeded;
	  
	  cout << setprecision(10);
	  
	  while(numCookies < X_cookiesNeeded) {
		double timeLeft = (X_cookiesNeeded - numCookies) / currCookieProduction;
		
		if(timeLeft < C_farmPrice/currCookieProduction) {
			// if it's faster to wait than to buy a farm, just wait.
			seconds += timeLeft;
			numCookies += currCookieProduction * timeLeft;
			
		}
		else if(timeLeft > (C_farmPrice/currCookieProduction) + ((X_cookiesNeeded - numCookies) / (currCookieProduction + F_farmProd))) {
			// if it's worse to wait than to buy a farm
			// buy a farm.
			
			// wait long enough to purchase a farm.
			seconds += C_farmPrice/currCookieProduction;
			
			// buy the farm.
			currCookieProduction += F_farmProd;
		}
		else {
			seconds += timeLeft;
			break;
		}
	  }
	  
	  cout << "Case #" << i << ": " << seconds << endl;
	  
    }
    
  }

  return 0;
}
