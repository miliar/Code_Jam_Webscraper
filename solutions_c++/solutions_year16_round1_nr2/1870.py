#include<iostream>
#include<string>
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
  int N;
};

void core(InputData& in) {
  std::vector<int> vec;
  std::vector<int> vec2;
  for(int i=0; i < in.N * 2 - 1; i++)
  {
    for(int j=0; j < in.N; j++)
    {
      int val;
      std::cin >> val;
      vec.push_back(val);
      vec2.push_back(val);
    }
  }
  std::vector<int>::iterator it;
  std::sort(vec.begin(), vec.end());
  it = std::unique(vec.begin(), vec.end());
  vec.resize(std::distance(vec.begin(), it));
  std::vector<int>outVec;
  for(auto& i: vec)
  {
    int count = std::count(vec2.begin(), vec2.end(), i);
    if(count%2)
      std::cout << " " << i;
  }
}

int main() 
{
  int T;
  std::cin >> T;
  for (int tc = 1; tc <= T; tc ++)
  {
    std::cout << "Case #" << tc << ":";
    struct InputData input;
    std::cin >> input.N;
    core(input);
    std::cout << std::endl;
  }
  return 0;
}

