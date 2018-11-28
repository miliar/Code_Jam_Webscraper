// run cat in | qra
#include <iostream>
using namespace std;
int debug = 0;

int main(int argc, const char *argv[]) {
  int Tc = 0;
  int N = 0;
  int M = 0;
  unsigned int l[100][100];
  unsigned int s[100][100];
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
    cin >> N;
    cin >> M;
    if (debug == 1) {
      cout << "N = " << N << " M = " << M << endl;
    }
    // input N lines with M entries each
    for (int n=0; n<N; n++) {
      for (int m=0; m<M; m++) {
	cin >> l[m][n];
	s[m][n] = 0; // init the score matrix
	if (debug == 1) {
	  cout << l[m][n];
	}
      }
      if (debug == 1) {
	cout << endl;
      }
    }
    
    for (int n=0; n<N; n++) {
      for (int m=0; m<M; m++) {
	// test m until > value found
	for (int dm=0; dm<M; dm++) {
	  if (l[dm][n] > l[m][n]) {
	    s[m][n]|=1; 
	    if (debug == 1) {
	      cout << n << ", " << m << " is not safe in m " << endl;
	    }
	    break;
	  }
	}
	for (int dn=0; dn<N; dn++) {
	  if (l[m][dn] > l[m][n]) {
	    s[m][n]|=2; 
	    if (debug == 1) {
	      cout << n << ", " << m << " is not safe in n " << endl;
	    }
	    break;
	  }
	}
      }
    }
    for (int n=0; n<N; n++) {
      for (int m=0; m<M; m++) {
	// it has to blocked in both x and y
	if (done == 0) {
	  if (s[m][n] == 3) {
	    cout << "NO" << endl;
	    done = 1;
	  }
	}
      }
    }
    if (done == 0) {
      cout << "YES" << endl;
    }
  }
  return 0;
}
