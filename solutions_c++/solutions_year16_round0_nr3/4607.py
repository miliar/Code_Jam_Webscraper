#include <iostream>

using namespace std;

main() {
  int T;
  long long divisor[11];
  cin >> T;
  for (int x=1; x<=T; x++) {
    int N,J,solutions=0;
    cin >> N >> J;
   
    cout << "Case #1:" << endl;
    for (int i=(1<<15)+1; i<(1<<16); i+=2) {
      bool likely_prime = true;
      int d=2;
      for (; d<=10; d++) {
	likely_prime = true;
	// convert i to base d value x
	long long x=0;
	for (long long p=1, b=i; b; b>>=1, p*=d)
	  if (b&1) x+=p;
	// check likely prime
	for (long long y=2; y<x && y<1000; y++) {
	  if ((x%y)==0) { divisor[d]=y; likely_prime=false; break; }
	};
	if (likely_prime) break;
      };
      if (likely_prime) continue;
      for (int p=15; p>=0; p--) cout << ((i>>p)&1);
      for (int d=2; d<=10; d++) cout << " " << divisor[d];
      cout << endl;
      if (++solutions>=J) break;
    };
  };
};

