#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;

bool isPalindrome(int j);
string integerToString(int integer);
bool isSquareOfPalindrome(int integer);
int main(){
   ifstream infile;
   ofstream outfile;
   outfile.open("output.in");
   infile.open("input.in");
   int testCases;
   infile>>testCases;
   int counter=0; 
   for(int i=0;i<testCases;i++){
      int a,b;
	  infile>>a;
	  infile>>b;
	  for(int j=a;j<=b;j++){
	     if(isPalindrome(j)&&isSquareOfPalindrome(j)){
		    counter++;
		 }
	  }
      outfile<<"Case #"<<i<<": "<<counter<<endl;
	  counter=0;
   }
   infile.close();
   return 0;
}

bool isPalindrome(int j){
   string integerString = integerToString(j);
   for(int i=0;i<(integerString.length()/2);i++){
      if(integerString[i]!=integerString[integerString.length()-i-1])
	     return false;
   }
   return true;
}
bool isSquareOfPalindrome(int integer){
	if(sqrt(double(integer))==floor(sqrt(double(integer)))){
		if(isPalindrome(int(sqrt(double(integer)))))
			return true;
		else
			return false;
	}else{
	   return false;
	}
}
string integerToString(int integer){
	int oldInt = integer;
	string integerInStringForm="";
	while(integer>0){
	   char lastChar = char('0'+integer%10);
	   integerInStringForm=lastChar+integerInStringForm;
	   integer/=10;
	}
	return integerInStringForm;
}
