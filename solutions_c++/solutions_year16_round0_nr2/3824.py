#include<stdio.h>
#include<fstream>
#include<vector>
#include<algorithm>
#include<map>
#include<string>
#include<iostream>
using namespace std;
int main(){
  ofstream result;
  result.open("revengeOfThePancakes.txt");
  int T,M=0;
  int flips,len;
  char currentChar;
  string input;
  scanf("%d",&T);
  while(T--){
   cin>>input; 
   flips=0;
   len = input.length();
   currentChar = input[0];
   
   for(int i=1; i<len; i++){
     if(input[i]==currentChar){continue;}
     else{
       flips++;
       while(currentChar != input[i] && i<len){i++;}       
       i--;
       currentChar = input[i];
     }
   }
   if(currentChar=='-'){flips++;}
   result<<"Case #"<<++M<<": "<<flips<<"\n";
  }
}
