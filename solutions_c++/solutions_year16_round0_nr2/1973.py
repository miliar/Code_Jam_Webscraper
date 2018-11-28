#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <map>
#include <climits>
#include <stack>
#include <string>
#include <stdio.h>
#include <ctype.h>
#include <cstdint>
#include <unordered_set>
#include <unordered_map>
#include <utility>
#include <math.h>

using namespace std;

void flipAndSwap(string& s, int index){
  for(int i = 0; i <= index; i++){
    if(s[i] == '+')
      s[i] = '-';
    else
      s[i] = '+';
  }
  
  int start = 0;
  while(start < index){
    int temp = s[index];
    s[index] = s[start];
    s[start] = temp;
    start++;
    index--;
  }
}

void maneuver(string& s, int last, int& count){
  if(s[0]=='+'){
    int sum = 0;
    while(s[sum] == '+')
      sum++;
    flipAndSwap(s, sum - 1);
    count++;
  }
  
  flipAndSwap(s, last);
  count++;
  while(last >= 0 && s[last] == '+'){
    last--;
  }
  
  if(last >= 0)
    maneuver(s, last, count);
}

int main() {
  int t, n;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  string s;
  for (int i = 1; i <= t; ++i) {
    cin >> s;
    
    int count = 0;
    int last = s.size() - 1;
    while(last >= 0 && s[last] == '+')
      last--;
    
    if(last >= 0)
      maneuver(s, last, count);
    
      cout << "Case #" << i << ": " << count << endl;
  }
  
  return 0;
}
