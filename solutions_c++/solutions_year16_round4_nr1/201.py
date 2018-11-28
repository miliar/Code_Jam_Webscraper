#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <set>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <map>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef vector<pii> vii;
typedef vector<string> vs;

int main() {
  int T;
  cin >> T;
  for (int test = 1; test <= T; ++test) {
    printf("Case #%d: ", test);
    int n,R,P,S;
    cin >> n >> R >> P >> S;
    vector<string> s(3);
    s[0] = 'P';
    s[1] = 'R';
    s[2] = 'S';
    for (int t = 1; t <= n; ++t) {
      vs ns(3);
      for (int i = 0; i < 3; ++i) {
        string s1 = s[i];
        string s2 = s[(i+1)%3];
        ns[i] = min(s1+s2, s2+s1);
      }
      s.swap(ns);
    }
    string res = "";
    for (int i = 0; i < 3; ++i) {
//      cerr << s[i] << endl;
      int cr=0,cp=0,cs=0;
      for (char x : s[i]) {
        if (x == 'P') ++cp;
        if (x == 'R') ++cr;
        if (x == 'S') ++cs;
        if (cs == S && cp == P && cr == R && (res.size() == 0 || res > s[i])) {
          res = s[i];
        }
      }
    }
    if (res == "") cout << "IMPOSSIBLE\n";
    else cout << res << endl;
  }
  return 0;
}
