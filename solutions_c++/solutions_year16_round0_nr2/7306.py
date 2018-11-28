
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <cstring>

using namespace std;


int calcflips(string s) {
  bool first = true;
  int flips = 0;
  bool badpatch = false;
  for(int i = 0; i < s.size(); i++) {
    char c = s[i];
    if(first) {
      first = false;
      bool did = false;
      while(c == '-' && i < s.size()) {
        flips = 1;
        i++;
        c = s[i];
        did = true;
      }
      if(did) {
        i--;
      }
      continue;
    }

    if(c == '+') {
      if(badpatch == true) {
        flips += 2;
      }
      badpatch = false;
    }
    else {
      badpatch = true;
    }
  }

  if(badpatch == true) {
    flips += 2;
  }

  return flips;
}

int main() {

  int kases;
  cin >> kases;
  cin >> ws;
  for(int k = 0; k < kases; k++) {
    string s;
    getline(cin, s);
    int a = calcflips(s);
    cout << "Case #" << k+1 << ": " << a << endl;
  }

  return 0;
}
