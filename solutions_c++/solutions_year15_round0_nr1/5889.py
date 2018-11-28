#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <bitset>
#include <deque>
#include <sstream>
#include <utility>
#include <functional>
#include <numeric>
#include <stack>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <iomanip>

using namespace std;

void solve(const int &number, const int &sz, const string &s) {
  vector< int > v(sz, 0);
  for (int i = 0; i < sz; i++) 
    v[i] = s[i] - '0';
  int ans = 0;
  for (int req = 1; req < sz; req++) {
    if (v[req] == 0) {
      v[req] += v[req - 1];
    }
    else {
      int cur = v[req - 1];
      if (cur >= req) {
        v[req] += cur;
      }
      else {
        int more = req - cur;
        v[req] += more + cur;
        ans += more;
      } 
    }
  }
  cout << "Case #" << number << ": " << ans << endl;
}

int main() {
  ios_base::sync_with_stdio(0);
  int tt;
  cin >> tt;
  for (int at = 1; at <= tt; at++) {
    int x;
    string s;
    cin >> x >> s;
    solve(at, x + 1, s);
  }
  return 0;
}