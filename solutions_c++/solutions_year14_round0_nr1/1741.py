#include <cstdlib>
#include <cmath>
#include <ctime>
#include <iostream>
#include <fstream>
#include <queue>
#include <string>
#include <vector>
using namespace std;

const char* input  = "A-small-attempt0.in";
//const char* input  = "opa.txt";
const char* output = "A-small-attempt0.out";


int main(int argc, char** argv) {
  
  ifstream I(input);
  ofstream O(output);

  int T; I >> T;
  for (int t = 0; t < T; ++t) {

    int cards1[4][4], cards2[4][4];
    int a1, a2; // answers

    I >> a1; --a1;
    for (int i = 0; i < 4; ++i)
      for (int j = 0; j < 4; ++j)
        I >> cards1[i][j];

    I >> a2; --a2;
    for (int i = 0; i < 4; ++i)
      for (int j = 0; j < 4; ++j)
        I >> cards2[i][j];

    // possible cards
    int* p1 = cards1[a1];
    int* p2 = cards2[a2];

    int card = 0;

    for (int i = 0; i < 4 && card >= 0; ++i) {
      for (int j = 0; j < 4 && card >= 0; ++j) {
        if (p1[i] == p2[j])
          // we have a match
          card = (card != 0) ? (-1) : (p1[i]);
      }
    }

    if (card > 0) {
      O << "Case #" << (t + 1) << ": " << card << endl;
      cout << "Case #" << (t + 1) << ": " << card << endl;
    }
    else if (card == 0) {
      O << "Case #" << (t + 1) << ": Volunteer cheated!" << endl;
      cout << "Case #" << (t + 1) << ": Volunteer cheated!" << endl;
    }
    else {
      O << "Case #" << (t + 1) << ": Bad magician!" << endl;
      cout << "Case #" << (t + 1) << ": Bad magician!" << endl;
    }
  }


  I.close();
  O.close();
  return 0;
}