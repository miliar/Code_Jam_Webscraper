#include <iostream>
#include <fstream>
#include <stdlib.h>
#define file  "A-large.in"
#define printForever "INSOMNIA"
using namespace std;


int main (int argc , char ** argv ){

 string word;
 int numberOfCases,temp = 0;
 ifstream inputFile(file);
 
 if(!inputFile.is_open()){
   cout<<"File not found";
   return 0;
 }

 inputFile>>word;
 numberOfCases = atoi(word.c_str());
 
 for(int i=1;i<=numberOfCases;i++){
 

  inputFile>>word;
  int num = atoi(word.c_str());
  
  if(num == 0){
  cout<<"Case #"<<i<<": "<<printForever<<endl;
  continue;
  }
  
  int m = 1;
  int tempNum = num;
  while(1){
  
  while(tempNum != 0){
  int digit = tempNum % 10;
  tempNum = tempNum/10;
  temp |= 1<<digit;
  }
  
  if(temp == 1023){
    cout<<"Case #"<<i<<": "<<m*num<<endl;
    temp = 0;
    break;
  }
  m++;
  tempNum = m * num;
  
  }
  
  
  
 }
 
 
 }
 
