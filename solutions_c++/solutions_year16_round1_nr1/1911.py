#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

void proc(ifstream& ifile) {
  int t = 0, x = 1;
  ifile >> t;
  for(int i = 0; i < t; ++i) {
    cout << "Case #" << (x++) << ": ";
    //// TODO ////
    string S = "";
    vector<char> y;
    char first = 'A';
    ifile >> S;
    int l = S.length();
    for(int i = 0; i < l; ++i) {
      if(S[i] < first) {
        y.push_back(S[i]);
      } else {
        y.insert(y.begin(), S[i]);
        first = S[i];
      }
    }
    for(int i = 0; i < l; ++i) { cout << y[i]; }
    //////////////
    cout << endl;
  }
}

int main(int argc, char** argv) {
  if(argc != 2) { cerr << "Wrong usage." << endl; }
  ifstream ifile(argv[1]);

  proc(ifile);

  return 0;
}
