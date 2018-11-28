#include <algorithm>
#include <cmath>
#include <iostream>
#include <fstream>

using namespace std;

int size_int(int n) {
  string n_str = to_string(n);
  return n_str.size();
}

bool IsPalindrome(int n) {
  cerr << "IsPalindrome: " << n << endl;
  string str = to_string(n);
  for (int i = 0; i < (str.size()+1)/2; i++) {
    cerr << "i:" << i << "," << str[i] << " ; i2: " << str.size()-1-i << ", " << str[str.size()-1-i] << endl;
    if (str[i] != str[str.size()-1-i])
      return false;
  }
  return true;
}

bool CheckPalindrome(int n, int min, int max) {
  int square_nb_pal = n*n;
  cerr << "nb²: " << square_nb_pal << endl;
  if (square_nb_pal >= min and square_nb_pal <= max) {
    if (IsPalindrome(square_nb_pal)) {
      return true;
    }
  }
  return false;
}

int main(int argc, char** argv) {

  if (argc < 2) {
    cerr << "You should provide an input file" << endl;
    return 1;
  }

  ifstream myfile(argv[1]);
  if (!myfile.is_open()) {
    cerr << "Cannot open file" << endl;
    return 1;
  }

  int nb_tests;
  myfile >> nb_tests;

  for (int test_i = 1; test_i <= nb_tests; test_i++) {
    // Read input data

    int A1, B1;
    myfile >> A1;
    myfile >> B1;

    int A = sqrt(A1);
    int B = sqrt(B1);
    int sizeA = size_int(A1);
    cerr << "sizeA: " << sizeA << endl;
    int sizeB = size_int(B1);
    cerr << "sizeB: " << sizeB << endl;

    int count = 0;
    //for (int size = sizeA; size <= sizeB; size++)
    int min = pow(10, sizeA/2-1);
    cerr << "min: " << min << endl;
    int max = pow(10, (sizeB+1)/2);
    cerr << "max: " << max << endl;
    if (min < 10) {
      for (int i = min; i < 10; i++) {
        if (CheckPalindrome(i, A1, B1))
          count++;
      }
    }
    for (int nb = min; nb <= max; nb++) {
      cerr << "----" << endl;
      cerr << nb << endl;
      string nb_str = to_string(nb);
      string nb_str_reverse = nb_str;
      reverse(nb_str_reverse.begin(), nb_str_reverse.end());
      nb_str += nb_str_reverse;
      //cerr << nb_str << endl;
      int nb_pal = stoi(nb_str);
      cerr << nb_pal << endl;
      if (CheckPalindrome(nb_pal, A1, B1)) {
        count++;
      }
      for (int i = 0; i < 9; i++) {
        cerr << "...." <<to_string(nb) << endl;
        string nb_str2 = to_string(nb) + to_string(i) + (nb_str_reverse);
        nb_pal = stoi(nb_str2);
        cerr << nb_pal << endl;
        if (CheckPalindrome(nb_pal, A1, B1)) {
          count++;
        }
      }
    }


    cout << "Case #" << test_i << ": " <<  count << endl;
  }

  return 0;
}
