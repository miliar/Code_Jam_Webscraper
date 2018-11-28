#include <iostream>
#include <vector>
#include <string>
#include <cstdio>

using namespace std;

int main()
{
  int t;
  string s;
  cin >> t;
  for(int i=0; i<t; ++i){
    int r = 0;
    int blank = true;
    cin >> s;
    while(blank){
      int flipPos = 0;
      for(flipPos=s.size()-1; flipPos>=0; --flipPos){
	if(s[flipPos] == '-') break;
      }
      if(flipPos == -1){
	blank = false;
      } else {
        for(int j=flipPos; j>=0; --j){
	  if(s[j] == '-') s[j] = '+';
	  else s[j] = '-';
	}
	r++;
      }
    }
    
    cout << "Case #" << i+1 << ": " << r << '\n';
  }
  
  return 0;
}
