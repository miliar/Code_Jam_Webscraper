#include <cstdlib>
#include <cmath>
#include <ctime>
#include <iostream>
#include <fstream>
#include <functional>
#include <queue>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

//const char* input = "sample-input.txt";
//const char* output = "sample-output.txt";
const char* input = "A-large.in";
const char* output = "A-large.out";

int main(int argc, char** argv) {

  ifstream I(input);
  ofstream O(output);

  int T; I >> T;
  for (int t = 0; t < T; ++t) {

    int Smax; I >> Smax;
    char Si; I >> Si;

    long acc = (Si - '0'), needed = 0;
    for (int i = 1; i <= Smax; ++i) {
      I >> Si;

      int s = Si - '0';
      int n = max(i - acc, 0L);
      needed += n;
      acc += (s + n);
    }


    stringstream ss;
    ss << "Case #" << (t + 1) << ": " << needed << endl;
    string result = ss.str();
    O << result;
    cout << result;
  }


  I.close();
  O.close();
  return 0;
}
