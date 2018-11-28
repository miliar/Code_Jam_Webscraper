#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#include <string>
#include <sstream>
#include <gmpxx.h>
#include <iostream>
#include <vector>
#include <algorithm>

std::vector<int> v;
std::vector<mpz_class> vec;

bool is_palindrome(mpz_class *lnum, bool count) {

  std::string number;
  std::stringstream strstream;
  strstream << *lnum;
  strstream >> number;


  int i = strlen(number.c_str());
  if (count)
  v[i]++;
  i--;
  for (int j = 0; j <= i/2; j++) {
    if (number.c_str()[j] != number.c_str()[i]) {
      return false;
    }
    i--;
  }
  return true;
}

int main () {
  v.resize(20);
 
  mpz_class x("0");
  mpz_class y("1");
 



  while(x < 1000000) {
    
    x++; 
    y=x*x;
    
    if (is_palindrome( &x, false ) && is_palindrome( &y, true )) {
      //printf("%llu \n", i*i );
      //        std::cout << "    = " << y << std::endl;	    
      vec.push_back(y);
    }
    
  }
  
  int N;
  scanf("%d", &N);
  int I = 0;
  while (N-- > 0) {

    unsigned long  r1, r2;
    scanf("%lu %lu", &r1, &r2);
    
    mpz_class mpz_r1(r1);
  mpz_class mpz_r2(r2);


    std::vector<mpz_class>::iterator low,up;
    low=std::lower_bound(vec.begin(), vec.end(), mpz_r1);
    up= std::upper_bound(vec.begin(), vec.end(), mpz_r2); 
    printf("Case #%d: ", I+1);

    printf("%d\n", up-low);
    /*
    while (low != up) 
      std::cout << *(low++) << " ";
    
    std::cout << std::endl;
    */
    I++;
  }
  
  //  for (int i = 0; i < v.size(); i++ ) {
  //   printf("v[%d] = %d\n", i, v[i]);
  // }

}
