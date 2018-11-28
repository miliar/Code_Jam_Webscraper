#include <iostream>
#include <sstream>
#include <string>
#include <map>
#include <utility>
#include <cmath>

using namespace std;


typedef unsigned long long int inte;

map<inte, bool> palCache;

bool isPal(inte x) {
  stringstream s;
  s << x;
  string st = s.str();
  for(int i = 0; i < st.length() / 2; ++i) {
    if(st[i] != st[st.length() - i - 1]) {
      return false;
    }
  }
  return true;
}

int main() {
  int cases;
  cin >> cases;
  inte a, b;

  for(int i = 0; i < cases; ++i) {
    int c = 0;
    cin >> a >> b;
    for(inte j = a; j <= b; ++j) {
      if(isPal(j)) {
        inte s = sqrt((long double)j);
        if((s * s) == j && isPal(s)) {
          ++c;
        }
      }
    }
    cout << "Case #" << (i + 1) << ": " << c << endl;
  }
  return 0;
}

