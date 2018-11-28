#include <algorithm>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>

void Solve(std::ifstream& input,std::ofstream& output) {
  double C,F,X;
  
  input>>C>>F>>X;
  
  double previous=std::numeric_limits<double>::max();
  double cookieTime=0;
  double time=0;
  
  int N=0;
  
  do {
    time=cookieTime+X/(2+F*N);
    if (time>previous) {
      output<<std::fixed<<std::setprecision(7)<<previous;
      break;
    }
    cookieTime+=C/(2+F*N);
    previous=time;
    ++N;
  } while (N>0);
}

void main() {
  std::ifstream input("Input.Txt");
  std::ofstream output("Output.Txt");
  int testCases;
  
  input>>testCases;
  
  for (int testCase=1;testCase<=testCases;++testCase) {
    output<<"Case #"<<testCase<<": ";
    Solve(input,output);
    output<<std::endl;
  }
}