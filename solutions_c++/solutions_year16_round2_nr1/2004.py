#include <fstream>
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

void removeChar(std::string &s, char p){
  size_t pos = s.find(p);
  if (pos == std::string::npos)
    std::cerr<<"BUG BUG BUG";
  s.erase(pos,1);
}


std::vector<int> ParseString(std::string nS){
  std::vector<int> result;
  while (nS.find('Z')!=std::string::npos){
    result.push_back(0);
    removeChar(nS, 'Z');
    removeChar(nS, 'E');
    removeChar(nS, 'R');
    removeChar(nS, 'O');
  }
  while (nS.find('W')!=std::string::npos){
    result.push_back(2);
    removeChar(nS, 'T');
    removeChar(nS, 'W');
    removeChar(nS, 'O');
  }
  while (nS.find('U')!=std::string::npos){
    result.push_back(4);
    removeChar(nS, 'F');
    removeChar(nS, 'O');
    removeChar(nS, 'U');
    removeChar(nS, 'R');
  }
  while (nS.find('X')!=std::string::npos){
    result.push_back(6);
    removeChar(nS, 'S');
    removeChar(nS, 'I');
    removeChar(nS, 'X');
  }
  while (nS.find('G')!=std::string::npos){
    result.push_back(8);
    removeChar(nS, 'E');
    removeChar(nS, 'I');
    removeChar(nS, 'G');
    removeChar(nS, 'H');
    removeChar(nS, 'T');
  }
  while (nS.find('O')!=std::string::npos){
    result.push_back(1);
    removeChar(nS, 'O');
    removeChar(nS, 'N');
    removeChar(nS, 'E');
  }
  while (nS.find('F')!=std::string::npos){
    result.push_back(5);
    removeChar(nS, 'F');
    removeChar(nS, 'I');
    removeChar(nS, 'V');
    removeChar(nS, 'E');
  }
  while (nS.find('S')!=std::string::npos){
    result.push_back(7);
    removeChar(nS, 'S');
    removeChar(nS, 'E');
    removeChar(nS, 'V');
    removeChar(nS, 'E');
    removeChar(nS, 'N');
  }
  while (nS.find('T')!=std::string::npos){
    result.push_back(3);
    removeChar(nS, 'T');
    removeChar(nS, 'H');
    removeChar(nS, 'R');
    removeChar(nS, 'E');
    removeChar(nS, 'E');
  }
  while (nS.find('N')!=std::string::npos){
    result.push_back(9);
    removeChar(nS, 'N');
    removeChar(nS, 'I');
    removeChar(nS, 'N');
    removeChar(nS, 'E');
  }
  return result;
}



int main(int argc, char *argv[]){
    std::ifstream inF;
    inF.open(argv[1]);
    int n;
    inF>>n;

    for (int i = 1; i <= n; i++){
      std::string nS;
      inF>>nS;
      std::vector<int> parsed = ParseString(nS);
      std::sort (parsed.begin(), parsed.end());
      std::cout<<"Case #"<<i<<": ";
      for (std::vector<int>::iterator it=parsed.begin(); it!=parsed.end(); ++it)
        std::cout<<*it;
      std::cout<<std::endl;
  }

  return 0;
}
