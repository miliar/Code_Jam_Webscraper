#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <math.h>

using namespace std;

int ispalindrome(string str){
  
  int l=str.size();
  int resp=1;
  int half=l/2;
  for(int k=0;k<half;++k){
    if(str.at(k)!=str.at(l-k-1))resp=0;
  }
  return resp;
}


int main(){

  
  ifstream input("input.in",ios::in);
  ofstream output("output.out", ios::out);
  
  int T;
  int A, B;
  double a, b;
  
  int square;
  
  input>>T;
  for(unsigned t=0; t<T; ++t){
    
    input>>A;
    input>>B;
    
    a=sqrt((double)A);
    b=sqrt((double)B);
    
   
    int ans=0;
    
    for(int i=(int)ceil(a-.000001);i<(int)ceil(b+.000001);++i){
      ostringstream oss;
      oss<<i;
      string s = oss.str();
      if(ispalindrome(s)){
	cout<<s<<"\n";
	square=i*i;
	ostringstream oss2;
        oss2<<square;
        string s2 = oss2.str();
	if(ispalindrome(s2)){
	  cout<<s2<<"\n";
	  ans++;
	}
	
      }
      
    }
    
    
    output<<"Case #"<<t+1<<": "<<ans<<"\n";
  } 
  
  return 1;

}