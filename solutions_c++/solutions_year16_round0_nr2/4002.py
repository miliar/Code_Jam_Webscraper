#include <iostream>
#include <fstream>
using namespace std;

void flipPanCake(ifstream& ifile) {
  int t = 0, x = 1;
  ifile >> t;
  for(int i = 0; i < t; ++i) {
    cout << "Case #" << (x++) << ":";
    string S = "";
    ifile >> S;
    int len = S.length(), n = 0, p = 1;;
    for(int j = len-1; j >= 0; --j) {
      if(p == 1) {
        if(S[j] == '-') { ++n; p = 0; }
      } else {
        if(S[j] == '+') { ++n; p = 1; }
      }
    }
    cout << ' ' << n << endl;
  }
}

int main(int argc, char** argv) {
  if(argc != 2) { cerr << "Wrong usage." << endl; }
  ifstream ifile(argv[1]);

  flipPanCake(ifile);

  return 0;
}
