#include <iostream>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;

bool check(size_t Sn);

int main() {
  int cases;
  int number=1;
  cin >> cases;
while(cases--){
  size_t A, B;
  cin >> A >> B;
  size_t n=sqrt(A);
  if (n*n<A) n++;
  size_t Sn1=n*n;
  size_t an=Sn1*2/n-1;
  size_t count=0;
  for(size_t Sn=Sn1;Sn<=B;Sn+=an){
    if (check(Sn)) {
      size_t root=sqrt(Sn);
      if (check(root)) count++;
    }   
    an+=2;    
  }
  cout<< "Case #" << number <<": " << count << endl;
  number++; 
}
  return 0;
}
 
 
bool check(size_t Sn){
  ostringstream convert;
  convert << Sn;
  string str=convert.str();
  size_t length=str.length();
  string::reverse_iterator rit=str.rbegin();
  string::iterator it=str.begin();  
  for(size_t i=1;i<=length/2;i++ ){
    if (*(it++)==*(rit++)) {
      continue;
    } else {
      return false;
    }
  }
  return true;
}
