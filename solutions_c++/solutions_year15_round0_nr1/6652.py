#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <string.h>
#include <cstdlib>
#include <map>

using namespace std;

int main(int argc, char const* argv[])
{
  std::ifstream ifs("input.txt");
  std::string str;
  if(ifs.fail()) {
    std::cerr << "can't read files " << std::endl;
    return -1;
  }
  getline(ifs, str);
  std::cout << str << std::endl;
  long long probNum = 1;
  while ( getline(ifs, str))
  {
    std::stringstream ss(str);
    std::string maxLevel, data;
    ss >> maxLevel;
    ss >> data;

    long long total = 0;
    long long i;
    for(i = 0; i < (long long)data.size(); i++) {
      char c = data[i];
      long long val = std::atoi(&c);
      total += val;
    }
    i--;

#if 0
    std::cout << "total:" << total << std::endl;
    std::cout << "i:" << i << std::endl;
#endif

    long long result = 0;
    for(; i >= 0; i--) {
      char c = data[i];
      total = total - std::atoi(&c);
      if( i > total) {
#if 0
        std::cout << i << " - " << total <<  std::endl;
#endif
        long long add = i - total;
        result += add;
        total += add;
#if 0
        std::cout << "result:" << result << std::endl;
#endif
      }
    }

    std::cout << "Case #" << probNum++ << ": " << result << std::endl;

    //std::cout << maxLevel << ":" << data << std::endl;
    //std::cout << total << std::endl;
  }
  return 0;
}
