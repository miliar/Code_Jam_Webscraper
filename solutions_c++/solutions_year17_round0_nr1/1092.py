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

int main() {
  int t, k;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  int count = 10;
  for (int i = 1; i <= t; ++i) {
    string s;
    cin >> s >> k;
    int count = 0;
    bool inm = false;
    for(int j = 0; j < s.size(); j++){
      if(s[j] == '-' && j + k <= s.size()){
        for(int m = 0; m < k; m++){
          if(s[j + m] == '-')
            s[j + m] = '+';
          else
            s[j + m] = '-';
        }
        count++;
      }else if(s[j] == '-'){
        inm = true;
        break;
      }
    }
    if(inm)
      cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
    else
      cout << "Case #" << i << ": " << count << endl;
  }
  
  return 0;
}