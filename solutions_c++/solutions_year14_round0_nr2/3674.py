#include <iomanip>
#include <iostream>

using namespace std;

int main() {
  int ncases;
  cin >> ncases;
  
  cout << setprecision(15);
  
  for (int test = 0; test < ncases; ++test) {
    double C, F, X;
    cin >> C >> F >> X;
    double prev = X / 2;
    
    int nfarms = 1;
    
    while (true) {
      double next = X / (2 + nfarms*F);
      for (int n = 0; n < nfarms; ++n) {
        next += C / (2 + n*F);
      }
      
      if (next > prev) {
        break;
      }
      ++nfarms;
      prev = next;
    }
    
    cout << "Case #" << test + 1 << ": ";
    cout << prev << endl;
  }
  
  return 0;
}

