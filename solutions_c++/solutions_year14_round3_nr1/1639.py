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
#include <string>
#include <vector>

int GCD(int a,int b) {
  while ((a>0)&&(b>0))
    if (a>b) a%=b; else b%=a;
  return a+b;
}

void Solve(std::ifstream& input,std::ofstream& output) {
  char c;
  int p,q;
  input>>p>>c>>q;
  
  int gcd=GCD(p,q);
  p/=gcd;q/=gcd;
  
  int counter=0;
  int result=0;
  
  while ((q>1)&&(q%2==0)) {
    q/=2;
    ++counter;
  }
  
  if (q>1) {
    output<<"impossible";
    return;
  }
  
  result=counter;
  while ((1<<result)>p) --result;
  // result=counter-result;
  
  output<<counter-result;
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