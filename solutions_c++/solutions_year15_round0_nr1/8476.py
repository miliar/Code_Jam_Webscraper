#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <stdio.h>
#include <map>
#include <sstream>
#include <fstream>

using namespace std;

int Smax = 1000;
int T = 0;
int cur_s = 0;
int L;
int ov[1001];

int dig(const char& s) {  
  return s - (int) '0';
}

void input_case() {  
  cin >> L;
  string s;  
  cin >> s;  
  for (int i=0; i<L+1; ++i) {
    ov[i] = dig(s[i]);
  }
}

int answer() {
  int friends = 0;
  int tot = 0;
  for (int i=0; i<L+1; ++i) {    
  
  //cout << "i = " << i << " tot = " << friends << " req: " << ov[i] << endl;
  if (tot >= i){
        tot += ov[i];
  } else {
    while (tot <= i) {      
      tot += 1;
      friends += 1;
      if (tot >= i)
        tot += ov[i];
    }
  }
  }
  return friends;
}


int main() {
  int res;
  cin >> T;
  
  for (int i=1; i<= T; ++i) {
    input_case();    
    res = answer();
    cout << "Case #" << i << ": " << res << endl;
  }
  return 0;
}