#include<iostream>
#include<string>
#include<cstring>
#include<sstream>
#include<fstream>
#include<vector>
#include<algorithm>
#include<cassert>
#include<cstdint>

int str2int(std::string s) {
  int value;
  std::istringstream(s) >> value;
  return value;
}

struct InputData {
  std::string str;
};

void core(InputData& in) {
  std::vector<char> vec;
  for(char &c : in.str)
  {
    if(vec.size()==0)
      vec.push_back(c);
    else
    {
     if(c >= vec.front())
       vec.insert(vec.begin(),c);
     else
       vec.push_back(c);
    }
  }
  for(auto i=vec.begin(); i!= vec.end(); i++)
    std::cout << *i;
}

int main() 
{
  int T;
  std::cin >> T;
  for (int tc = 1; tc <= T; tc ++)
  {
    std::cout << "Case #" << tc << ": ";
    struct InputData input;
    std::cin >> input.str;
    core(input);
    std::cout << std::endl;
  }
  return 0;
}

