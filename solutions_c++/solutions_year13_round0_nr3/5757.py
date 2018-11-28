#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>
using namespace std;
typedef long long lli;

string toString(lli i) {
  char buff[128];
  sprintf(buff, "%lld", i);
  return string(buff);
}

bool isPali(const string &s) {
  for(int i = 0; i < s.size()-1-i; ++i) {
    if(s[i] != s[s.size()-1-i]) return false;
  }
  return true;
}

int main() {
  int T;
  cin >> T;
  for(int tc = 0; tc < T; ++tc) {
    lli A, B;
    cin >> A >> B;
    lli cnt = 0;
    for(lli i = 0; i*i <= B; ++i) {
      lli v = i*i;
      if(A <= v) ; else continue;
      cnt += isPali(toString(i)) && isPali(toString(v));
    }
    cout << "Case #" << tc+1 << ": " << cnt << endl;
  }
  return 0;
}
