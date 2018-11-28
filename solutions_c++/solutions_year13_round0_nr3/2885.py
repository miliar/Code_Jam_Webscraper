// run cat in | qra
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <gmp.h>

using namespace std;
int debug = 0;

int palindrome(int x) {
  char str[100];
  sprintf(str, "%d",x);
  if (debug == 2) {
    cout << str << endl;
  }
  int n = strlen(str);
  for (int i=0; i<n; i++) {
    if (str[i] != str[n-i-1]) {
      return 0;
    }
  }
  return 1;
}

int main(int argc, const char *argv[]) {
  int Tc = 0;
  int A = 0;
  int B = 0;
  unsigned int l[1000];
  // read the number of test cases
  cin >> Tc;
  if (debug == 1) {
    cout << "Test Cases: " << Tc <<  endl;
  }
  for (int k=0; k<Tc; k++) {
    int done = 0;
    cout << "Case #" << k+1 << ": ";
    if (debug == 1) {
      cout << endl;
    }
    cin >> A;
    cin >> B;
    if (debug == 1) {
      cout << "A = " << A << " B = " << B << endl;
    }
    // search for fair and square between A and B
    int ct = 0;
    for (int n = A; n <= B; n++) {
      if (palindrome(n) == 1) {
	int f = sqrt(n);
	if (n == f*f) {
	  if (palindrome(f)) {
	    ct++;
	    if (debug == 1) {
	      cout << "n = " << n << endl;
	    }
	  }
	}
      }
    }
    cout << ct << endl;
  }
  return 0;
}
