#include <algorithm>
#include <cmath>
#include <iostream>
#include <fstream>

using namespace std;

bool is_consonant(char c) {
  return c != 'a' &&
         c != 'e' &&
         c != 'i' &&
         c != 'o' &&
         c != 'u';
}

int main(int argc, char** argv) {

  if (argc < 2) {
    ////cerr << "You should provide an input file" << endl;
    return 1;
  }

  ifstream myfile(argv[1]);
  if (!myfile.is_open()) {
    ////cerr << "Cannot open file" << endl;
    return 1;
  }

  int nb_tests;
  myfile >> nb_tests;

  for (int test_i = 1; test_i <= nb_tests; test_i++) {
    // Read input data
    int N;
    string str;
    myfile >> str;
    myfile >> N;
    int res = 0;

    int str_len = str.size();
    int nb_consonant = 0;
    int last_i = 0;
    for (int i = 0; i < str_len; i++) {
      if (is_consonant(str[i])) {
        nb_consonant++;
        if (nb_consonant >= N) {
          int nb_substrings = 0;
          int after = str_len - i - 1;
          int before = i - (N -1) - last_i;
          cerr << "Before: " << before << ", after: " << after << ", i: " << i << ", last_i: " << last_i << endl;
          after++;
          before++;
          nb_substrings = after * before;
          res += nb_substrings;
          last_i = i - N + 2;
        }
      } else {
        nb_consonant = 0;
      }
    }

    cout << "Case #" << test_i << ": " << res << endl;
  }

  return 0;
}
