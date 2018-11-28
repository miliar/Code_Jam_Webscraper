#include<iostream>
#include<vector>

using namespace std;

#define rep(i, n) for (int i = 0; i < int(n); ++i)

void solve() {
  int k1, k2, t1[4][4], t2[4][4];
  cin >> k1;
  rep (i, 4) rep (j, 4) cin >> t1[i][j];
  cin >> k2;
  rep (i, 4) rep (j, 4) cin >> t2[i][j];
  --k1, --k2;
  vector<int> v;
  rep (i, 4) rep (j, 4) if (t1[k1][i] == t2[k2][j]) v.push_back(t1[k1][i]);
  if (v.empty()) cout << "Volunteer cheated!" << endl;
  else if (v.size() == 1u) cout << v[0] << endl;
  else cout << "Bad magician!" << endl;
}

int main() {
  int t;
  cin >> t;
  rep (i, t) {
    cout << "Case #" << i + 1 << ": ";
    solve();
  }
}
