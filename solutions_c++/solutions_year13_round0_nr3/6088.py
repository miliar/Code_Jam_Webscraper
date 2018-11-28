#include <iostream>
#include <sstream>
#include <cstdio>
#include <math.h>

using namespace std;
bool isPal(int n){
  string s;
  stringstream convert;
  convert << n;
  s = convert.str();
  for(int i = 0; i < int(s.size() / 2); ++i)
  	if(s[i] != s[s.size() - i - 1])
  		return false;
  return true;
}
int main( int argc, const char* argv[] ){
  int cases;
  cin >> cases;
  for(int z = 0; z < cases; ++z){
  	int start, end, count = 0;
  	cin >> start;
  	cin >> end;

  	for(int i = start; i <= end; ++i){
      double d = sqrt(i);
      int x = d;

      if(d == x)
    		if(isPal(i) && isPal(x))
    			++count;
  	}
    printf("Case #%d: %d\n", z + 1, count);
  }
  return 0;
}