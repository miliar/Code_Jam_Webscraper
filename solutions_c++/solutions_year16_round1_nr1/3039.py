#include <deque>
#include <iostream>
#include <string>

std::string lastword(std::string k){
  std::deque<char> word;
  for(auto c : k){
    if(word.empty())
      word.push_back(c);
    else if(word.front() <= c)
      word.push_front(c);
    else
      word.push_back(c);
  }
  return std::string(word.begin(), word.end());
}

int main(){
  int t;
  std::cin >> t;
  std::cin.ignore();
  std::string in;
  for(int i = 1; std::getline(std::cin, in); ++i){
    std::cout << "Case #" << i << ": " << lastword(in) << "\n";
  }
  return 0;
}

