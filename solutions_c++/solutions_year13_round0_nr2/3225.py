#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>

void SolveTask(std::ifstream& input,std::ofstream& output) {
  std::vector<std::vector<int> > lawn;
  
  int n,m;
  input>>n>>m;
  
  for (int index=0;index<n;++index) {
    std::vector<int> row;
    for (int index2=0;index2<m;++index2) {
      int cell;
      input>>cell;
      row.push_back(cell);
    }
    lawn.push_back(row);    
  }
  
  bool evaluating;
  do {
    evaluating=false;
    int minIndex=0;
    int minIndex2=0;
    
    for (int index=0;index<n;++index)
      for (int index2=0;index2<m;++index2)
        if (lawn[index][index2]!=0)
          if (evaluating) {
            if (lawn[minIndex][minIndex2]>lawn[index][index2]) {
              minIndex=index;
              minIndex2=index2;
            }
          } else {
            minIndex=index;
            minIndex2=index2;
            evaluating=true;
          }
    
    if (evaluating) {
      bool canCut=true;
      
      for (int index=0;index<n;++index) canCut=canCut&&(lawn[index][minIndex2]<=lawn[minIndex][minIndex2]);
      
      if (canCut) {
        for (int index=0;index<n;++index) lawn[index][minIndex2]=0;
      } else {
        canCut=true;
        for (int index2=0;index2<m;++index2) canCut=canCut&&(lawn[minIndex][index2]<=lawn[minIndex][minIndex2]);
        
        if (canCut){
          for (int index2=0;index2<m;++index2) lawn[minIndex][index2]=0;
        } else {
          output<<"NO";
          return;
        }        
      }
    }
  } while (evaluating);
  
  output<<"YES";
}

void main() {
  std::ifstream input("Input.Txt");
  std::ofstream output("Output.Txt");
  
  int numberOfCases;  
  input>>numberOfCases;
  
  for (int caseNumber=1;caseNumber<=numberOfCases;++caseNumber) {
    output<<"Case #"<<caseNumber<<": ";
    SolveTask(input,output);
    output<<std::endl;
  }
}