#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

void count(ifstream& ifile) {
  int64_t t = 0, x = 1;
  ifile >> t;
  for(int64_t i = 0; i < t; ++i) {
    cout << "Case #" << (x++) << ":";
    int64_t n = 0;
    vector<bool> _d;
    for(int64_t j = 0; j < 10; ++j) { _d.push_back(false); }
    ifile >> n;
    if(n == 0) {
      cout << ' ' << "INSOMNIA" << endl;
    } else {
      int64_t ans = n, loop = 100*n*n;
      bool fin = true;
      for(int64_t j = 0; j < loop; ++j) {
        int64_t tmp = ans;
        while(tmp > 0) {
          _d[tmp%10] = true; tmp /= 10;
        }
        fin = true;
        for(int k = 0; k < 10; ++k) { fin = fin && _d[k]; }
        if(fin) break;
        ans += n;
      }
      if(fin) cout << ' ' << ans << endl;
      else cout << ' ' << "INSOMNIA" << endl;
    }
  }
}

int main(int argc, char** argv) {
  if(argc != 2) { cerr << "Wrong usage." << endl; }
  ifstream ifile(argv[1]);

  count(ifile);

  return 0;
}
