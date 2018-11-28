#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>

long long int MakePalindrome(int number,bool trim) {
  std::vector<int> digits;
  long long int result=0;
  
  while (number>0) {
    result=10*result+(number%10);
    digits.push_back(number%10);
    number/=10;
  }
  
  while (!digits.empty()) {
    if (!trim) {
      result=result*10+(*digits.rbegin());    
    } else trim=false;
    digits.pop_back();
  }
  
  return result;
}

bool IsPalindrome(long long int number) {
  std::vector<int> digits;
  
  while (number>0) {
    digits.push_back(static_cast<int>(number%10));
    number/=10;
  }
  
  for (size_t index=0;2*index<digits.size();++index)
    if (digits[index]!=digits[digits.size()-index-1]) return false;
  
  return true;
}

void SolveTask(std::ifstream& input,std::ofstream& output) {
  int a,b;
  int result=0;
  
  input>>a>>b;
  if (a>b) std::swap(a,b);
  
  for (int palindromeBase=1;palindromeBase<100000;++palindromeBase) {
    long long int candidate=MakePalindrome(palindromeBase,false)*MakePalindrome(palindromeBase,false);
    if ((candidate>=a)&&(candidate<=b)&&IsPalindrome(candidate)) ++result;
        
    candidate=MakePalindrome(palindromeBase,true)*MakePalindrome(palindromeBase,true);
    if ((candidate>=a)&&(candidate<=b)&&IsPalindrome(candidate)) ++result;
    
    if (candidate>b) break;
  }
  
  output<<result;
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