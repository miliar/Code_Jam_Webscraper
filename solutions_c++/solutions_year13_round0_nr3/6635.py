#include <iostream>
#include <fstream>
#include <cmath>
#include <sstream>
#include <string>

using namespace std;

int main(int argc, char * argv[]) {
  int T;
  ifstream input;
  input.open(argv[1]);
  input >> T;
  for (int i=0; i<T; i++) {
    long a,b;
    long count = 0;
    input >> a >> b;
    for (long j=a; j<b+1; j++) {
      stringstream ss;
      ss << j;
      string s = ss.str();
      string rs = string(s.rbegin(), s.rend());
      long root = (long)sqrt(j);
      if (root * root != j)
        continue;

      stringstream sr;
      sr << root;
      string rootstr = sr.str();
      string rootstrr = string(rootstr.rbegin(), rootstr.rend());
      if (s == rs && rootstr == rootstrr) {
        count++;
      }
    }
    cout << "Case #" << i+1 << ": " << count << endl;
  }
}

