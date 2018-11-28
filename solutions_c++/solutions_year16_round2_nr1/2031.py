#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

void proc(ifstream& ifile) {
  int t = 0, x = 1;
  ifile >> t;
  for(int i = 0; i < t; ++i) {
    cout << "Case #" << (x++) << ": ";
    //// TODO ////
    string S;
    ifile >> S;
    // Z0, E0135789, R034, O0124, N179, T238, W2, H38, F45, U4, I5689, V57, S67, X6, G8
    // Z, E, R, O, N, T, W, H, F, U, I, V, S, X, G
    vector<int> digits(10, 0), letters(26, 0);
    for(int j = 0; j < S.length(); ++j) { ++letters[(int)(S[j]-'A')]; }
    //0
    if(letters[(int)('Z'-'A')] > 0) {
      digits[0] += letters[(int)('Z'-'A')];
      int tmp = letters[(int)('Z'-'A')];
      letters[(int)('Z'-'A')] -= tmp;
      letters[(int)('E'-'A')] -= tmp;
      letters[(int)('R'-'A')] -= tmp;
      letters[(int)('O'-'A')] -= tmp;
    }
    //2
    if(letters[(int)('W'-'A')] > 0) {
      digits[2] += letters[(int)('W'-'A')];
      int tmp = letters[(int)('W'-'A')];
      letters[(int)('T'-'A')] -= tmp;
      letters[(int)('W'-'A')] -= tmp;
      letters[(int)('O'-'A')] -= tmp;
    }
    //4
    if(letters[(int)('U'-'A')] > 0) {
      digits[4] += letters[(int)('U'-'A')];
      int tmp = letters[(int)('U'-'A')];
      letters[(int)('F'-'A')] -= tmp;
      letters[(int)('O'-'A')] -= tmp;
      letters[(int)('U'-'A')] -= tmp;
      letters[(int)('R'-'A')] -= tmp;
    }
    //6
    if(letters[(int)('X'-'A')] > 0) {
      digits[6] += letters[(int)('X'-'A')];
      int tmp = letters[(int)('X'-'A')];
      letters[(int)('S'-'A')] -= tmp;
      letters[(int)('I'-'A')] -= tmp;
      letters[(int)('X'-'A')] -= tmp;
    }
    //8
    if(letters[(int)('G'-'A')] > 0) {
      digits[8] += letters[(int)('G'-'A')];
      int tmp = letters[(int)('G'-'A')];
      letters[(int)('E'-'A')] -= tmp;
      letters[(int)('I'-'A')] -= tmp;
      letters[(int)('G'-'A')] -= tmp;
      letters[(int)('H'-'A')] -= tmp;
      letters[(int)('T'-'A')] -= tmp;
    }
    //1
    if(letters[(int)('O'-'A')] > 0) {
      digits[1] += letters[(int)('O'-'A')];
      int tmp = letters[(int)('O'-'A')];
      letters[(int)('O'-'A')] -= tmp;
      letters[(int)('N'-'A')] -= tmp;
      letters[(int)('E'-'A')] -= tmp;
    }
    //3
    if(letters[(int)('R'-'A')] > 0) {
      digits[3] += letters[(int)('R'-'A')];
      int tmp = letters[(int)('R'-'A')];
      letters[(int)('T'-'A')] -= tmp;
      letters[(int)('H'-'A')] -= tmp;
      letters[(int)('R'-'A')] -= tmp;
      letters[(int)('E'-'A')] -= tmp;
      letters[(int)('E'-'A')] -= tmp;
    }
    //5
    if(letters[(int)('F'-'A')] > 0) {
      digits[5] += letters[(int)('F'-'A')];
      int tmp = letters[(int)('F'-'A')];
      letters[(int)('F'-'A')] -= tmp;
      letters[(int)('I'-'A')] -= tmp;
      letters[(int)('V'-'A')] -= tmp;
      letters[(int)('E'-'A')] -= tmp;
    }
    //7
    if(letters[(int)('V'-'A')] > 0) {
      digits[7] += letters[(int)('V'-'A')];
      int tmp = letters[(int)('V'-'A')];
      letters[(int)('S'-'A')] -= tmp;
      letters[(int)('E'-'A')] -= tmp;
      letters[(int)('V'-'A')] -= tmp;
      letters[(int)('E'-'A')] -= tmp;
      letters[(int)('N'-'A')] -= tmp;
    }
    //9
    if(letters[(int)('I'-'A')] > 0) {
      digits[9] += letters[(int)('I'-'A')];
      int tmp = letters[(int)('I'-'A')];
      letters[(int)('N'-'A')] -= tmp;
      letters[(int)('I'-'A')] -= tmp;
      letters[(int)('N'-'A')] -= tmp;
      letters[(int)('E'-'A')] -= tmp;
    }
    for(int j = 0; j < 10; ++j) {
      if(digits[j] > 0) {
        for(int k = 0; k < digits[j]; ++k) cout << j;
      }
    }
    //////////////
    cout << endl;
  }
}

int main(int argc, char** argv) {
  if(argc != 2) { cerr << "Wrong usage." << endl; }
  ifstream ifile(argv[1]);

  proc(ifile);

  return 0;
}
