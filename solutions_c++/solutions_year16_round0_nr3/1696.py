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

static void generateString(vector<string>& vec, string s, int& count, int start, int end){
    if(count <= 0){
      return;
    }
    
    if(start >= end){
      vec.push_back(s);
      count--;
      return;
    }
    
    generateString(vec, s, count, start + 2, end);
    if(count <= 0)
      return;
    s[start] = '1';
    s[start + 1] = '1';
    generateString(vec, s, count, start + 2, end);
}

static vector<string> generate(int n, int J){
  string s(n, '0');
  s[0] = '1';
  s[1] = '1';
  s[n - 1] = '1';
  s[n - 2] = '1';
  vector<string> myvec;
  
  generateString(myvec, s, J, 2, n - 2);
  return myvec;
}

int main() {
  int t;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  int n, J;
  for (int i = 1; i <= t; ++i) {
    cin >> n >> J; 
    vector<string> result = generate(n, J);
    cout << "Case #" << i << ": "<< endl;
    for(int m = 0; m < result.size(); m++){
      cout << result[m] << " ";
      for(int h = 3; h <= 11; h++){
        cout << h << " ";
      }
    cout << endl;
    }
  }
  
  return 0;
}
