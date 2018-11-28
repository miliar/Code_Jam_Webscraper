#include <algorithm>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

using namespace std;

bool check(int ptr, const vector < int > & perm, vector < int > & used, const vector < string > & v) {
  if(ptr == perm.size()) return true;
  int id = perm[ptr];
  bool found = false;
  for(size_t i = 0; i < v.size(); ++i){
    if(used[i]) continue;
    if(v[id][i] == '0') continue;
    found = true;
    used[i] = 1;
    if(!check(ptr + 1, perm, used, v)) return false;
    used[i] = 0;
  }
  return found;
}

int solve(vector < string > v, int mask) {
  int added = 0;
  for(size_t i = 0; i < v.size(); ++i){
    for(size_t j = 0; j < v.size(); ++j){
      if(mask & (1 << (i * v.size() + j))){
        if(v[i][j] == '0'){
          v[i][j] = '1';
          ++added;
        }
      }
    }
  }
  vector < int > used(v.size(), 0);
  vector < int > perm(v.size());
  iota(perm.begin(), perm.end(), 0);
  do{
    if(!check(0, perm, used, v)){
      return 16;
    }
  }while(next_permutation(perm.begin(), perm.end()));
  return added;
}

void solve() {
  int n;
  cin >> n;
  vector < string > v(n);
  for(int i = 0; i < n; ++i){
    cin >> v[i];
  }
  int ans = 16;
  for(int i = 0; i < (1 << (n * n)); ++i){
    ans = min(ans, solve(v, i));
  }
  cout << ans << endl;
}

int main() {
  int t;
  cin >> t;
  for(int i = 1; i <= t; ++i){
    cout << "Case #" << i << ": ";
    solve();
  }
}
