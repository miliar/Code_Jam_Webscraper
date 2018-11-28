//============================================================================
// Name        : google jam
// Author      : jamcoin
// Version     : Revenge of the Pancakes
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <sstream>
#include <array>
#include <fstream>
#include <utility>
#include <algorithm>
#include <vector>
#include <cmath>

using std::string;

size_t power(int x, int a){
  if(a==0) return 1;
   return a==1 ? static_cast<size_t>(x) :((a%2==0)? power(x*x,a/2):x*power(x*x,a/2));
}

int main(int argc, char* argv[])
{
  std::ifstream ifs("input/input7.txt");
  std::ofstream ofs("input/output7.txt");
  int T;
  ifs >> T;
  for(int i = 1; i <= T ; ++i)
    {
      int K,C,S;
      ifs >> K >> C >> S;
      size_t step = (size_t)pow(K,C-1);
      ofs << "Case #" << i << ":";
      for(int j = 0; j < K ; ++j) {
          ofs << " "<< static_cast<size_t>(step*j + 1);
      }
      ofs << std::endl;
    }
  return 0;
}

