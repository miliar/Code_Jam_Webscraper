#include <algorithm>
#include <cmath>
#include <cfloat>
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char** argv) {

  if (argc < 2) {
    //////cerr << "You should provide an input file" << endl;
    return 1;
  }

  ifstream myfile(argv[1]);
  if (!myfile.is_open()) {
    //////cerr << "Cannot open file" << endl;
    return 1;
  }

  int nb_tests;
  myfile >> nb_tests;

  for (int test_i = 1; test_i <= nb_tests; test_i++) {
    // Read input data
    double C, F, X;
    myfile >> C;
    myfile >> F;
    myfile >> X;
    //cerr << "C: " << C << " F: " << F << " X:" << X << endl;
    double X_C = X/C + 1;
    //cerr << X_C << endl;
    double min = DBL_MAX;
    double penal = 0;
    for (int i = 0; i <= X_C; i++) {
      double coef = (i*F)+2;
      double res = X/coef + penal;
      //cerr << " c: " << coef << " p: " << penal << " C/coef " << C/coef << endl;
      //cerr << res << endl;
      if (res < min) {
        min = res;
      }
      penal = penal + C/coef;
    }
    cout.precision(10);
    cout << "Case #" << test_i << ": " << min << endl;
  }

  return 0;
}

