#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

const unsigned int SIZE     = 4;
const unsigned int ATTEMPTS = 2;


// Let N be the number of farms
// We want X / (2 + NF) <= C / (2 + NF) + X / (2 + (N + 1)F)
// Which in turn is N >= X / C - 2 / F - 1
//
// For N >= 1,
//   Total time = C * (1/2 + 1/(2+F) + ... + 1/(2+(N-1)F)) + X/(2+NF)
//
// If N = 0,
//   Total time = X /2
//
int main() {
  // Read in # test cases
  unsigned int T;
  cin >> T;
  for (unsigned int i = 1; i <= T; ++i) {
    // Parse inputs
    double C, F, X;
    cin >> C >> F >> X;
  
    // Compute answers 
    double N = ceil((X / C) - (2.0 / F) - 1);
    if (N < 0) {
      N = 0;
    }
 
    double timeTaken = 0.0;
    for (unsigned int n = 0; n < N; ++n) {
      timeTaken += (1 / (2 + (n * F)));
    }
    timeTaken = (timeTaken * C) + (X / (2 + (N * F)));   

    // Print answers
    cout << "Case #" << i << ": " << std::setprecision(7) << fixed << timeTaken << "\n";
  }

  return 0;
}
