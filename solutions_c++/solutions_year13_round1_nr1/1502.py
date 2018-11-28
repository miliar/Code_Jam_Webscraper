#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <map>
using namespace std;

#define ccout cout<<"Case #"<<tc<<": "

int main(){
  int t;
  cin >> t;
  
  for(int tc=1 ; tc<=t ; ++tc){
      long r,t;
      cin >> r >> t;
      long c = 0,r2;
      long v;
      while(t){
	  r2 = r + 1;
	  v = r2*r2 - r*r;
	  if(t-v < 0)
	      break;
	  t -= v;
	  r = r2 + 1;
	  ++c;
      }
      ccout << c << endl;
  }
  
  return 0;
}
