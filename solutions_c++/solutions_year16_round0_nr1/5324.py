#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

unsigned long T, N, Nby;
vector<bool> found(10, false);
int numFound = 0;

bool canSleep() { return N != 0; }

bool isAwake(unsigned long mult) {
  stringstream ss;
  ss << (N * mult);
  string str = ss.str();
  ss.clear();
  ss.str("");
  for (char i = '0'; i < ('9' + 1); i++) {
    if (!found[i - '0']) {
      // cout << "char: " << i << endl;
      if (find(str.begin(), str.end(), i) != str.end()) {
        found[i - '0'] = true;
        numFound++;
        if (numFound == 10)
          return false;
      }
    }
  }
  return true;
}

int main(int argc, char **argv) {
  fstream fin(argv[1]);
  fin >> T;
  for (int i = 0; i < T; i++) {
    fin >> N;
    if (N == 0) {
      cout << "Case #" << (i + 1) << ": "
           << "INSOMNIA" << endl;
    } else {
      unsigned long mult = 0;
      while (isAwake(++mult)) {
        // cout << N * mult;
      };
      cout << "Case #" << (i + 1) << ": " << N * (mult) << endl;
      for (int j = 0; j < 10; j++) {
        found[j] = false;
        numFound = 0;
      }
    }
  }
}
