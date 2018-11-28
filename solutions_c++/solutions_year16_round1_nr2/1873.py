#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

void proc(ifstream& ifile) {
  int t = 0, x = 1;
  ifile >> t;
  for(int i = 0; i < t; ++i) {
    cout << "Case #" << (x++) << ":";
    //// TODO ////
    int N = 0;
    vector<int> count(2510, 0);
    ifile >> N;
    for(int j = 0; j < 2*N-1; ++j) {
      for(int k = 0; k < N; ++k) {
        int h = 0;
        ifile >> h;
        ++count[h];
      }
    }
    vector<int> y;
    for(int j = 1; j <= 2500; ++j) {
      if(count[j]%2 == 1) {
        y.push_back(j);
        if(y.size() == N) break;
      }
    }
    for(int j = 0; j < N; ++j) cout << ' ' << y[j];
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
