#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <array>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <functional>

using namespace std;

bool isVovel(const char c) {
  return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

bool checkNvalue(const string& name, const uint64_t n, const int start, const int end) {
  // cout << __PRETTY_FUNCTION__ << ": " << start << " to " << end << endl;
  int slength = 0;
  int maxslength = 0;
  for(int i = start; i <= end; ++i) {
    if(!isVovel(name[i])) {
      slength++;
    } else {
      if(maxslength < slength) maxslength = slength;
      slength = 0;
    }
  }
  if(maxslength < slength) maxslength = slength;
  return maxslength >= n;
}

uint64_t findNValue(const string& name, const uint64_t n) {
  uint64_t nvalue;
  for(int i = 0; i < name.size(); ++i) {
    for(int j = name.size()-1; j >= i; --j) {
      bool hasNconsonants = checkNvalue(name,n,i,j);
      if(hasNconsonants)
        nvalue++;
    }
  }
  return nvalue;
}

int main() {
  int T;
  cin >> T;
  for(int i = 0; i < T; ++i) {
    string name;
    cin >> name;
    uint64_t n;
    cin >> n;
    uint64_t realN = findNValue(name,n);
    cout << "Case #" << i+1 << ": " << realN << endl;
  }
}
