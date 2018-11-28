#include <iostream>
#include <fstream>
using namespace std;

void findG(ifstream& ifile) {
  int t = 0, x = 1;
  ifile >> t;
  for(int i = 0; i < t; ++i) {
    cout << "Case #" << (x++) << ":";
    int k = 0, c = 0, s = 0;
    ifile >> k >> c >> s;
    if(k == s) {
      for(int j = 0; j < k; ++j) {
        cout << ' ' << (j+1);
      }
      cout << endl;
    } else {
      cout << ' ' << "IMPOSSIBLE" << endl;
    }
  }
}

int main(int argc, char** argv) {
  if(argc != 2) { cerr << "Wrong usage." << endl; }
  ifstream ifile(argv[1]);

  findG(ifile);

  return 0;
}
