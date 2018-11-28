#include <bits/stdc++.h>

using namespace std;

void solve() {
  int p;
  cin >> p;
  vector<long long> e(p);
  vector<long long> f(p);
  for (int i = 0; i < p; ++i) cin >> e[i];
  for (int i = 0; i < p; ++i) cin >> f[i];
  map<long long, long long> mp;
  for (int i = 0; i < p; ++i) mp[e[i]] = f[i];
  int cnt = 0;
  while (mp.size() > 1u || mp[0] > 1) {
    long long a;
    if (mp[0] > 1) {
      a = 0;
    } else {
      auto itr = mp.begin();
      ++itr;
      a = itr->first;
    }
    auto tmp = mp;
    for (const auto& k : tmp) {
      if (mp.count(k.first) == 0 || mp[k.first] == 0) continue;
      if (a != 0) {
        //cerr << k.first << endl;
        mp[k.first + a] -= mp[k.first];
        if (mp[k.first + a] == 0) {
          //cerr << __LINE__ << " " << k.first + a << endl;
          mp.erase(k.first + a);
          //cerr << mp.count(k.first + a) << endl;
        }
      } else {
        mp[k.first] /= 2;
      }
    }
    cout << " " << a;
    ++cnt;
    //if (cnt == 2) break;
  }
  //for (const auto& k : mp) cerr << k.first << " " << k.second << endl;
}

int main() {
  int t;
  cin >> t;
  //#pragma omp parallel for
  for (int i = 0; i < t; ++i) {
    cout << "Case #" << i + 1 << ":";
    solve();
    cout << endl;
    //break;
  }
}
