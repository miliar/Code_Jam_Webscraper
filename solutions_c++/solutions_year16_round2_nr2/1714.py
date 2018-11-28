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

bool match(string s, int i) {
  int l = s.size()-1;
  string tmp = to_string(i);
  tmp = string(s.size() - tmp.size(), '0') + tmp;
  for (int i = 0; i < s.size(); ++i)
    if (s[i] != '?')
      if (s[i] != tmp[i])
        return false;
  return true;
}

void doit() {
  string c, j;
  cin >> c >> j;
  int wid = c.size();

  int ll = -1, rr = -1;


  for (int i = 0; i < (int)(pow(10, wid)); ++i) {
    for (int k = 0; k < (int)(pow(10, wid)); ++k) {
      if (match(c, i) && match(j, k)) {
        if (ll == -1) {
          ll = i;
          rr = k;
        }
        if (abs(ll-rr) > abs(i-k)) {
          ll = i; rr = k;
        }
        if (abs(ll-rr) == abs(i-k)) {
          if (ll >= i) {
            if (i < ll) {
              ll = i;
              rr = k;
            } else if (i == ll && k < rr) {
              ll = i;
              rr = k;
            }
          }
        }
      }
    }
  }
  cout <<setw(wid) << setfill('0')<< ll << " " <<setw(wid) << setfill('0')<< rr << endl;

}

int main() {
  ios::sync_with_stdio(false);

  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t<< ": ";
    doit();
  }

}
