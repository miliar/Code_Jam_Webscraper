#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <math.h>
using namespace std; 
#define ull unsigned long long int
bool chk_square(ull num){
  long double num1 = sqrt(num);
  return (num1*num1 == num);
}
bool chk_palindrome(ull num){
 ull rev=0,numcpy=num;
 int digit;
 do{digit = num%10; rev = (rev*10)+digit; num = num/10;} while (num !=0);
 return (rev==numcpy);
}


int main(){
int cases; 
cin>>cases;
for(int casenum=1;casenum<=cases;casenum++){
  ull lower,upper;
  cin>>lower>>upper;
  int countnum=0;
  for(ull num=lower;num<=upper;num++){
      if(num%10!=4  &&  num%10!=6 && num%10!=9 && num%10!=1) continue;
      if(chk_palindrome(num)&& chk_palindrome(sqrt(num))&&chk_square(num))
      {
          //cout<<num<<endl;
          countnum++;}
  }
  cout<<"Case #"<<casenum<<": "<<countnum<<endl;
}
}
