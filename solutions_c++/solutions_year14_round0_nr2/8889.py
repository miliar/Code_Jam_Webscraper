#include <iostream>
#include <iomanip>

using namespace std;

double process_testcase() {
    double C, F, X;
    cin >> C;
    cin >> F;
    cin >> X;
    
    double initial_rate = 2;
    double rate = 2;
    double cookies = 0;
    double time = 0;
    
    while( X/rate > C/rate + X/(rate + F) ){
      time += C/rate;
      rate += F;
    }
    
    time += X/rate;
        
    return time;
}


int main( int argc, char* argv[] ) {
  int T;
  cin >> T;
  for(int i = 1; i <= T; i++){
    cout << "Case #" << i << ": " ;
    cout << std::fixed << std::setw( 11 ) << std::setprecision( 7 ) 
          << process_testcase() << endl;
  }

  return 0;
}