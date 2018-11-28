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
#include <deque>

using namespace std;

static vector<int> dealString(string s, vector<string>& ref){
  int arr[] = {0,2,4,6,8,7,1,3,5,9};
  char cap[] = {'Z','W','U','X','G','S','O','T','V','I'};
  vector<int> myvec(26,0);
  for(int i = 0; i < s.size(); i++){
    myvec[int(s[i]-'A')]++;
  }
  
  vector<int> result(10,0);
  for(int i = 0; i < 10; i++){
    result[arr[i]] = myvec[cap[i]-'A'];
    for(int j = 0; j < ref[arr[i]].size();j++){
      myvec[ref[arr[i]][j]-'A'] -= result[arr[i]];
    }
  }
  return result;
}

int main() {
  int t;
  string s;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  vector<string> ref;
  ref.push_back("ZERO");
  ref.push_back("ONE");
  ref.push_back("TWO");
  ref.push_back("THREE");
  ref.push_back("FOUR");
  ref.push_back("FIVE");
  ref.push_back("SIX");
  ref.push_back("SEVEN");
  ref.push_back("EIGHT");
  ref.push_back("NINE");
  
  
  
  for (int k = 1; k <= t; ++k) {
    cin >> s;
    vector<int> result = dealString(s, ref);
    cout << "Case #" << k << ": ";
    for(int i = 0; i < result.size(); i++){
      for(int j = 0; j < result[i]; j++){
        cout << i ;
      }
    }
    cout << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
  
  return 0;
}