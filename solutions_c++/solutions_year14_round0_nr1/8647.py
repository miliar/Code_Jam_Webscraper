#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>

void Solve(std::ifstream& input,std::ofstream& output) {
  int firstRow,secondRow;
  std::vector<std::vector<int> > firstArrangement(4),secondArrangement(4);
  
  for (std::size_t index=0;index<4;++index) {
    firstArrangement[index].resize(4);
    secondArrangement[index].resize(4);
  }
  
  input>>firstRow;
  for (std::size_t index=0;index<4;++index)
    for (std::size_t index2=0;index2<4;++index2)
      input>>firstArrangement[index][index2];
      
  input>>secondRow;
  for (std::size_t index=0;index<4;++index)
    for (std::size_t index2=0;index2<4;++index2)
      input>>secondArrangement[index][index2];
  
  int counter=0;
  int number=0;
  for (std::size_t index=0;index<4;++index)
    for (std::size_t index2=0;index2<4;++index2) {
      if (firstArrangement[firstRow-1][index]==secondArrangement[secondRow-1][index2]) {
        number=firstArrangement[firstRow-1][index];
        ++counter;
      }
    }
  
  switch (counter) {
    case 0: {
      output<<"Volunteer cheated!";
      break;
    }
    case 1: {
      output<<number;
      break;
    }
    default: {
      output<<"Bad magician!";
      break;
    }
  }
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