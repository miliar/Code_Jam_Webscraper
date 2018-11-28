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
  std::ifstream ifs("input/input4.txt");
  std::ofstream ofs("input/output4.txt");
  int T;
  ifs >> T;
  for(int i = 0; i < T ; ++i)
    {
      string pancakes;
      ifs >> pancakes;
      size_t res = 0;
      auto it = std::unique(pancakes.begin(),pancakes.end());
      pancakes.resize( std::distance(pancakes.begin(),it) );
      if(pancakes[0]=='-')      res= (pancakes.size()-pancakes.size()/2 -1)*2 + 1;
      else res= (pancakes.size()!=1)*(pancakes.size()/2)*2;
      ofs << "Case #" << i+1 << ": "<<res<<std::endl;
    }
  return 0;
}
