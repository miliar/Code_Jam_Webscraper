#include <algorithm>
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char* argv[]) {

  if(argc != 2) {
    cout << "please pass exactly one argument" << endl;
    exit(1);
  }
  ifstream input;
  input.open(argv[1]);
  int t(0);

  input >> t;
  for(int i(0); i != t; ++i) {
      cout << "Case #" << i+1 << ": ";
      int a(0);
      int b(0);
      input >> a >> b;
      int fsq(0);
      for(int j(a); j != b + 1; ++j) {
          string s = to_string(j);
          string s2 = string(s.rbegin(), s.rend());
          if(s.compare(s2) != 0) continue;
          double sqj = sqrt(j);
          if(sqj != floor(sqj)) continue;
          s = to_string(int(floor(sqj)));
          s2 = string(s.rbegin(), s.rend());
          if(s.compare(s2) != 0) continue;
          ++fsq;
      }
      cout << fsq;
      cout << endl;
  }

  input.close();
  return 0;
}
