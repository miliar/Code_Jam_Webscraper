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

long long int GCD(long long int a,long long int b) {
  while ((a>0)&&(b>0))
    if (a>b) a%=b; else b%=a;
  return a+b;
}

int GetAnswer(const std::vector<std::string>& data,std::vector<bool>& used,std::string& str) {
  int result=0;
  bool allUsed=true;
  
  for (std::size_t index=0;index<data.size();++index) if (!used[index]) {
    bool flag=true;
    char previousCharacter=0;
    
    allUsed=false;
    
    for (std::size_t charIndex=0;charIndex<data[index].size();++charIndex) {
      if (data[index][charIndex]!=previousCharacter) {
        if (data[index][charIndex]==data[index][0]) {
          std::size_t position=str.find(data[index][charIndex]);
          
          if (position!=str.npos)
            while (position<str.size()) if (str[position++]!=data[index][charIndex]) flag=false;
        } else flag=flag&&(str.find(data[index][charIndex])==str.npos);
        
        previousCharacter=data[index][charIndex];
      }
    }
    
    if (flag) {
      used[index]=true;
      str+=data[index];
      result+=GetAnswer(data,used,str);
      str.resize(str.size()-data[index].size());
      used[index]=false;
    }
  }
  
  if (allUsed) {
    return 1;
  }
  
  return result;
}

void Solve(std::ifstream& input,std::ofstream& output) {
  int N;
  std::vector<std::string> data;
  
  input>>N;
  while (N-->0) {
    std::string s;
    input>>s;
    data.push_back(s);
  }
  
  std::vector<bool> used(data.size());
  
  for (std::size_t index=0;index<data.size();++index) {
    bool flag=true;
    
    for (char ch='a';ch<='z';++ch) {
      std::size_t i=1000;
      for (std::size_t charIndex=0;charIndex<data[index].size();++charIndex)
        if (data[index][charIndex]==ch) {
          if (i==1000) i=charIndex;
          if (i+1<charIndex) {
            flag=false;
          } else i=charIndex;
        }
    }
    
    if (!flag) {
      output<<"0";
      return;
    }
  }
  
  std::string str;
  
  output<<GetAnswer(data,used,str);
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