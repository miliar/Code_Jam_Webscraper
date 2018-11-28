#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <fstream>
#include <string>

using namespace std;


int main() {
  int tc, n, extra;
  string s;
  cin >> tc;
  for (int t=1; t<=tc; t++) {
    cin >> n;
    cin >> s;
    int tot = 0;
    int res = 0;
    for (int i=0; i<s.size(); i++) {
      extra = 0;
      if (i > tot) {
        extra = i - tot;
      }
      tot += s[i]-'0' + extra;
      res += extra;
    }
    cout << "Case #"<<t<<": "<< res << endl;
  }

  return 0;
}
