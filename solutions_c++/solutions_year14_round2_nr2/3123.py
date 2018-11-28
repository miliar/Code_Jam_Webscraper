#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <bitset>

using namespace std;

int debug = 0;

int main(int argc, char *argv[]) {
  int Tc = 0;
  unsigned int A;
  unsigned int B;
  unsigned int K;
  // read the number of test cases
  cin >> Tc;
  if (debug == 1) {
    cout << "  Test Cases: " << Tc <<  endl;
  }
  for (int Tci=1; Tci<=Tc; Tci++) {
    // inputs
    cin >> A >> B >> K;
    if (debug == 1) {
      cout << "inputs A " << A << " B " << B <<  " K " << K << endl;
    }
    // combinations
    int res = 0;
    for (int a = 0; a < A; a++) {
      for (int b = 0; b < B; b++) {
	if ((a & b) < K) {
	  res++;
	}
      }
    }
    cout << "Case #" << Tci << ": " << res <<  endl;
  }
}
