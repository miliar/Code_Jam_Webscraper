
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int T;	
	cin >> T;

  for(int t = 1; t <= T; t++) {
    double C, F, X;
    cin >> C >> F >> X;

    double rate = 2.;
    double time = 0.;

    double best_time = time + X/rate;

    for(int nb = 0; ; nb++) {
      time += C / rate;
      rate += F;
      double new_time = time + X / rate;
      if(new_time < best_time)
        best_time = new_time;
      else 
        break;
    }
    
    cout.precision(10);
    cout << "Case #" << t << ": " << best_time << endl;
  }


}
