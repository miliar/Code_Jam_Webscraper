#include <cstdio>
#include <cmath>
#include <iostream>

using namespace std;

double getTimeTaken( double C, double F, double X ) {
  double timeTaken = 0;
  double prev = 2;
  while ( X / prev > ( C / prev + X / (prev + F) ) ) {
    timeTaken += C / prev;
    prev += F;
  }
  return timeTaken + X / prev;
}

int main() {

  double C, F, X;
  int T;
  
  cin >> T;
  cout.precision( 7 );
  cout.setf( ios::fixed, ios::floatfield );
  
  for (int i = 0; i < T; i++) {
    cin >> C >> F >> X;
    double timeTaken = getTimeTaken(C, F, X);    
    cout << "Case #" << ( i + 1 ) << ": " << timeTaken << endl;
  }
}
