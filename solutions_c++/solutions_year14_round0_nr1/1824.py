#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;

ifstream in("data.in");
ofstream out("data.out");

int main() {
  int T;
  in >> T;
  for (int c = 1; c <= T; c++) {
    vector<bool> possible(17,1);
    int currow,curval;
    for (int n=0; n<2; n++) {
      in >> currow;
      for (int i=1; i<=4; i++) {
	for (int j=1; j<=4; j++) {
	  in >> curval;
	  if (i!=currow) {
	    possible[curval] = 0;
	  }
	}
      }
    }
    int numpossible = 0,whichisit;
    for (int i=1; i<=16; i++) {
      if (possible[i]) {
	numpossible++;
	whichisit = i;
      }
    }
    
    out << "Case #" << c << ": ";
    if (numpossible == 0) {
      out << "Volunteer cheated!" << endl;
    } else if (numpossible == 1) {
      out << whichisit << endl;
    } else {
      out << "Bad magician!" << endl;
    }
  }
}
