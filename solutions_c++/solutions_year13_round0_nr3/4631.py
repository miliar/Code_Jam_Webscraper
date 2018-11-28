#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdlib>
using namespace std;

#include <sstream>

bool palindrome(int i)
{

  std::string s;
  std::stringstream out;
  out << i;
  s = out.str();
  
  int j=0,k=s.size()-1;

  while (j<k && s[j] == s[k]) { j++; k--; } 

  return (j>=k)?true:false;  
}

int main(int argc , char ** argv){
  ifstream fi(argv[1]);
  int T;
  long int A,B;
  string line;

  fi >> T;
  for(int i=0;i<T;++i){
   
    fi >> A >> B ;
    int low_min_A = (sqrt(A) > ((int) sqrt(A)) ) ? sqrt(A) + 1: sqrt(A); 
    int count =0;
    for(int j=low_min_A;j<=sqrt(B);j++)
      if( palindrome(j) && palindrome(j*j))
	count++;
    
    cout << "Case #" << i+1 << ": " << count << endl; 
  }

  fi.close();
}
