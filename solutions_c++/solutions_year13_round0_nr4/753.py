#include <iostream>
#include <vector>

using namespace std;

int n;
vector<int> mem_solve;
vector<int> initial;
vector<int> lock;
vector<vector<int> > keys;

int solve(int bm) {
  int &ret = mem_solve[bm];
  if (ret != -1) return ret;
  if (bm == (1<<n)-1) return n;
  vector<int> have = initial;
  for (int i = 0; i < n; ++i) if (((bm>>i)&1) == 1) {
    --have[lock[i]];
    for (int j = 0; j < int(keys[i].size()); ++j) {
      ++have[keys[i][j]];
    }
  }
  for (int i = 0; i < n; ++i) if (((bm>>i)&1) == 0) {
    if (have[lock[i]] > 0 && solve(bm|(1<<i)) >= 0) {
      return ret = i;
    }
  }
  return ret = -2;
}

int main() {
  int t;
  cin >> t;
  for (int ca = 1; t--; ++ca) {
    int k;
    cin >> k >> n;
    initial = vector<int>(200, 0);
    for (int i = 0; i < k; ++i) {
      int ktype;
      cin >> ktype;
      --ktype;
      ++initial[ktype];
    }
    lock = vector<int>(n);
    keys = vector<vector<int> >(n);
    for (int i = 0; i < n; ++i) {
      int nk;
      cin >> lock[i] >> nk;
      --lock[i];
      for (int j = 0; j < nk; ++j) {
        int ktype;
        cin >> ktype;
        --ktype;
        keys[i].push_back(ktype);
      }
    }
    
    mem_solve = vector<int>(1<<n, -1);
    cout << "Case #" << ca << ": ";
    if (solve(0) >= 0) {
      for (int bm = 0; bm != (1<<n)-1; bm |= (1<<solve(bm))) {
        if (bm != 0) cout << " ";
        cout << solve(bm)+1;
      }
      cout << endl;
    }
    else {
      cout << "IMPOSSIBLE" << endl;
    }
  }
}
