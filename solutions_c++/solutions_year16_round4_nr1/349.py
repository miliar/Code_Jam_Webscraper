/*{{{*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <unordered_map>
#include <unordered_set>
#include <cassert>
using namespace std;
typedef pair<int, int> PP;
typedef long long LL;
#define pb push_back
#define fr first
#define sc second
#define bitcnt __builtin_popcount
#define all(x) x.begin(), x.end()
inline int ri() {int x; scanf("%d", &x); return x;}
#define rep2(i, n, ...) for (int i = 0; i < (n); i ++) 
#define rep3(i, a, b, ...) for (int i = (a); i < (b); i ++)
#define GET_MACRO(_1, _2, _3, NAME, ...) NAME
#define rep(...) GET_MACRO(__VA_ARGS__, rep3, rep2)(__VA_ARGS__)
#define drep2(i, n, ...) for (int i = (n) - 1; i >= 0; i --)
#define drep3(i, a, b) for (int i = (a) - 1; i >= (b); i --)
#define drep(...) GET_MACRO(__VA_ARGS__, drep3, drep2)(__VA_ARGS__)
template<typename T>inline bool smax(T&a, T b){if(a<b){a=b;return true;}return false;} 
template<typename T>inline bool smin(T&a, T b){if(a>b){a=b;return true;}return false;} 
/*}}}*/




string check(int p, int r, int s) {
  if (p < 0 || r < 0 || s < 0) return "";
  if (p + r + s == 1) {
    if (p) return "P";
    else if (r) return "R";
    else if (s) return "S";
  }
  int n = p + r + s;
  if (n % 2 == 1) return "";
  n /= 2;
  int pr, ps, sr;
  pr = p + r - n;
  ps = p + s - n;
  sr = s + r - n;
  string hs = check(pr, sr, ps);
  string res = "";
  for (auto c : hs) {
    if (c == 'P') res += "PR";
    if (c == 'R') res += "RS";
    else if (c == 'S') res += "PS";
  }
  return res;
}
string sort(string s) {
  int n = s.length() / 2;
  if (n == 0) return s;
  string l = sort(s.substr(0, n));
  string r = sort(s.substr(n, n));
  if (l < r) return l + r;
  else return r + l;
}
void solve() {
  int m, p, r, s; cin >> m;
  cin >> r >> p >> s;
  string res = check(p, r, s);
  if (res.length()) cout << sort(res) << endl;
  else cout << "IMPOSSIBLE" << endl;

}

int main() {
  #ifdef _TEST_
  freopen("input.txt", "r", stdin);
  //freopen("out.txt", "w", stdout);
    
  #endif
  int Q; cin >> Q;
  rep(i, Q) {
    cout << "Case " << "#" << i + 1 << ": ";
    solve();
  }
  return 0;
}
