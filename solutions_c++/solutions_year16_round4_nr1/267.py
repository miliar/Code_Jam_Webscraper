#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

string solve(const string& next, int& r, int& p, int& s, int lvl) {
  if(r < 0 || p < 0 || s < 0) return "";
  if(!lvl) return next;
  string lhs = solve(next, r, p, s, lvl - 1);
  if(lhs.empty()) return "";
  string rhs;
  if(next[0] == 'R'){
    --s;
    rhs = solve("S", r, p, s, lvl - 1);
  }else if(next[0] == 'P'){
    --r;
    rhs = solve("R", r, p, s, lvl - 1);
  }else{
    --p;
    rhs = solve("P", r, p, s, lvl - 1);
  }
  if(rhs.empty()) return "";
  if(rhs < lhs) lhs.swap(rhs);
  return lhs + rhs;
}

void solve() {
  int n, r, p, s;
  cin >> n >> r >> p >> s;
  int x = r - 1;
  int y = p;
  int z = s;
  string a = solve("R", x, y, z, n);
  x = r;
  y = p - 1;
  z = s;
  string b = solve("P", x, y, z, n);
  x = r;
  y = p;
  z = s - 1;
  string c = solve("S", x, y, z, n);
  if(a.empty() && b.empty() && c.empty()){
    cout << "IMPOSSIBLE" << endl;
  }else{
    if(a.empty()) a = "Z";
    if(b.empty()) b = "Z";
    if(c.empty()) c = "Z";
    cout << min(a, min(b, c)) << endl;
  }
}

int main() {
  int t;
  cin >> t;
  for(int i = 1; i <= t; ++i){
    cout << "Case #" << i << ": ";
    solve();
  }
}
