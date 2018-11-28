//#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;

ifstream cin ("A-small.in");
ofstream cout ("A-small.out");

long long run() {
  long long t, r;
  cin >> r >> t;
  
  long long s0 = 1;
  long long s2 = sqrt(t);
  while (s2 >= s0) {
    long long n = (s0 + s2)/2ll;
    long long c = 2*n*n+(2*r-1)*n;
    if (c < 0 || c > t) s2 = n;
    else if (c == t) return n;
    else {
      long long c2 = 2*(n+1)*(n+1)+(2*r-1)*(n+1);
      if (c2 > t) return n;
      else if (c2 == t) return n+1;
      else s0 = n;
    }
  }
  return s2;
}

int main () {
  int T; cin >> T;
  for (int i=1; i<=T; i++) {
    cout << "Case #" << i << ": " << run() << endl;
  }
  return 0;
}
