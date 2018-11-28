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

static vector<long long> generate(int k, int c, int s){
  vector<long long> result;
  long long part;
  long long set = 1;
  long long remain = 0;
  if(c == 1)
    part = k;
  else{
     set = (long long)pow(2,(int)log2(c));
     part = k / set;
     remain = k % set;
  }
  
  if(remain == 0){
    if(s < part)
      return result;
  }else{
    if(s < part + 1)
      return result;
  }

  //long long base = set * (long long)pow(k, c - 1);
  //long long start = 0;
  for(int i = 0; i < part; i++){
    long long position = i * set + 1;
    for(int j = 2; j <= set; j++){
      position = k * (position - 1) + j + i * set;
    }
    
    for(int j = 1; j <= c - set; j++){
      position *= k;
    } 
    
    result.push_back(position);
    //result.push_back(start + position);
    //start += base;
  }
  
  if(remain != 0){
    long long position = part * set + 1;
    for(int j = 2; j <= remain; j++){
      position = k * (position - 1) + j + part * set;
    }
    for(int j = 1; j <= c - remain; j++){
      position *= k;
    } 
    //result.push_back(start + position);
    result.push_back(position);
  }
  
  return result;
}

int main() {
  int t, k, c, s;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> k >> c >> s;
    vector<long long> result = generate(k, c, s);
    
    cout << "Case #" << i << ": ";
    if(result.empty())
      cout << "IMPOSSIBLE" << endl;
    else{
      for(int i = 0; i < result.size(); i++){
        cout << result[i] << " ";
      }
      cout << endl;
    }
    
  }
  
  return 0;
}
