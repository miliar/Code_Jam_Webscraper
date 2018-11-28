#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

void solve() {
  int n, k;
  cin >> n >> k;
  vector < double > prob(n);
  for(int i = 0; i < n; ++i)
    cin >> prob[i];
  vector < double > taken;
  double global = 0;
  sort(prob.begin(), prob.end());
  for(int it = 0; it <= k; ++it){
    for(int i = 0; i < it; ++i)
      taken.push_back(prob[i]);
    for(int i = it; i < k; ++i)
      taken.push_back(prob[n - 1 - i + it]);
    vector < double > res(k + 1, 0);
    vector < double > tmp(k + 1);
    res[0] = 1;
    for(int i = 0; i < k; ++i){
      tmp[0] = res[0] * (1 - taken[i]);
      for(int j = 1; j <= k; ++j){
        tmp[j] = res[j] * (1 - taken[i]) + res[j - 1] * taken[i];
      }
      tmp.swap(res);
    }
    global = max(global, res[k / 2]);
    taken.clear();
  }
  cout << global << endl;
}

int main() {
  cout.precision(12);
  int t;
  cin >> t;
  for(int i = 1; i <= t; ++i){
    cout << "Case #" << i << ": ";
    solve();
  }
}
