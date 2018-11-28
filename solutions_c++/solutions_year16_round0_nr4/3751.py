#include <cmath>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
  
  int t,k,s,c;
  cin >> t;
  for(int j = 0;j < t;j++){
      cin >> k >> s >> c;
      cout << "Case #" << j+1 << ": "; 
      for(int i = 0;i < k;i++) cout << i+1 << " "; 
      cout << endl;
  }
    
   
  return 0;
}