#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

double simulate( double C, double F, double X ) {
  double rate = 2.0;
  double t = 0.0;

  // do nothing
  if( C > X ) {
    return X / rate;
  }

  // simple simulation
  while( true ) {
    // find next decision point, i.e. when we have enough cookies to be able
    // to choose whether we want to spend them on a factory or not.
    double alpha = C / rate;
    t += alpha;

    double dt = (X-C) / rate; // do nothing
    double dtprime = X / (rate+F); // build a factory
    if( dtprime < dt ) {
      rate += F;
    } else {
      return t+dt;
    }
  }

  return 0.0;
}

int main( int argc, char* argv[] ) {
  int T;
  cin >>T;

  for( int ca=0; ca<T; ++ca ) {
    double C, F, X;
    cin >> C >> F >> X;
    double res = simulate( C, F, X );
    cout << "Case #" << (ca+1) << ": " << fixed << setprecision(7) << res << endl;
  }

  return 0;
}

