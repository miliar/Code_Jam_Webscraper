// Copyright (c) 2013 Patrick Huck
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <cmath>

using namespace std;
typedef long long i64;
std::ifstream inFile;
std::ofstream outFile;
const bool verbose = true;

void initIO(const char* str) {
  string fn(str);
  inFile.open(fn.c_str());
  fn.replace(fn.end()-2, fn.end(), "out");
  outFile.open(fn.c_str());
}

struct TestCase {
  i64 A;  // lower limit
  i64 B;  // upper limit
  void print() { cout << "A = " << A << "  B = " << B << endl; }
  i64 reverse(i64 i) {
    i64 rev = 0;
    while ( i > 0 ) { rev*=10; rev+=i%10; i/=10; }
    return rev;
  }
  bool isFair(const i64& i) { return (i==reverse(i)); }  //  palindrome
  bool isSquare(const i64& i) {  // square of a palindrome
    std::ostringstream oss; oss << sqrt(i);
    string sRoot = oss.str(); std::stringstream ss(sRoot);
    i64 iRoot;
    bool isIntRoot = ( ss >> iRoot && !(ss >> sRoot) );
    return (isIntRoot && isFair(iRoot));
  }
  bool isFairSquare(const i64& i) { return (isFair(i) && isSquare(i)); }
  int analyze() {
    int cnt = 0;
    for ( i64 n = A; n <= B; ++n ) {
      if ( isFairSquare(n) ) { cnt++; if (verbose) cout << n << endl; }
    }
    return cnt;
  }
  void clear() { A = -1; B = -1; }
} tc;

int main(int argc, char *argv[]) {
  if ( argc < 1 ) return 1;
  initIO(argv[1]);
  string line, buf;
  int nl = -1;
  while ( getline(inFile, line) ) {
    nl++; if (!nl) continue;
    std::istringstream ss(line);
    tc.clear();
    ss >> tc.A >> tc.B;
    if ( verbose ) tc.print();
    outFile << "Case #" << nl << ": " << tc.analyze() << endl;
  }
  inFile.close();
  outFile.close();
  return 0;
}
