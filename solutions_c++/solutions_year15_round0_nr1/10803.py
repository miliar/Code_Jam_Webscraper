#include <iostream>
#include <vector>
#include <string>
#include <fstream>

int main(){
  std::ifstream file;
  file.open("input.in", std::ios::out);
  int T = 0;
  int caseCounter = 1;
  file >> T;
  while(T--){
    int sMax = 0;
    std::string shy;
    std::string::iterator s_itr = shy.begin();
    std::vector<int> shyVec;
    file >> sMax >> shy;
    while(s_itr != shy.end()){
      shyVec.push_back(*s_itr - '0');
      s_itr++;
    }
    int counter = 0;
    int invite = 0;
    for(int x = 0; x < shyVec.size(); x++){
      int total = counter+invite;
      if(total >= x){
        counter += shyVec[x];
      } else {
        invite = x-counter;
        counter += shyVec[x];
      }
      
    }
    std::cout << "Case #" << caseCounter << ": " << invite << "\n";
    caseCounter++;
  }
}