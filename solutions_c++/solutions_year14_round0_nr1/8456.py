#include <algorithm>
#include <cmath>
#include <cfloat>
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char** argv) {

  if (argc < 2) {
    ////////cerr << "You should provide an input file" << endl;
    return 1;
  }

  ifstream myfile(argv[1]);
  if (!myfile.is_open()) {
    ////////cerr << "Cannot open file" << endl;
    return 1;
  }

  int nb_tests;
  myfile >> nb_tests;

  for (int test_i = 1; test_i <= nb_tests; test_i++) {
    // Read input data
    int ans1, ans2;
    int tab1[4][4];
    int tab2[4][4];
    myfile >> ans1;
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
        myfile >> tab1[i][j];
      }
    }
    myfile >> ans2;
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
        myfile >> tab2[i][j];
      }
    }
    int res = -1;
    bool bad_magician = false;
    //cerr << "ans1: " << ans1 << " ans2: " << ans2 << endl;
    ans1--;
    ans2--;
    for (int j = 0; j < 4; j++) {
      for (int k = 0; k < 4; k++) {
        //cerr << tab1[ans1][j] << " " << tab2[ans2][k] << endl;
        if (tab1[ans1][j] == tab2[ans2][k]) {
          //cerr << "Found something" << endl;
          if (res != -1) {
            // We already had a result!
            bad_magician = true;
          }
          res = tab1[ans1][j];
        }
      }
      //cerr << endl;
    }
    cout << "Case #" << test_i << ": ";
    if (bad_magician)
      cout << "Bad magician!";
    else if (res == -1)
      cout << "Volunteer cheated!";
    else
      cout << res;
    cout << endl;
  }

  return 0;
}

