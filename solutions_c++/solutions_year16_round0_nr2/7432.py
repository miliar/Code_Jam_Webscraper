#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <stack>
#include <list>
#define file  "B-large.in"
using namespace std;


int main (int argc , char ** argv ){

 string word;
 int numberOfCases,temp = 0;
 int sign = 1;
 ifstream inputFile(file);
 
 if(!inputFile.is_open()){
   cout<<"File not found";
   return 0;
 }

 inputFile>>word;
 numberOfCases = atoi(word.c_str());
 
 for(int i=1;i<=numberOfCases;i++){
  inputFile>>word;
  stack<int> st;
  stack<int> flipStack;
  stack<int> tempStack;
  int wordLen = word.length();
  int count=0;
 
  for(int j=0;j<wordLen;j++){
   
  if(word.at(j)=='-') {
  sign =-1;
  }
  else {
  sign = 1;
  }
  st.push(sign);

  }

  while(!st.empty()){
  //flip pancackes
  if(st.top() == -1 ){
  count++; 
  while(!st.empty()){
   flipStack.push(-1 * st.top());
   st.pop();
   }
  while(!flipStack.empty()){
   st.push(flipStack.top());
   flipStack.pop();
   }
  }


  while(!st.empty() && st.top() == 1){
  tempStack.push(st.top());
  st.pop();
  }


  }
  
 cout<<"Case #"<<i<<": "<<count<<endl;
  
  
  
 }
 
 
 }
 
