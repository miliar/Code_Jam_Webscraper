#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
  ifstream myfile("D-small-attempt0.in");
  ofstream of("output");
  int testcases;
  myfile >> testcases;
  int X;
  int R;
  int C;
  int casenum = 1;
  while(myfile >> X >> R >> C) {
    bool ret = false;
    if ((R*C)%X != 0)
      ret = false;
    else if (X <= 2) {
      ret = true;
    }
    else {
      if (X == 3) {
	if (C == 1 || R == 1)
	  ret = false;
	else
	  ret = true;
      }
      else{
	if (C*R<12)
	  ret = false;
	else
	  ret = true;	
      }	
    }
    if (ret)
      of <<"Case #"<<casenum <<": GABRIEL"<<std::endl;
    else
      of <<"Case #"<<casenum <<": RICHARD"<<std::endl;
    casenum++;
  }
  return 0;
}
