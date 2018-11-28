//============================================================================
// Name        : google jam
// Author      : mohahamd
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <sstream>
#include <set>
#include <fstream>
#include <utility>
#include <algorithm>
#include <vector>

using std::string;

int main(int argc, char* argv[])
{
  std::ifstream ifs("input/input2.txt");
  std::ofstream ofs("input/output2.txt");
  std::set<char> numbers;
  int T;
  ifs >> T;
  for(int i = 0; i < T ; ++i)
    {
      size_t N;
      ifs >> N;
      if(N==0) { ofs << "Case #" << i+1 << ": "<<"INSOMNIA"<<std::endl;continue;}
      size_t res = 0;
      std::ostringstream oss;
      while(numbers.size() < 10) {
          res+=N;
          oss << res;
          const string& tmp = oss.str();
          for(size_t j = 0 ; j < tmp.size() ;++j)
          {
            numbers.insert(tmp[j]);
          }
      }
      ofs << "Case #" << i+1 << ": "<<res<<std::endl;
      numbers.clear();
    }
  return 0;
}
