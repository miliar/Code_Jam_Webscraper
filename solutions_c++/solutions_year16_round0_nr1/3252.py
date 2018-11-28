//
//  main.cpp
//  codeJam
//
//  Created by Emanuele Dalmasso on 09/04/16.
//  Copyright © 2016 Dalmax.Net. All rights reserved.
//

#include <iostream>
using namespace std;

bool digits[10];


bool updateDigits(uint64_t v){
  while(v){
    digits[v%10]=true;
    v/=10;
  }
  for(int i=0;i<10;++i)
    if(!digits[i])
      return false;
  return true;
  
}


int main(int argc, const char * argv[]) {
  int t;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    uint64_t n;
    cin >> n;  // read n.
    bool imsomnia = false;
    for(int i=0;i<10;++i)
      digits[i]=false;
    if(n!=0){
   
      uint64_t k=n;
      for(;!updateDigits(k);k+=n)
      {      }
      cout << "Case #" << i << ": " << k << endl;
    }
    else{
      imsomnia = true;
    }
    if(imsomnia)
      cout << "Case #" << i << ": INSOMNIA" << endl;
    
  }
  return 0;
}


