//
//  main.cpp
//  CGJ_C
//
//  Created by Volodya Karpliuk on 4/13/13.
//  Copyright (c) 2013 Volodya Karpliuk. All rights reserved.
//

#include <iostream>
#include <math.h>
using namespace std;
#include <fstream>


bool isPalindrome (int number);

int main(int argc, const char * argv[]) {
  
  ifstream in;
  in.open("/Users/keyv/Documents/GCJ/CGJ_C/CGJ_C/C-small-attempt7.in");
  in >> fixed >> showpoint;

  
  ofstream out;
  out.open("/Users/keyv/Documents/GCJ/CGJ_C/CGJ_C/test.txt");
 
  int t;
  in>>t;
  
  int *results = new int[t];
  
  for (int i = 0; i <t; i++) {
    int a,b;
    in>>a;
    in>>b;
    
    int palindromeCount = 0;
    
    for (int j = a; j <=b; j++) {
      double param = sqrt((double)j);
      double fractpart, intpart;
      fractpart = modf(param , &intpart);
      if (fractpart == 0.0f)
        if (isPalindrome(j)) {
          if(isPalindrome((int)intpart))
            palindromeCount++;
        }
    }
    results[i] = palindromeCount;
  }
  
  
  for (int i = 0; i < t; i++) {
    out<<"Case #"<<(i+1)<<": "<<results[i]<<endl;
//    
//    fprintf(out, , , );
  }
  delete []results;
  out.close();
  in.close();
  return 0;
}

bool isPalindrome (int number) {
  bool result;
  
  int rem,sum=0,numCopy;    //Defining variables.
  numCopy=number;
  while(number!=0)    //Loop to reverse the number.
  {
    rem=number%10;
    number=number/10;
    sum=sum*10+rem;
  }
  //Result Display:
  if(numCopy==sum)
    result = true;
  else
    result = false;  
  return result;  
}

