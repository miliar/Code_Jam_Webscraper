#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

bool prev(const vector < int > & a, const vector < int > & b) {
  for(size_t i = 0; i < a.size(); ++i)
    if(a[i] > b[i]) return false;
  return true;
}

bool check(int n, int mask, const vector < vector < int > > & lines) {
  int prevRow = -1;
  int prevCol = -1;
  vector < int > rows;
  vector < int > cols;
  for(int i = 0; i < n * 2 - 1; ++i){
    if(mask & (1 << i)){
      if(prevRow != -1)
        if(!prev(lines[prevRow], lines[i])) return false;
      prevRow = i;
      rows.push_back(i);
    }else{
      if(prevCol != -1)
        if(!prev(lines[prevCol], lines[i])) return false;
      prevCol = i;
      cols.push_back(i);
    }
  }
  int next = 0;
  for(int i = 0; i + 1 < n && next < n; ++i){
    for(int j = 0; j < n; ++j){
      if(lines[rows[j]][next] != lines[cols[i]][j]){
        ++next;
        --i;
        break;
      }
    }
  }
  return next < n;
}

void recursive(int p, int r, int c, int n, int mask, const vector < vector < int > > & lines, vector < int > & res) {
  if(!res.empty()) return;
  if(p == 2 * n - 1){
    if(!check(n, mask, lines)) return;
    map < int, int > rows;
    map < int, int > cols;
    for(int i = 0; i < 2 * n - 1; ++i){
      for(int j = 0; j < n; ++j){
        if(mask & (1 << i)) ++rows[lines[i][j]];
        else ++cols[lines[i][j]];
      }
    }
    for(const auto& cnt: rows){
      for(int i = cols[cnt.first]; i < cnt.second; ++i){
        res.push_back(cnt.first);
      }
    }
    return;
  }
  if(r != n) recursive(p + 1, r + 1, c, n, mask | (1 << p), lines, res);
  if(c + 1 != n) recursive(p + 1, r, c + 1, n, mask, lines, res);
}

void solve() {
  int n;
  cin >> n;
  vector < vector < int > > lines(n * 2 - 1);
  for(int i = 0; i < n * 2 - 1; ++i){
    lines[i].resize(n);
    for(int j = 0; j < n; ++j)
      cin >> lines[i][j];
  }
  sort(lines.begin(), lines.end());
  vector < int > res;
  recursive(0, 0, 0, n, 0, lines, res);
  for(int i = 0; i < n; ++i)
    cout << ' ' << res[i];
  cout << endl;
}

int main() {
  int n;
  cin >> n;
  for(int i = 1; i <= n; ++i){
    cout << "Case #" << i << ":";
    solve();
  }
}
