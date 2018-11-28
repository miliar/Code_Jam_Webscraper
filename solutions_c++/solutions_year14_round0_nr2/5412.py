#include <iostream>
#include <iomanip>
#include <vector>
#include <set>
using namespace std;

int main() {

  int n;
  cin >> n;
  cout << fixed;
  for (int i = 0; i< n; i++) {
    double C, F, X;
    cin >> C;
    cin >> F;
    cin >> X;
    // By no farm == t = X/2;
    double mint = X/2.0;
    double inc = 2;
    double base = 0;
    while (X>0) {
      base = base + C/inc;
      //      cout << base << endl;
      
      inc = inc+F;
      //cout << inc << endl;
      double m = X/inc;
      //cout << m << endl;
      //cout << mint << endl;
      if (mint > base + m) {
	mint = base+m;
      } else {
	break;
      }
      //if (X/inc < C/inc) {
      //break;
      //}
    }
    
    
    cout << "Case #"<<i+1<<": "<< setprecision(7) << mint << endl;
  }
}

    
