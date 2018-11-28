#include <iostream>
#include <vector>
#include <set>
using namespace std;

int m, n;
string s[1010];
vector<int> shard[110];
int maxv = 0, maxct = 0;

int nodes(vector<int>& v) {
  set<string> nd;
  for (int i = 0; i < v.size(); i++)
    for (int j = 0; j <= s[v[i]].size(); j++)
      nd.insert(s[v[i]].substr(0, j));
  return nd.size();
}

void go(int idx) {
  if (idx == m) {
    int v = 0;
    for (int i = 0; i < n; i++) {
      // cout << "shard " << i << ":";
      // for (int j = 0; j < shard[i].size(); j++) cout << " " << shard[i][j];
      // cout << endl;
      v += nodes(shard[i]);
    }
    // cout << v << endl;
    if (v > maxv) { maxv = v; maxct = 1; }
    else if (v == maxv) maxct += 1;
    return;
  }

  for (int i = 0; i < n; i++) {
    shard[i].push_back(idx);
    go(idx + 1);
    shard[i].pop_back();
  }
}

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    cin >> m >> n;
    for (int i = 0; i < m; i++) cin >> s[i];
    for (int i = 0; i < n; i++) shard[i].clear();
    maxv = maxct = 0;

    go(0);
    cout << "Case #" << c << ": " << maxv << " " << maxct << endl;
  }
  return 0;
}
