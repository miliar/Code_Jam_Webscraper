#include <algorithm>
#include <bitset>
#include <cstdio>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string.h>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

string q[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

bool has(string& s, const string v) {
  string cpy = s;
  for (char c : v) {
    int pos;
    if ((pos = cpy.find(c)) == string::npos) {
      return false;
    }
    cpy[pos] = '_';

  }
  s = cpy;
  return true;
}

bool correct(string& s) {
  return s.find_first_not_of("_") == string::npos;
}

string dig(string s, int pos, string sofar) {
  if (pos < 0) {
    if (correct(s)) {
      sort(sofar.begin(), sofar.end());
      return sofar;
    }
    return "";
  }

  string tmp = dig(s, pos-1, sofar);
  if (tmp != "") return tmp;
  tmp = s;
  
  while (has(tmp, q[pos])) {
    sofar = sofar + to_string(pos);
    string tt = dig(tmp, pos-1, sofar);
    if (tt != "")
      return tt;
  }
  return dig(s, pos-1, sofar);
}


void doit() {
  string s;
  cin >> s;

  cout << dig(s, 9, "") << endl;
}

int main() {
  ios::sync_with_stdio(false);

  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #"<<t<<": ";
    doit();
  }

}
