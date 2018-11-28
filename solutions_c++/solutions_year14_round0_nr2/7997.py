#include <iostream>
#include <sstream>
#include <string> 
#include <cmath>

using namespace std;

void case_(int n, double answer) {
  cout.precision(7);
  cout << "Case #" << n << ":" << " " << fixed << answer << endl; 
}


void toString(int number, string& result) {  
  ostringstream convert;
  convert << number;    
  result = convert.str();  
}

double computeTime(int n, double C, double F, double X) {
  double r = 0;

  for (int i = 0; i < n; i++) {
    r += C / (2.0 + ((double) i) * F);
  }

  r += X / (2.0 + ((double) n) * F);
  
  return r;
}

void doCase(int n) {
  double C,F,X;
  cin >> C;
  cin >> F;
  cin >> X;

  int rn = ceil(X / C - 1.0 - 2.0/F);
  if (rn < 0) rn = 0;
  case_(n, computeTime(rn, C, F, X));
}

int main() {
  int cases;
  cin >> cases;
  for (int i = 0; i < cases; i++) {
    doCase(i+1);
  }
}
