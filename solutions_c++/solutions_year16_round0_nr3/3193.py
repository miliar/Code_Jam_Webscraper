//============================================================================
// Name        : google jam
// Author      : mohahamd
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

using std::string;
std::vector<size_t> primes = {1};
size_t is_prime(size_t x) {
  size_t q,r;
  for(int i = 2;true;i++) {
      q = x / i;
      r = x % i;
      if(r == 0) return i;
      if(i > q) return 0;
  }
}
size_t power(int x, int a){
  if(a==0) return 1;
   return a==1 ? static_cast<size_t>(x) :((a%2==0)? power(x*x,a/2):x*power(x*x,a/2));
}
void next(std::vector<size_t>& numbers, const int N = 16) {
  numbers[0] += 2;
  for(int i = 1; i < 9 ; ++i) {
      numbers[i] = 0;
      for(int j =0 ; j < N ; ++j) {
          numbers[i] += (( numbers[0] >> j) & 1)*power(i+2,j);
      }
  }
}
int main(int argc, char* argv[])
{
  std::ofstream ofs("input/output6.txt");
  const int N=16;
  int J = 50;
  std::vector<size_t> tab(9);
  for(int i = 0 ; i < 9 ; ++i) tab[i] = power(i+2,N-1) + 1;
  ofs << "Case #" << 1 << ": "<<std::endl;
  while(J > 0) {
      std::ostringstream tss;
      bool good = true;
      for(int i = 0 ; i < 9 ; ++i) {
          size_t d =is_prime(tab[i]);
          if(d==0) {good=false;break;}
          tss << " " << d;
      }
      if(good) {ofs << tab[8] << tss.str() << std::endl;J--;}
      next(tab,N);
  }
 //ofs << "Case #" << 1 << ": "<<res<<std::endl;
  return 0;
}
