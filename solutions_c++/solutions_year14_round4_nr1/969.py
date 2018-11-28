#include <algorithm>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int ca = 1; ca <= T; ++ca) {
    int n, x;
    cin >> n >> x;
    vector<int> s(n);
    for (int i = 0; i < n; ++i) {
      cin >> s[i];
    }
    sort(s.begin(), s.end());
    set<pair<int, int> > a;
    for (int i = 0; i < n; ++i) {
      a.insert(pair<int, int>(s[i], i));
    }
    
    int ans = 0;
    for (int i = n-1; i >= 0; --i) if (s[i] != -1) {
      ++ans;
      a.erase(pair<int, int>(s[i], i));
      if (a.size() == 0) continue;
      set<pair<int, int> >::iterator it = a.upper_bound(pair<int, int>(x-s[i], n));
      if (it == a.begin()) continue;
      --it;
      s[i] = -1;
      s[it->second] = -1;
      a.erase(it);
    }
    
    cout << "Case #" << ca << ": " << ans << endl;
  }
}

