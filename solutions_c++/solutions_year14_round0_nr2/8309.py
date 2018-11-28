#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

int main() {
  size_t ntests;
  cin >> ntests;

  for(int i_test = 1 ; i_test <= ntests ; i_test++) {
    double C, F, X;

    double rate = 2.0;
    double time = 0.0;

    cin >> C >> F >> X;
    
    int n = 0;
    // Buying extra farm is quicker than waiting for objective
    // Time for extra farm : objective) / 
    while(X/(rate+F) < (X-C)/rate) {
      time += C/rate;
      n++;
      rate += F;
    }
    time += X/rate;

    // Time to output something
    cout << "Case #" << i_test << ": ";
    
    printf("%0.7f", time);

    cout << endl;
  }
}
