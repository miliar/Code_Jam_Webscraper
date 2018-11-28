#include <cstdlib>
#include <cmath>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <fstream>
#include <queue>
#include <string>
#include <vector>
using namespace std;

const char* input  = "B-large.in";
//const char* input  = "opa.txt";
const char* output = "B-large.out";


int main(int argc, char** argv) {
  
  ifstream I(input);
  ofstream O(output);

  cout << fixed << setprecision(7);
  O << fixed << setprecision(7);

  int T; I >> T;
  for (int t = 0; t < T; ++t) {

    double C, F, X;
    I >> C >> F >> X;

    double f = 2.0;
    double best_time = numeric_limits<double>::max();
    double time_spent_so_far = 0.0;

    while (true) {
      double time_to_finish_with_current_production = X / f;
      double time_to_buy_with_current_production = C / f;

      // how much time to finish with current production
      double current_time = time_spent_so_far + time_to_finish_with_current_production;

      if (current_time > best_time)
        break;
      else {
        best_time = current_time;

        time_spent_so_far += time_to_buy_with_current_production;
        f += F;
      }
    }

    O << "Case #" << (t + 1) << ": " << best_time << endl;
    cout << "Case #" << (t + 1) << ": " << best_time << endl;
  }


  I.close();
  O.close();
  return 0;
}