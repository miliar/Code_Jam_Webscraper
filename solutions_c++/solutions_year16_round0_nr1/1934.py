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

static void check(vector<int>& myvec, int n, int& count){
  while(n > 0){
    if(myvec[n%10] == 0){
      myvec[n%10]++;
      count--;
    }
    n /= 10;
  }
}

int main() {
  int t, n;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  vector<int> vec(10,0);
  int count = 10;
  for (int i = 1; i <= t; ++i) {
    cin >> n;
    if(n == 0)
      cout << "Case #" << i << ": " << "INSOMNIA" << endl;
    else{
      int base = n;
      while(1){
        check(vec, n, count);
        if(count==0){
          break;
        }
        n += base;
      }
      cout << "Case #" << i << ": " << n << endl;
    }
    
    for(int j = 0; j < 10; j++){
      vec[j] = 0;
    }
    count = 10;
  }
  
  return 0;
}
