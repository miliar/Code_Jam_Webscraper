#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <list>
#include <stdint.h>

using namespace std;

uint64_t str2uint(string input) {
  uint64_t val = 0;

  for (int n=0; n<input.length(); n++)
    val += input[n] == '1' ? 1 << n : 0;

  return val;
}
 
class Solver {
 public:
  Solver() {
  }

  ostringstream convert;

  string solve() {
    int cnt = 0;
    for (int n=0; n<A; n++) {
      for (int m=0; m<B; m++) {
        if ((n&m) < K) {
          cnt++;
        }
      }
    }

    convert << cnt;
    return convert.str();
  }

  uint64_t A, B, K;

};
 
int main (void) {
  int n, T;
  string val;

  cin >> T;

  for (n=1; n<=T; n++) {  
    Solver *solver = new Solver();
    cin >> solver->A >> solver->B >> solver->K;

    cout << "Case #" << n << ": " << solver->solve() << endl;
  }

  return 0;
}
